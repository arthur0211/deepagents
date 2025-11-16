"""Middleware Design Tools."""

from typing import Literal

from langchain_core.tools import tool


@tool
def design_custom_middleware(
    middleware_name: str,
    purpose: str,
    hook_points: list[str],
    configuration: dict[str, str],
) -> dict:
    """Design a custom middleware component.

    Args:
        middleware_name: Name of the middleware (e.g., "ValidationMiddleware")
        purpose: Clear description of what the middleware does
        hook_points: Where middleware hooks into execution (e.g., ["pre_tool", "post_tool"])
        configuration: Configuration options with descriptions

    Returns:
        Middleware design specification
    """
    return {
        "name": middleware_name,
        "purpose": purpose,
        "hooks": hook_points,
        "config": configuration,
        "total_hooks": len(hook_points),
        "total_config_options": len(configuration),
    }


@tool
def plan_middleware_stack(
    agent_name: str,
    middleware_layers: list[dict[str, str]],
    execution_order: Literal["bottom-up", "top-down", "custom"],
) -> dict:
    """Plan the middleware stack for an agent.

    Args:
        agent_name: Name of the agent
        middleware_layers: List of middleware with name and purpose
                          Example: [{"name": "TodoListMiddleware", "purpose": "Task planning"}]
        execution_order: Order of middleware execution

    Returns:
        Middleware stack specification
    """
    return {
        "agent": agent_name,
        "layers": middleware_layers,
        "order": execution_order,
        "total_layers": len(middleware_layers),
    }


@tool
def configure_built_in_middleware(
    middleware_type: Literal[
        "TodoList",
        "Filesystem",
        "SubAgent",
        "Summarization",
        "PromptCaching",
        "AgentMemory",
    ],
    configuration: dict[str, str],
    enabled: bool = True,
) -> dict:
    """Configure a built-in Deep Agents middleware.

    Args:
        middleware_type: Type of middleware to configure
        configuration: Configuration options
        enabled: Whether middleware is enabled

    Returns:
        Middleware configuration
    """
    return {
        "type": middleware_type,
        "config": configuration,
        "enabled": enabled,
        "is_built_in": True,
    }


@tool
def design_middleware_interaction(
    middleware_a: str,
    middleware_b: str,
    interaction_type: Literal[
        "sequential", "parallel", "conditional", "isolated"
    ],
    coordination_mechanism: str,
) -> dict:
    """Design how two middleware components interact.

    Args:
        middleware_a: First middleware name
        middleware_b: Second middleware name
        interaction_type: How they interact
        coordination_mechanism: Description of coordination (e.g., "Shared state via backend")

    Returns:
        Interaction specification
    """
    return {
        "middleware_a": middleware_a,
        "middleware_b": middleware_b,
        "interaction": interaction_type,
        "coordination": coordination_mechanism,
    }


@tool
def plan_middleware_optimization(
    optimization_type: Literal[
        "performance", "cost", "reliability", "observability"
    ],
    strategies: list[str],
    expected_impact: str,
) -> dict:
    """Plan middleware optimizations.

    Args:
        optimization_type: Type of optimization to apply
        strategies: List of optimization strategies
        expected_impact: Description of expected improvement

    Returns:
        Optimization plan
    """
    return {
        "type": optimization_type,
        "strategies": strategies,
        "impact": expected_impact,
        "total_strategies": len(strategies),
    }


@tool
def validate_middleware_stack(
    middleware_stack: list[str],
    validation_criteria: list[str],
) -> dict:
    """Validate that a middleware stack meets requirements.

    Args:
        middleware_stack: List of middleware names in order
        validation_criteria: Requirements to check (e.g., "Has task planning", "Has memory")

    Returns:
        Validation result
    """
    return {
        "stack": middleware_stack,
        "criteria": validation_criteria,
        "stack_size": len(middleware_stack),
        "criteria_count": len(validation_criteria),
        "validated": True,
    }
