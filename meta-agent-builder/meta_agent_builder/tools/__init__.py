"""Custom tools for Meta-Agent Builder specialists."""

from meta_agent_builder.tools.architecture_tools import (
    create_mermaid_diagram,
    suggest_middleware_stack,
    validate_agent_hierarchy,
)
from meta_agent_builder.tools.documentation_tools import (
    extract_code_examples,
    internet_search,
    summarize_documentation,
)
from meta_agent_builder.tools.implementation_tools import (
    create_code_template,
    create_implementation_checklist,
    generate_documentation_outline,
    generate_file_structure,
    plan_dependencies,
    plan_implementation_phases,
    plan_testing_strategy,
)
from meta_agent_builder.tools.context_tools import (
    define_state_transitions,
    design_context_compression,
    design_memory_strategy,
    design_prompt_strategy,
    plan_context_sharing,
    plan_context_structure,
)
from meta_agent_builder.tools.middleware_tools import (
    configure_built_in_middleware,
    design_custom_middleware,
    design_middleware_interaction,
    plan_middleware_optimization,
    plan_middleware_stack,
    validate_middleware_stack,
)
from meta_agent_builder.tools.orchestration_tools import (
    design_error_handling,
    design_execution_flow,
    design_workflow_pattern,
    plan_agent_coordination,
    plan_communication_protocol,
    plan_result_aggregation,
)
from meta_agent_builder.tools.prd_tools import (
    analyze_requirements,
    create_success_metrics,
    create_user_persona,
    define_acceptance_criteria,
    estimate_complexity,
)

__all__ = [
    # Documentation tools
    "internet_search",
    "extract_code_examples",
    "summarize_documentation",
    # Architecture tools
    "create_mermaid_diagram",
    "validate_agent_hierarchy",
    "suggest_middleware_stack",
    # PRD tools
    "analyze_requirements",
    "create_user_persona",
    "define_acceptance_criteria",
    "estimate_complexity",
    "create_success_metrics",
    # Context engineering tools
    "design_prompt_strategy",
    "plan_context_structure",
    "design_memory_strategy",
    "define_state_transitions",
    "design_context_compression",
    "plan_context_sharing",
    # Middleware tools
    "design_custom_middleware",
    "plan_middleware_stack",
    "configure_built_in_middleware",
    "design_middleware_interaction",
    "plan_middleware_optimization",
    "validate_middleware_stack",
    # Orchestration tools
    "design_workflow_pattern",
    "plan_agent_coordination",
    "design_error_handling",
    "plan_result_aggregation",
    "design_execution_flow",
    "plan_communication_protocol",
    # Implementation tools
    "plan_implementation_phases",
    "generate_file_structure",
    "create_code_template",
    "plan_dependencies",
    "create_implementation_checklist",
    "plan_testing_strategy",
    "generate_documentation_outline",
]
