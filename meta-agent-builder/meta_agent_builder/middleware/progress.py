"""ProgressTrackingMiddleware for monitoring execution progress."""

import time
from typing import Any

from langchain_core.messages import AIMessage, ToolMessage


class ProgressTrackingMiddleware:
    """Middleware that tracks execution progress and provides status updates.

    This middleware monitors:
    - Task completion progress
    - Time elapsed
    - Current phase/specialist
    - Tool usage statistics
    - Estimated time remaining
    """

    def __init__(
        self,
        report_interval: int = 5,
        track_tool_usage: bool = True,
        estimate_completion: bool = True,
    ):
        """Initialize ProgressTrackingMiddleware.

        Args:
            report_interval: Report progress every N messages
            track_tool_usage: Track which tools are being used
            estimate_completion: Estimate time remaining
        """
        self.report_interval = report_interval
        self.track_tool_usage = track_tool_usage
        self.estimate_completion = estimate_completion
        self.start_time = None

    async def __call__(
        self,
        state: dict[str, Any],
        config: dict[str, Any],
        store: Any,
    ) -> dict[str, Any]:
        """Track progress for current state.

        Args:
            state: Current agent state
            config: Configuration
            store: Store instance

        Returns:
            Updated state with progress tracking
        """
        # Initialize tracking on first call
        if "progress_tracking" not in state:
            state["progress_tracking"] = {
                "start_time": time.time(),
                "message_count": 0,
                "tool_calls": [],
                "phases": [],
                "current_phase": None,
                "specialists_used": set(),
            }
            self.start_time = time.time()

        tracking = state["progress_tracking"]
        messages = state.get("messages", [])

        # Update message count
        tracking["message_count"] = len(messages)

        # Track tool usage
        if self.track_tool_usage and messages:
            last_message = messages[-1]

            # Track tool calls
            if isinstance(last_message, ToolMessage):
                tool_name = getattr(last_message, "name", "unknown")
                tracking["tool_calls"].append({
                    "tool": tool_name,
                    "timestamp": time.time(),
                })

            # Track specialist usage (from AI messages)
            if isinstance(last_message, AIMessage):
                content = getattr(last_message, "content", "")
                # Look for specialist mentions
                for specialist in [
                    "documentation-specialist",
                    "architecture-specialist",
                    "prd-specialist",
                    "context-specialist",
                    "middleware-specialist",
                    "orchestration-specialist",
                    "implementation-specialist",
                ]:
                    if specialist in content.lower():
                        tracking["specialists_used"].add(specialist)

        # Detect phase changes
        current_phase = self._detect_phase(messages)
        if current_phase != tracking["current_phase"]:
            tracking["phases"].append({
                "phase": current_phase,
                "started_at": time.time(),
                "message_index": len(messages),
            })
            tracking["current_phase"] = current_phase

        # Report progress at intervals
        if len(messages) % self.report_interval == 0 and len(messages) > 0:
            progress_report = self._generate_progress_report(tracking)
            # In a real implementation, we might add this to state or log it
            # For now, we just calculate it
            state["latest_progress_report"] = progress_report

        return state

    def _detect_phase(self, messages: list) -> str:
        """Detect current execution phase from messages.

        Args:
            messages: List of messages

        Returns:
            Current phase name
        """
        if not messages:
            return "initializing"

        # Look at recent messages to detect phase
        recent_content = ""
        for msg in messages[-5:]:  # Look at last 5 messages
            if hasattr(msg, "content"):
                recent_content += msg.content.lower()

        # Detect phases based on keywords
        if "documentation" in recent_content or "research" in recent_content:
            return "documentation_research"
        elif "architecture" in recent_content or "design" in recent_content:
            return "architecture_design"
        elif "prd" in recent_content or "requirements" in recent_content:
            return "requirements_definition"
        elif "context" in recent_content or "prompt" in recent_content:
            return "context_engineering"
        elif "middleware" in recent_content:
            return "middleware_design"
        elif "orchestration" in recent_content or "workflow" in recent_content:
            return "orchestration_design"
        elif "implementation" in recent_content or "code" in recent_content:
            return "implementation_planning"
        elif "summary" in recent_content or "complete" in recent_content:
            return "finalization"
        else:
            return "processing"

    def _generate_progress_report(self, tracking: dict[str, Any]) -> dict[str, Any]:
        """Generate progress report.

        Args:
            tracking: Tracking data

        Returns:
            Progress report dictionary
        """
        elapsed = time.time() - tracking["start_time"]

        report = {
            "elapsed_seconds": elapsed,
            "elapsed_formatted": self._format_time(elapsed),
            "message_count": tracking["message_count"],
            "current_phase": tracking["current_phase"],
            "phases_completed": len(tracking["phases"]) - 1,  # -1 for current phase
            "tool_calls_count": len(tracking["tool_calls"]),
            "specialists_used": list(tracking["specialists_used"]),
            "specialists_count": len(tracking["specialists_used"]),
        }

        # Add tool usage breakdown
        if tracking["tool_calls"]:
            tool_counts = {}
            for call in tracking["tool_calls"]:
                tool = call["tool"]
                tool_counts[tool] = tool_counts.get(tool, 0) + 1
            report["tool_usage"] = tool_counts

        # Estimate completion if enabled
        if self.estimate_completion and tracking["phases"]:
            # Simple estimation: assume 7 phases total
            total_phases = 7
            completed = len(tracking["phases"]) - 1
            if completed > 0:
                avg_time_per_phase = elapsed / completed
                remaining_phases = total_phases - completed
                estimated_remaining = avg_time_per_phase * remaining_phases
                report["estimated_remaining_seconds"] = estimated_remaining
                report["estimated_remaining_formatted"] = self._format_time(estimated_remaining)
                report["estimated_completion_percentage"] = (completed / total_phases) * 100

        return report

    def _format_time(self, seconds: float) -> str:
        """Format seconds into human-readable string.

        Args:
            seconds: Time in seconds

        Returns:
            Formatted time string
        """
        if seconds < 60:
            return f"{int(seconds)}s"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            secs = int(seconds % 60)
            return f"{minutes}m {secs}s"
        else:
            hours = int(seconds / 3600)
            minutes = int((seconds % 3600) / 60)
            return f"{hours}h {minutes}m"

    def get_final_report(self, state: dict[str, Any]) -> dict[str, Any]:
        """Get final execution report.

        Args:
            state: Final agent state

        Returns:
            Final report dictionary
        """
        if "progress_tracking" not in state:
            return {"error": "No tracking data available"}

        tracking = state["progress_tracking"]
        elapsed = time.time() - tracking["start_time"]

        phases_summary = []
        for i, phase in enumerate(tracking["phases"]):
            phase_data = {
                "phase": phase["phase"],
                "started_at_message": phase["message_index"],
            }

            # Calculate duration if not last phase
            if i < len(tracking["phases"]) - 1:
                next_phase = tracking["phases"][i + 1]
                duration = next_phase["started_at"] - phase["started_at"]
                phase_data["duration"] = self._format_time(duration)

            phases_summary.append(phase_data)

        return {
            "total_time": self._format_time(elapsed),
            "total_messages": tracking["message_count"],
            "total_tool_calls": len(tracking["tool_calls"]),
            "specialists_used": list(tracking["specialists_used"]),
            "phases": phases_summary,
            "tool_usage": self._generate_progress_report(tracking).get("tool_usage", {}),
        }
