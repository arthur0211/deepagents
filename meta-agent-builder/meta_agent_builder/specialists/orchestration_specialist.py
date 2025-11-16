"""Orchestration Specialist - Workflow and coordination expert."""

from meta_agent_builder.specialists.base import BaseSpecialist
from meta_agent_builder.tools import (
    design_error_handling,
    design_execution_flow,
    design_workflow_pattern,
    plan_agent_coordination,
    plan_communication_protocol,
    plan_result_aggregation,
)


class OrchestrationSpecialist(BaseSpecialist):
    """Specialist for designing workflow orchestration and agent coordination.

    This specialist designs:
    - Workflow orchestration patterns
    - Agent coordination and delegation strategies
    - Result aggregation approaches
    - Error handling and recovery mechanisms
    - Communication protocols
    - Execution flows with branching

    Outputs complete orchestration specification to /project_specs/orchestration_specification.md
    """

    def __init__(self):
        """Initialize the Orchestration Specialist."""
        super().__init__(
            name="orchestration-specialist",
            description=(
                "Expert in workflow orchestration and agent coordination for multi-agent systems. "
                "Use this specialist to design workflow patterns, plan agent delegation, "
                "design result aggregation, create error handling strategies, define communication "
                "protocols, and design complex execution flows. "
                "Creates comprehensive orchestration specifications."
            ),
            prompt_file="orchestration_specialist_prompt.md",
            tools=[
                design_workflow_pattern,
                plan_agent_coordination,
                design_error_handling,
                plan_result_aggregation,
                design_execution_flow,
                plan_communication_protocol,
            ],
            model="claude-sonnet-4-5-20250929",
        )
