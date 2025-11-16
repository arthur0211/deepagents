"""Example of using project templates with Meta-Agent Builder."""

import asyncio

from meta_agent_builder.orchestrator import MetaOrchestrator
from meta_agent_builder.templates import TemplateManager


async def main():
    """Demonstrate template usage."""

    print("🎯 META-AGENT BUILDER - Template Usage Example\n")
    print("=" * 70)

    # Initialize template manager
    template_manager = TemplateManager()

    # List available templates
    print("\n📚 Available Templates:\n")
    templates = template_manager.list_templates()

    for i, template in enumerate(templates, 1):
        print(f"{i}. {template['name']}")
        print(f"   ID: {template['id']}")
        print(f"   Type: {template['project_type']}")
        print(f"   Complexity: {template['complexity']}")
        print(f"   Description: {template['description']}")
        print()

    # Example 1: Use research agent template
    print("\n" + "=" * 70)
    print("Example 1: Using Research Agent Template")
    print("=" * 70 + "\n")

    user_request = """
    I need a research agent that can:
    - Search academic papers using APIs
    - Extract key findings and methodologies
    - Compare multiple papers
    - Generate literature review summaries
    """

    # Enhance request with template
    enhanced_request = template_manager.enhance_user_request(
        user_request,
        "research_agent"
    )

    print("Enhanced Request (first 500 chars):")
    print(enhanced_request[:500])
    print("...\n")

    # Generate specs (commented out to avoid API calls in example)
    # orchestrator = MetaOrchestrator()
    # async for event in orchestrator.process_project_request(enhanced_request):
    #     if "messages" in event:
    #         print(event["messages"][-1].content)

    # Example 2: Automatically detect template
    print("\n" + "=" * 70)
    print("Example 2: Automatic Template Detection")
    print("=" * 70 + "\n")

    # Request mentions "chatbot" - should match chatbot template
    auto_request = "Create a customer support chatbot with memory"

    # Try to find matching template
    detected_template = template_manager.get_template_for_project_type("chatbot")

    if detected_template:
        print(f"✅ Detected template: {detected_template}")
        template_desc = template_manager.get_template_description(detected_template)
        print(f"\nTemplate Details:\n{template_desc[:300]}...")
    else:
        print("❌ No matching template found")

    # Example 3: Load and inspect template details
    print("\n" + "=" * 70)
    print("Example 3: Inspecting Template Details")
    print("=" * 70 + "\n")

    code_template = template_manager.load_template("code_assistant")

    print(f"Template Name: {code_template['name']}")
    print(f"Complexity: {code_template['complexity']}")
    print(f"\nAgents ({len(code_template['agents'])}):")

    for agent in code_template["agents"]:
        print(f"\n  • {agent['name']} ({agent['type']})")
        print(f"    {agent['description']}")
        print(f"    Capabilities: {', '.join(agent['capabilities'][:3])}...")

    print(f"\nFeatures ({len(code_template['features'])}):")
    for feature in code_template["features"][:5]:
        print(f"  • {feature}")

    if len(code_template["features"]) > 5:
        print(f"  ... and {len(code_template['features']) - 5} more")

    # Example 4: Create custom template
    print("\n" + "=" * 70)
    print("Example 4: Creating Custom Template")
    print("=" * 70 + "\n")

    custom_template = {
        "name": "my-custom-agent",
        "description": "Custom agent for my specific use case",
        "project_type": "custom",
        "complexity": "medium",
        "agents": [
            {
                "name": "custom-orchestrator",
                "type": "orchestrator",
                "description": "Main coordinator",
                "capabilities": ["planning", "coordination"],
                "middleware": ["TodoListMiddleware", "FilesystemMiddleware"]
            }
        ],
        "architecture": {
            "pattern": "single-agent",
            "coordination": "direct"
        },
        "features": [
            "Feature 1",
            "Feature 2",
            "Feature 3"
        ]
    }

    # Save custom template (commented out to not modify filesystem in example)
    # template_manager.save_template("my_custom", custom_template)
    print("✅ Custom template created (example only, not saved)")
    print(f"   Name: {custom_template['name']}")
    print(f"   Agents: {len(custom_template['agents'])}")
    print(f"   Features: {len(custom_template['features'])}")

    print("\n" + "=" * 70)
    print("✅ Template Usage Examples Complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
