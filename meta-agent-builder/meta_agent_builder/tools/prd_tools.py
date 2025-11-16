"""PRD (Product Requirements Document) Tools."""

from typing import Literal

from langchain_core.tools import tool


@tool
def analyze_requirements(
    project_description: str,
    focus_area: Literal[
        "functional", "non-functional", "user-stories", "constraints", "success-metrics"
    ],
) -> dict:
    """Analyze and extract specific requirement types from project description.

    Args:
        project_description: The project description to analyze
        focus_area: Type of requirements to extract

    Returns:
        Dictionary with extracted requirements and insights
    """
    # This is a helper tool that structures the analysis
    # The actual analysis is done by the specialist
    return {
        "focus_area": focus_area,
        "analyzed": True,
        "description": project_description,
        "message": f"Ready to extract {focus_area} requirements. Please provide your analysis.",
    }


@tool
def create_user_persona(
    persona_name: str,
    role: str,
    goals: list[str],
    pain_points: list[str],
    technical_level: Literal["beginner", "intermediate", "advanced", "expert"],
) -> dict:
    """Create a structured user persona for the PRD.

    Args:
        persona_name: Name of the persona (e.g., "Data Scientist Dave")
        role: User's role or job title
        goals: List of user goals
        pain_points: List of user pain points
        technical_level: User's technical proficiency

    Returns:
        Structured persona dictionary
    """
    return {
        "name": persona_name,
        "role": role,
        "goals": goals,
        "pain_points": pain_points,
        "technical_level": technical_level,
        "created": True,
    }


@tool
def define_acceptance_criteria(
    feature_name: str,
    criteria: list[str],
    priority: Literal["must-have", "should-have", "nice-to-have"],
) -> dict:
    """Define acceptance criteria for a feature.

    Args:
        feature_name: Name of the feature
        criteria: List of acceptance criteria (Given-When-Then format recommended)
        priority: Priority level using MoSCoW method

    Returns:
        Structured acceptance criteria
    """
    return {
        "feature": feature_name,
        "criteria": criteria,
        "priority": priority,
        "total_criteria": len(criteria),
    }


@tool
def estimate_complexity(
    feature_name: str,
    technical_complexity: Literal["low", "medium", "high", "very-high"],
    implementation_risk: Literal["low", "medium", "high"],
    dependencies: list[str],
    estimated_effort: str,
) -> dict:
    """Estimate the complexity and effort for a feature.

    Args:
        feature_name: Name of the feature
        technical_complexity: Technical complexity level
        implementation_risk: Risk level for implementation
        dependencies: List of dependencies (external services, libraries, etc.)
        estimated_effort: Effort estimate (e.g., "2-3 days", "1 week")

    Returns:
        Complexity estimation summary
    """
    return {
        "feature": feature_name,
        "complexity": technical_complexity,
        "risk": implementation_risk,
        "dependencies": dependencies,
        "effort": estimated_effort,
        "total_dependencies": len(dependencies),
    }


@tool
def create_success_metrics(
    category: Literal[
        "performance", "quality", "usability", "business", "adoption"
    ],
    metrics: list[dict[str, str]],
) -> dict:
    """Define success metrics for the project.

    Args:
        category: Category of metrics
        metrics: List of metrics with name, target, and measurement method
                 Example: [{"name": "Response Time", "target": "< 2s", "method": "Load testing"}]

    Returns:
        Structured success metrics
    """
    return {
        "category": category,
        "metrics": metrics,
        "total_metrics": len(metrics),
    }
