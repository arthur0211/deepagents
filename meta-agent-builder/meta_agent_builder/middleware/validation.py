"""ValidationMiddleware for quality checking generated specifications."""

import re
from typing import Any

from langchain_core.messages import AIMessage


class ValidationMiddleware:
    """Middleware that validates outputs for quality and completeness.

    This middleware checks generated content for:
    - Minimum content length
    - Required sections
    - Code block formatting
    - Link validity
    - Markdown structure
    """

    def __init__(
        self,
        min_content_length: int = 100,
        required_sections: list[str] | None = None,
        validate_code_blocks: bool = True,
        validate_links: bool = True,
    ):
        """Initialize ValidationMiddleware.

        Args:
            min_content_length: Minimum characters for valid content
            required_sections: List of required markdown sections
            validate_code_blocks: Check code block formatting
            validate_links: Validate markdown links
        """
        self.min_content_length = min_content_length
        self.required_sections = required_sections or []
        self.validate_code_blocks = validate_code_blocks
        self.validate_links = validate_links

    async def __call__(
        self,
        state: dict[str, Any],
        config: dict[str, Any],
        store: Any,
    ) -> dict[str, Any]:
        """Validate the current state.

        Args:
            state: Current agent state
            config: Configuration
            store: Store instance

        Returns:
            Updated state with validation results
        """
        messages = state.get("messages", [])
        if not messages:
            return state

        last_message = messages[-1]

        # Only validate AI messages
        if not isinstance(last_message, AIMessage):
            return state

        content = getattr(last_message, "content", "")
        if not content:
            return state

        # Run validations
        issues = []

        # Check minimum length
        if len(content) < self.min_content_length:
            issues.append(
                f"Content too short: {len(content)} chars (min: {self.min_content_length})"
            )

        # Check required sections
        for section in self.required_sections:
            if not self._has_section(content, section):
                issues.append(f"Missing required section: {section}")

        # Validate code blocks
        if self.validate_code_blocks:
            code_issues = self._validate_code_blocks(content)
            issues.extend(code_issues)

        # Validate links
        if self.validate_links:
            link_issues = self._validate_links(content)
            issues.extend(link_issues)

        # Add validation results to state
        if "validation_results" not in state:
            state["validation_results"] = []

        validation_result = {
            "timestamp": "now",  # Would use datetime in real implementation
            "message_index": len(messages) - 1,
            "issues": issues,
            "passed": len(issues) == 0,
        }

        state["validation_results"].append(validation_result)

        # Optionally inject validation feedback
        if issues and len(issues) <= 3:  # Only for minor issues
            feedback_msg = AIMessage(
                content=f"⚠️ Validation issues found:\n" + "\n".join(f"- {issue}" for issue in issues)
            )
            # Note: In real middleware, we'd add this differently
            # This is simplified for demonstration

        return state

    def _has_section(self, content: str, section: str) -> bool:
        """Check if content has a markdown section.

        Args:
            content: Markdown content
            section: Section name to find

        Returns:
            True if section exists
        """
        # Look for markdown headers with this section
        patterns = [
            rf"^#+ {re.escape(section)}",  # # Section or ## Section
            rf"^#+ \*\*{re.escape(section)}\*\*",  # ## **Section**
        ]

        for pattern in patterns:
            if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                return True

        return False

    def _validate_code_blocks(self, content: str) -> list[str]:
        """Validate code block formatting.

        Args:
            content: Markdown content

        Returns:
            List of issues found
        """
        issues = []

        # Find all code blocks
        code_blocks = re.findall(r"```(\w*)\n(.*?)```", content, re.DOTALL)

        for i, (lang, code) in enumerate(code_blocks):
            # Check for language specification
            if not lang:
                issues.append(f"Code block #{i+1} missing language specification")

            # Check for empty code blocks
            if not code.strip():
                issues.append(f"Code block #{i+1} is empty")

        # Check for unclosed code blocks
        open_blocks = content.count("```")
        if open_blocks % 2 != 0:
            issues.append("Unclosed code block detected")

        return issues

    def _validate_links(self, content: str) -> list[str]:
        """Validate markdown links.

        Args:
            content: Markdown content

        Returns:
            List of issues found
        """
        issues = []

        # Find all markdown links
        links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", content)

        for text, url in links:
            # Check for empty link text
            if not text.strip():
                issues.append(f"Empty link text for URL: {url}")

            # Check for empty URL
            if not url.strip():
                issues.append(f"Empty URL for link text: {text}")

            # Check for placeholder URLs
            if url in ["#", "#todo", "TODO", "..."]:
                issues.append(f"Placeholder URL in link: [{text}]({url})")

        return issues

    def get_validation_summary(self, state: dict[str, Any]) -> dict[str, Any]:
        """Get summary of validation results.

        Args:
            state: Agent state with validation results

        Returns:
            Summary dictionary
        """
        results = state.get("validation_results", [])

        if not results:
            return {"total": 0, "passed": 0, "failed": 0, "issues": []}

        total = len(results)
        passed = sum(1 for r in results if r["passed"])
        failed = total - passed

        all_issues = []
        for result in results:
            all_issues.extend(result["issues"])

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": passed / total if total > 0 else 0,
            "issues": all_issues,
            "issue_count": len(all_issues),
        }
