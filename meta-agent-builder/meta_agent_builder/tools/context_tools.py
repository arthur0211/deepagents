"""Context Engineering Tools."""

from typing import Literal

from langchain_core.tools import tool


@tool
def design_prompt_strategy(
    agent_name: str,
    role_description: str,
    key_capabilities: list[str],
    tone: Literal["professional", "friendly", "technical", "educational", "concise"],
    interaction_style: Literal["directive", "collaborative", "advisory", "autonomous"],
) -> dict:
    """Design a prompt engineering strategy for an agent.

    Args:
        agent_name: Name of the agent
        role_description: Clear description of the agent's role
        key_capabilities: List of agent capabilities to emphasize
        tone: Desired communication tone
        interaction_style: How the agent should interact

    Returns:
        Prompt strategy structure
    """
    return {
        "agent": agent_name,
        "role": role_description,
        "capabilities": key_capabilities,
        "tone": tone,
        "style": interaction_style,
        "total_capabilities": len(key_capabilities),
    }


@tool
def plan_context_structure(
    agent_name: str,
    state_items: list[dict[str, str]],
    context_sources: list[str],
    update_frequency: Literal["per-message", "per-task", "on-demand", "persistent"],
) -> dict:
    """Plan the context structure for an agent.

    Args:
        agent_name: Name of the agent
        state_items: List of state items with name and description
                    Example: [{"name": "current_task", "description": "Active task being processed"}]
        context_sources: Sources of context (e.g., "user_input", "memory", "tools", "subagents")
        update_frequency: How often context should be updated

    Returns:
        Context structure plan
    """
    return {
        "agent": agent_name,
        "state_items": state_items,
        "sources": context_sources,
        "update_frequency": update_frequency,
        "total_state_items": len(state_items),
        "total_sources": len(context_sources),
    }


@tool
def design_memory_strategy(
    scope: Literal["agent-local", "shared", "persistent", "ephemeral"],
    storage_path: str,
    retention_policy: str,
    access_pattern: Literal["read-write", "read-only", "write-only", "append-only"],
) -> dict:
    """Design a memory storage strategy.

    Args:
        scope: Scope of memory storage
        storage_path: Virtual filesystem path for storage
        retention_policy: Description of retention policy (e.g., "Keep last 100 entries", "Persistent")
        access_pattern: How memory should be accessed

    Returns:
        Memory strategy specification
    """
    return {
        "scope": scope,
        "path": storage_path,
        "retention": retention_policy,
        "access": access_pattern,
    }


@tool
def define_state_transitions(
    agent_name: str,
    states: list[str],
    transitions: list[dict[str, str]],
    initial_state: str,
) -> dict:
    """Define state machine for agent workflow.

    Args:
        agent_name: Name of the agent
        states: List of possible states
        transitions: List of transitions with from, to, and trigger
                    Example: [{"from": "idle", "to": "processing", "trigger": "task_received"}]
        initial_state: Starting state

    Returns:
        State machine definition
    """
    return {
        "agent": agent_name,
        "states": states,
        "transitions": transitions,
        "initial_state": initial_state,
        "total_states": len(states),
        "total_transitions": len(transitions),
    }


@tool
def design_context_compression(
    compression_strategy: Literal[
        "summarization", "chunking", "pruning", "hierarchical", "hybrid"
    ],
    trigger_threshold: str,
    target_size: str,
    preservation_rules: list[str],
) -> dict:
    """Design context compression strategy to manage token limits.

    Args:
        compression_strategy: Method for compressing context
        trigger_threshold: When to trigger compression (e.g., "80% of limit", "10k tokens")
        target_size: Target size after compression (e.g., "50% of current", "5k tokens")
        preservation_rules: Rules for what to preserve (e.g., "Keep last 3 messages", "Preserve tool results")

    Returns:
        Compression strategy specification
    """
    return {
        "strategy": compression_strategy,
        "trigger": trigger_threshold,
        "target": target_size,
        "rules": preservation_rules,
        "total_rules": len(preservation_rules),
    }


@tool
def plan_context_sharing(
    sharing_mechanism: Literal[
        "shared-state", "store-based", "message-passing", "filesystem"
    ],
    shared_items: list[str],
    access_control: dict[str, list[str]],
) -> dict:
    """Plan how context is shared between agents.

    Args:
        sharing_mechanism: Method for sharing context
        shared_items: List of items to share
        access_control: Dictionary mapping items to list of agents with access
                       Example: {"research_data": ["agent1", "agent2"]}

    Returns:
        Context sharing plan
    """
    return {
        "mechanism": sharing_mechanism,
        "items": shared_items,
        "access_control": access_control,
        "total_shared_items": len(shared_items),
    }
