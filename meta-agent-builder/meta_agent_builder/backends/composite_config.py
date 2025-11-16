"""Backend configuration for Meta-Agent Builder.

This module provides the CompositeBackend configuration with routing
for different storage zones (memories, docs, templates, etc.).
"""

from typing import Callable, Optional

from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
from deepagents.backends.protocol import BackendProtocol
from langgraph.store.base import BaseStore

# Type alias for backend factory
BackendFactory = Callable[[any], BackendProtocol]


def create_meta_agent_backend(store: Optional[BaseStore] = None) -> BackendFactory:
    """Create the composite backend factory for Meta-Agent Builder.

    This backend routes different path prefixes to appropriate storage backends:
    - /memories/ -> StoreBackend (persistent knowledge base)
    - /docs/ -> StoreBackend (cached documentation)
    - /templates/ -> StoreBackend (reusable project templates)
    - /project_specs/ -> StateBackend (current project outputs)
    - /validation/ -> StateBackend (validation artifacts)
    - default -> StateBackend (temporary scratch space)

    Args:
        store: Optional LangGraph BaseStore instance for persistent storage.
               If None, falls back to StateBackend for all routes.

    Returns:
        BackendFactory that creates CompositeBackend with appropriate routing.

    Example:
        >>> from langgraph.store.memory import InMemoryStore
        >>> store = InMemoryStore()
        >>> backend_factory = create_meta_agent_backend(store)
        >>> # Now use backend_factory with create_deep_agent
    """

    def backend_factory(runtime) -> CompositeBackend:
        """Create backend with runtime context."""
        # Determine backends based on store availability
        if store is not None:
            memory_backend = StoreBackend(runtime)
            docs_backend = StoreBackend(runtime)
            templates_backend = StoreBackend(runtime)
        else:
            # Fallback to ephemeral storage if no store provided
            memory_backend = StateBackend(runtime)
            docs_backend = StateBackend(runtime)
            templates_backend = StateBackend(runtime)

        return CompositeBackend(
            default=StateBackend(runtime),  # Ephemeral default for scratch space
            routes={
                # Persistent knowledge base (agent learnings)
                "/memories/": memory_backend,
                # Cached documentation
                "/docs/": docs_backend,
                # Reusable project templates
                "/templates/": templates_backend,
                # Current project specifications (ephemeral)
                "/project_specs/": StateBackend(runtime),
                # Validation artifacts (ephemeral)
                "/validation/": StateBackend(runtime),
            },
        )

    return backend_factory


def create_backend_with_sandbox(
    store: Optional[BaseStore] = None,
    sandbox_backend=None,
) -> BackendFactory:
    """Create backend factory with optional sandbox for code execution.

    Args:
        store: Optional persistent store
        sandbox_backend: Optional SandboxBackend instance for code execution

    Returns:
        BackendFactory that creates CompositeBackend with sandbox as default if provided

    Example:
        >>> from deepagents.backends.sandbox import SandboxBackend
        >>> sandbox = SandboxBackend()  # Your sandbox implementation
        >>> backend_factory = create_backend_with_sandbox(store, sandbox)
    """

    def backend_factory(runtime) -> CompositeBackend:
        """Create backend with runtime context."""
        # Determine storage backends
        if store is not None:
            memory_backend = StoreBackend(runtime)
            docs_backend = StoreBackend(runtime)
            templates_backend = StoreBackend(runtime)
        else:
            memory_backend = StateBackend(runtime)
            docs_backend = StateBackend(runtime)
            templates_backend = StateBackend(runtime)

        # Use sandbox as default if provided, otherwise StateBackend
        default_backend = sandbox_backend if sandbox_backend is not None else StateBackend(runtime)

        return CompositeBackend(
            default=default_backend,
            routes={
                "/memories/": memory_backend,
                "/docs/": docs_backend,
                "/templates/": templates_backend,
                "/project_specs/": StateBackend(runtime),
                "/validation/": StateBackend(runtime),
            },
        )

    return backend_factory
