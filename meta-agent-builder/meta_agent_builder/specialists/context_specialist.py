"""Context Engineering Specialist - Prompt and context design expert."""

from meta_agent_builder.specialists.base import BaseSpecialist
from meta_agent_builder.tools import (
    define_state_transitions,
    design_context_compression,
    design_memory_strategy,
    design_prompt_strategy,
    plan_context_sharing,
    plan_context_structure,
)


class ContextSpecialist(BaseSpecialist):
    """Specialist for context engineering and prompt design.

    This specialist designs:
    - System prompts for all agents
    - Context management strategies
    - Memory storage and retention policies
    - State machines and transitions
    - Context compression approaches
    - Cross-agent context sharing

    Outputs complete context engineering spec to /project_specs/context_engineering.md
    """

    def __init__(self):
        """Initialize the Context Engineering Specialist."""
        super().__init__(
            name="context-specialist",
            description=(
                "Expert in prompt engineering and context management for multi-agent systems. "
                "Use this specialist to design system prompts, plan context structures, "
                "design memory strategies, define state machines, plan context compression, "
                "and establish cross-agent communication patterns. "
                "Creates comprehensive context engineering specifications."
            ),
            prompt_file="context_specialist_prompt.md",
            tools=[
                design_prompt_strategy,
                plan_context_structure,
                design_memory_strategy,
                define_state_transitions,
                design_context_compression,
                plan_context_sharing,
            ],
            model="claude-sonnet-4-5-20250929",
        )
