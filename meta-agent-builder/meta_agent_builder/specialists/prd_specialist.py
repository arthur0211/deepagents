"""PRD Specialist - Product Requirements Document expert."""

from meta_agent_builder.specialists.base import BaseSpecialist
from meta_agent_builder.tools import (
    analyze_requirements,
    create_success_metrics,
    create_user_persona,
    define_acceptance_criteria,
    estimate_complexity,
)


class PRDSpecialist(BaseSpecialist):
    """Specialist for creating Product Requirements Documents.

    This specialist creates comprehensive PRDs that include:
    - User personas and journeys
    - Functional and non-functional requirements
    - User stories with acceptance criteria
    - Success metrics and quality gates
    - Complexity estimates and timelines
    - Feature prioritization

    Outputs complete PRD to /project_specs/prd.md
    """

    def __init__(self):
        """Initialize the PRD Specialist."""
        super().__init__(
            name="prd-specialist",
            description=(
                "Expert in creating Product Requirements Documents (PRDs). "
                "Use this specialist to translate project descriptions into "
                "comprehensive requirements documents with user personas, user stories, "
                "acceptance criteria, success metrics, and feature specifications. "
                "Creates detailed, actionable PRDs that guide development."
            ),
            prompt_file="prd_specialist_prompt.md",
            tools=[
                analyze_requirements,
                create_user_persona,
                define_acceptance_criteria,
                estimate_complexity,
                create_success_metrics,
            ],
            model="claude-sonnet-4-5-20250929",
        )
