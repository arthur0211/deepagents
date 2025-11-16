"""Unit tests for specialist classes."""

import pytest

from meta_agent_builder.specialists import (
    ArchitectureSpecialist,
    ContextSpecialist,
    DocumentationSpecialist,
    ImplementationSpecialist,
    MiddlewareSpecialist,
    OrchestrationSpecialist,
    PRDSpecialist,
)


class TestSpecialistInitialization:
    """Test that all specialists initialize correctly."""

    def test_documentation_specialist_init(self):
        """Test DocumentationSpecialist initialization."""
        specialist = DocumentationSpecialist()
        assert specialist.name == "documentation-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 3
        assert specialist.system_prompt is not None

    def test_architecture_specialist_init(self):
        """Test ArchitectureSpecialist initialization."""
        specialist = ArchitectureSpecialist()
        assert specialist.name == "architecture-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 3
        assert specialist.system_prompt is not None

    def test_prd_specialist_init(self):
        """Test PRDSpecialist initialization."""
        specialist = PRDSpecialist()
        assert specialist.name == "prd-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 5
        assert specialist.system_prompt is not None

    def test_context_specialist_init(self):
        """Test ContextSpecialist initialization."""
        specialist = ContextSpecialist()
        assert specialist.name == "context-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 6
        assert specialist.system_prompt is not None

    def test_middleware_specialist_init(self):
        """Test MiddlewareSpecialist initialization."""
        specialist = MiddlewareSpecialist()
        assert specialist.name == "middleware-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 6
        assert specialist.system_prompt is not None

    def test_orchestration_specialist_init(self):
        """Test OrchestrationSpecialist initialization."""
        specialist = OrchestrationSpecialist()
        assert specialist.name == "orchestration-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 6
        assert specialist.system_prompt is not None

    def test_implementation_specialist_init(self):
        """Test ImplementationSpecialist initialization."""
        specialist = ImplementationSpecialist()
        assert specialist.name == "implementation-specialist"
        assert specialist.model == "claude-sonnet-4-5-20250929"
        assert len(specialist.tools) == 7
        assert specialist.system_prompt is not None


class TestSubAgentConfig:
    """Test SubAgent configuration generation."""

    def test_documentation_specialist_config(self):
        """Test DocumentationSpecialist SubAgent config."""
        specialist = DocumentationSpecialist()
        config = specialist.to_subagent_config()

        assert config["name"] == "documentation-specialist"
        assert "description" in config
        assert "system_prompt" in config
        assert "tools" in config
        assert config["model"] == "claude-sonnet-4-5-20250929"
        assert len(config["tools"]) == 3

    def test_all_specialists_have_valid_configs(self):
        """Test that all specialists generate valid SubAgent configs."""
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
            assert isinstance(config["tools"], list)
            assert len(config["tools"]) > 0


class TestToolCounts:
    """Test that specialists have the correct number of tools."""

    def test_total_tools_count(self):
        """Test total number of tools across all specialists."""
        specialists = [
            DocumentationSpecialist(),  # 3 tools
            ArchitectureSpecialist(),  # 3 tools
            PRDSpecialist(),  # 5 tools
            ContextSpecialist(),  # 6 tools
            MiddlewareSpecialist(),  # 6 tools
            OrchestrationSpecialist(),  # 6 tools
            ImplementationSpecialist(),  # 7 tools
        ]

        total_tools = sum(len(s.tools) for s in specialists)
        assert total_tools == 36  # Total expected tools

    def test_no_duplicate_tool_names(self):
        """Test that there are no duplicate tool names within a specialist."""
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
            tool_names = [tool.name for tool in specialist.tools]
            assert len(tool_names) == len(set(tool_names)), (
                f"{specialist.name} has duplicate tool names"
            )
