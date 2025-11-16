"""Implementation Specialist - Code generation and project setup expert."""

from meta_agent_builder.specialists.base import BaseSpecialist
from meta_agent_builder.tools import (
    create_code_template,
    create_implementation_checklist,
    generate_documentation_outline,
    generate_file_structure,
    plan_dependencies,
    plan_implementation_phases,
    plan_testing_strategy,
)


class ImplementationSpecialist(BaseSpecialist):
    """Specialist for code generation and implementation planning.

    This specialist creates:
    - Implementation phase plans
    - Project scaffolding and structure
    - Code templates for all components
    - Dependency specifications
    - Testing strategies
    - Documentation outlines
    - Step-by-step implementation guides

    Outputs complete implementation guide to /project_specs/implementation_guide.md
    """

    def __init__(self):
        """Initialize the Implementation Specialist."""
        super().__init__(
            name="implementation-specialist",
            description=(
                "Expert in translating specifications into working code and implementation plans. "
                "Use this specialist to create implementation phases, generate project structure, "
                "create code templates, plan dependencies, design testing strategies, and generate "
                "comprehensive implementation guides that engineering teams can follow. "
                "Creates complete, practical implementation documentation."
            ),
            prompt_file="implementation_specialist_prompt.md",
            tools=[
                plan_implementation_phases,
                generate_file_structure,
                create_code_template,
                plan_dependencies,
                create_implementation_checklist,
                plan_testing_strategy,
                generate_documentation_outline,
            ],
            model="claude-sonnet-4-5-20250929",
        )
