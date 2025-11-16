"""Middleware Specialist - Deep Agents middleware expert."""

from meta_agent_builder.specialists.base import BaseSpecialist
from meta_agent_builder.tools import (
    configure_built_in_middleware,
    design_custom_middleware,
    design_middleware_interaction,
    plan_middleware_optimization,
    plan_middleware_stack,
    validate_middleware_stack,
)


class MiddlewareSpecialist(BaseSpecialist):
    """Specialist for designing and configuring middleware stacks.

    This specialist designs:
    - Built-in middleware configuration
    - Custom middleware for project needs
    - Middleware stack ordering and optimization
    - Middleware interactions and coordination
    - Performance and cost optimizations

    Outputs complete middleware specification to /project_specs/middleware_specification.md
    """

    def __init__(self):
        """Initialize the Middleware Specialist."""
        super().__init__(
            name="middleware-specialist",
            description=(
                "Expert in Deep Agents middleware architecture. "
                "Use this specialist to configure built-in middleware "
                "(TodoList, Filesystem, SubAgent, Summarization, PromptCaching, AgentMemory), "
                "design custom middleware, optimize middleware stacks, and plan middleware "
                "interactions. Creates comprehensive middleware specifications."
            ),
            prompt_file="middleware_specialist_prompt.md",
            tools=[
                design_custom_middleware,
                plan_middleware_stack,
                configure_built_in_middleware,
                design_middleware_interaction,
                plan_middleware_optimization,
                validate_middleware_stack,
            ],
            model="claude-sonnet-4-5-20250929",
        )
