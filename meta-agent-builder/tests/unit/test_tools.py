"""Unit tests for custom tools."""

import pytest

from meta_agent_builder.tools import (
    # Documentation tools
    extract_code_examples,
    internet_search,
    summarize_documentation,
    # Architecture tools
    create_mermaid_diagram,
    suggest_middleware_stack,
    validate_agent_hierarchy,
    # PRD tools
    analyze_requirements,
    create_success_metrics,
    create_user_persona,
    define_acceptance_criteria,
    estimate_complexity,
    # Context tools
    define_state_transitions,
    design_context_compression,
    design_memory_strategy,
    design_prompt_strategy,
    plan_context_sharing,
    plan_context_structure,
    # Middleware tools
    configure_built_in_middleware,
    design_custom_middleware,
    design_middleware_interaction,
    plan_middleware_optimization,
    plan_middleware_stack,
    validate_middleware_stack,
    # Orchestration tools
    design_error_handling,
    design_execution_flow,
    design_workflow_pattern,
    plan_agent_coordination,
    plan_communication_protocol,
    plan_result_aggregation,
    # Implementation tools
    create_code_template,
    create_implementation_checklist,
    generate_documentation_outline,
    generate_file_structure,
    plan_dependencies,
    plan_implementation_phases,
    plan_testing_strategy,
)


class TestArchitectureTools:
    """Test architecture design tools."""

    def test_create_mermaid_diagram(self):
        """Test Mermaid diagram creation."""
        result = create_mermaid_diagram.invoke({
            "diagram_type": "sequence",
            "content": "A->>B: Message",
            "title": "Test Diagram"
        })
        assert isinstance(result, str)
        assert "```mermaid" in result
        assert "Test Diagram" in result

    def test_validate_agent_hierarchy(self):
        """Test agent hierarchy validation."""
        result = validate_agent_hierarchy.invoke({
            "hierarchy_spec": {
                "orchestrator": {"subagents": ["agent1", "agent2"]},
                "agent1": {"tools": ["tool1"]},
                "agent2": {"tools": ["tool2"]}
            }
        })
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], bool)
        assert isinstance(result[1], list)

    def test_suggest_middleware_stack(self):
        """Test middleware stack suggestions."""
        result = suggest_middleware_stack.invoke({
            "agent_type": "orchestrator",
            "requirements": ["planning", "memory", "delegation"]
        })
        assert isinstance(result, list)
        assert len(result) > 0


class TestPRDTools:
    """Test PRD creation tools."""

    def test_analyze_requirements(self):
        """Test requirements analysis."""
        result = analyze_requirements.invoke({
            "project_description": "Build a chatbot",
            "focus_area": "functional"
        })
        assert isinstance(result, dict)
        assert result["focus_area"] == "functional"
        assert result["analyzed"] is True

    def test_create_user_persona(self):
        """Test user persona creation."""
        result = create_user_persona.invoke({
            "persona_name": "Developer Dave",
            "role": "Software Engineer",
            "goals": ["Build efficiently", "Learn new tech"],
            "pain_points": ["Complex setup", "Poor docs"],
            "technical_level": "advanced"
        })
        assert isinstance(result, dict)
        assert result["name"] == "Developer Dave"
        assert result["created"] is True
        assert len(result["goals"]) == 2

    def test_define_acceptance_criteria(self):
        """Test acceptance criteria definition."""
        result = define_acceptance_criteria.invoke({
            "feature_name": "User Login",
            "criteria": ["User can login", "Session persists"],
            "priority": "must-have"
        })
        assert isinstance(result, dict)
        assert result["feature"] == "User Login"
        assert result["total_criteria"] == 2

    def test_estimate_complexity(self):
        """Test complexity estimation."""
        result = estimate_complexity.invoke({
            "feature_name": "Auth System",
            "technical_complexity": "high",
            "implementation_risk": "medium",
            "dependencies": ["OAuth", "Database"],
            "estimated_effort": "2 weeks"
        })
        assert isinstance(result, dict)
        assert result["complexity"] == "high"
        assert result["total_dependencies"] == 2


class TestContextTools:
    """Test context engineering tools."""

    def test_design_prompt_strategy(self):
        """Test prompt strategy design."""
        result = design_prompt_strategy.invoke({
            "agent_name": "TestAgent",
            "role_description": "Testing agent",
            "key_capabilities": ["test1", "test2"],
            "tone": "professional",
            "interaction_style": "collaborative"
        })
        assert isinstance(result, dict)
        assert result["agent"] == "TestAgent"
        assert result["total_capabilities"] == 2

    def test_plan_context_structure(self):
        """Test context structure planning."""
        result = plan_context_structure.invoke({
            "agent_name": "TestAgent",
            "state_items": [{"name": "task", "description": "Current task"}],
            "context_sources": ["user_input", "memory"],
            "update_frequency": "per-message"
        })
        assert isinstance(result, dict)
        assert result["total_sources"] == 2

    def test_design_memory_strategy(self):
        """Test memory strategy design."""
        result = design_memory_strategy.invoke({
            "scope": "persistent",
            "storage_path": "/memories/agent",
            "retention_policy": "Keep all",
            "access_pattern": "read-write"
        })
        assert isinstance(result, dict)
        assert result["scope"] == "persistent"


class TestMiddlewareTools:
    """Test middleware design tools."""

    def test_design_custom_middleware(self):
        """Test custom middleware design."""
        result = design_custom_middleware.invoke({
            "middleware_name": "TestMiddleware",
            "purpose": "Testing",
            "hook_points": ["pre_tool", "post_tool"],
            "configuration": {"option1": "value1"}
        })
        assert isinstance(result, dict)
        assert result["name"] == "TestMiddleware"
        assert result["total_hooks"] == 2

    def test_plan_middleware_stack(self):
        """Test middleware stack planning."""
        result = plan_middleware_stack.invoke({
            "agent_name": "TestAgent",
            "middleware_layers": [
                {"name": "Layer1", "purpose": "Purpose1"}
            ],
            "execution_order": "bottom-up"
        })
        assert isinstance(result, dict)
        assert result["total_layers"] == 1

    def test_configure_built_in_middleware(self):
        """Test built-in middleware configuration."""
        result = configure_built_in_middleware.invoke({
            "middleware_type": "TodoList",
            "configuration": {"enabled": "true"},
            "enabled": True
        })
        assert isinstance(result, dict)
        assert result["is_built_in"] is True


class TestOrchestrationTools:
    """Test orchestration design tools."""

    def test_design_workflow_pattern(self):
        """Test workflow pattern design."""
        result = design_workflow_pattern.invoke({
            "pattern_name": "sequential",
            "description": "Sequential execution",
            "agents_involved": ["Agent1", "Agent2"],
            "coordination_mechanism": "Message passing"
        })
        assert isinstance(result, dict)
        assert result["pattern"] == "sequential"
        assert result["total_agents"] == 2

    def test_plan_agent_coordination(self):
        """Test agent coordination planning."""
        result = plan_agent_coordination.invoke({
            "coordinator_agent": "Orchestrator",
            "specialist_agents": ["S1", "S2"],
            "delegation_strategy": "capability-based",
            "result_aggregation": "Synthesize"
        })
        assert isinstance(result, dict)
        assert result["total_specialists"] == 2

    def test_design_error_handling(self):
        """Test error handling design."""
        result = design_error_handling.invoke({
            "error_type": "tool-failure",
            "handling_strategy": "retry",
            "retry_config": {"max_attempts": "3"},
            "fallback_action": "Use default"
        })
        assert isinstance(result, dict)
        assert result["strategy"] == "retry"


class TestImplementationTools:
    """Test implementation planning tools."""

    def test_plan_implementation_phases(self):
        """Test implementation phase planning."""
        result = plan_implementation_phases.invoke({
            "project_name": "TestProject",
            "phases": [{"name": "Phase1", "description": "Desc", "duration": "1w"}],
            "total_estimated_time": "1 month"
        })
        assert isinstance(result, dict)
        assert result["project"] == "TestProject"
        assert result["total_phases"] == 1

    def test_generate_file_structure(self):
        """Test file structure generation."""
        result = generate_file_structure.invoke({
            "project_name": "TestProject",
            "directory_tree": {"src": ["main.py"], "tests": ["test.py"]},
            "package_manager": "pip"
        })
        assert isinstance(result, dict)
        assert result["total_directories"] == 2
        assert result["total_files"] == 2

    def test_create_code_template(self):
        """Test code template creation."""
        result = create_code_template.invoke({
            "template_type": "agent-class",
            "name": "TestAgent",
            "parameters": {"model": "claude-sonnet-4-5-20250929"}
        })
        assert isinstance(result, dict)
        assert result["type"] == "agent-class"
        assert result["ready"] is True

    def test_plan_dependencies(self):
        """Test dependency planning."""
        result = plan_dependencies.invoke({
            "core_dependencies": ["deepagents>=0.2.9"],
            "optional_dependencies": [{"package": "pytest", "purpose": "testing"}],
            "python_version": ">=3.10"
        })
        assert isinstance(result, dict)
        assert result["total_core"] == 1
        assert result["total_optional"] == 1


class TestToolAttributes:
    """Test that all tools have required attributes."""

    def test_all_tools_have_names(self):
        """Test that all tools have names."""
        tools = [
            internet_search, extract_code_examples, summarize_documentation,
            create_mermaid_diagram, validate_agent_hierarchy, suggest_middleware_stack,
            analyze_requirements, create_user_persona, define_acceptance_criteria,
            estimate_complexity, create_success_metrics,
            design_prompt_strategy, plan_context_structure, design_memory_strategy,
            define_state_transitions, design_context_compression, plan_context_sharing,
            design_custom_middleware, plan_middleware_stack, configure_built_in_middleware,
            design_middleware_interaction, plan_middleware_optimization, validate_middleware_stack,
            design_workflow_pattern, plan_agent_coordination, design_error_handling,
            plan_result_aggregation, design_execution_flow, plan_communication_protocol,
            plan_implementation_phases, generate_file_structure, create_code_template,
            plan_dependencies, create_implementation_checklist, plan_testing_strategy,
            generate_documentation_outline,
        ]

        for tool in tools:
            assert hasattr(tool, "name")
            assert hasattr(tool, "description")
            assert tool.name is not None
            assert tool.description is not None
