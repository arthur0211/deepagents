"""Integration tests for MetaOrchestrator."""

import pytest

from meta_agent_builder.backends import create_meta_agent_backend
from meta_agent_builder.specialists import (
    ArchitectureSpecialist,
    ContextSpecialist,
    DocumentationSpecialist,
    ImplementationSpecialist,
    MiddlewareSpecialist,
    OrchestrationSpecialist,
    PRDSpecialist,
)


class TestBackendConfiguration:
    """Test backend configuration."""

    def test_backend_factory_creation(self):
        """Test that backend factory is created correctly."""
        backend_factory = create_meta_agent_backend()
        assert callable(backend_factory)

    def test_backend_factory_with_store(self):
        """Test that backend factory works with store."""
        from langgraph.store.memory import InMemoryStore

        store = InMemoryStore()
        backend_factory = create_meta_agent_backend(store)
        assert callable(backend_factory)


class TestSpecialistCounts:
    """Test specialist counts and configurations."""

    def test_correct_number_of_specialists(self):
        """Test that all 7 specialist classes exist."""
        specialists = [
            DocumentationSpecialist(),
            ArchitectureSpecialist(),
            PRDSpecialist(),
            ContextSpecialist(),
            MiddlewareSpecialist(),
            OrchestrationSpecialist(),
            ImplementationSpecialist(),
        ]
        assert len(specialists) == 7

    def test_specialist_tool_counts(self):
        """Test that specialists have expected tool counts."""
        specialists = {
            "documentation-specialist": DocumentationSpecialist(),
            "architecture-specialist": ArchitectureSpecialist(),
            "prd-specialist": PRDSpecialist(),
            "context-specialist": ContextSpecialist(),
            "middleware-specialist": MiddlewareSpecialist(),
            "orchestration-specialist": OrchestrationSpecialist(),
            "implementation-specialist": ImplementationSpecialist(),
        }

        expected_tool_counts = {
            "documentation-specialist": 3,
            "architecture-specialist": 3,
            "prd-specialist": 5,
            "context-specialist": 6,
            "middleware-specialist": 6,
            "orchestration-specialist": 6,
            "implementation-specialist": 7,
        }

        for name, specialist in specialists.items():
            expected_count = expected_tool_counts[name]
            assert len(specialist.tools) == expected_count, (
                f"{name} should have {expected_count} tools, "
                f"but has {len(specialist.tools)}"
            )


class TestSubAgentConfiguration:
    """Test SubAgent configuration generation."""

    def test_all_specialists_generate_configs(self):
        """Test that all specialists can generate SubAgent configs."""
        specialists = [
            DocumentationSpecialist(),
            ArchitectureSpecialist(),
            PRDSpecialist(),
            ContextSpecialist(),
            MiddlewareSpecialist(),
            OrchestrationSpecialist(),
            ImplementationSpecialist(),
        ]

        for specialist in specialists:
            config = specialist.to_subagent_config()

            assert "name" in config
            assert "description" in config
            assert "system_prompt" in config
            assert "tools" in config
            assert "model" in config

            assert config["name"] == specialist.name
            assert len(config["tools"]) == len(specialist.tools)
            assert config["model"] == "claude-sonnet-4-5-20250929"


class TestDeliverables:
    """Test deliverables structure."""

    def test_deliverables_structure(self):
        """Test that deliverables structure is correct."""
        # Import here to avoid instantiating orchestrator
        from meta_agent_builder.orchestrator import MetaOrchestrator

        # Create a mock instance just to test get_deliverables method
        # We won't make API calls
        class MockOrchestrator(MetaOrchestrator):
            def __init__(self):
                # Don't call super().__init__() to avoid creating agent
                pass

        mock_orch = MockOrchestrator()
        deliverables = mock_orch.get_deliverables("test-thread")

        expected_deliverables = [
            "project_brief",
            "executive_summary",
            "architecture",
            "agents_hierarchy",
            "data_flows",
            "backend_strategy",
            "prd",
            "context_engineering",
            "middleware_specification",
            "orchestration_specification",
            "implementation_guide",
        ]

        assert len(deliverables) == len(expected_deliverables)
        for key in expected_deliverables:
            assert key in deliverables
            assert deliverables[key].startswith("/project_specs/")
