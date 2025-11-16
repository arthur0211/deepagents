"""Examples of using Meta-Agent Builder CLI.

This file demonstrates various CLI usage patterns.
Run these commands from the meta-agent-builder directory.
"""

# Example 1: Basic generation
"""
python -m meta_agent_builder generate "Create a chatbot with memory"
"""

# Example 2: Generate from file
"""
# First, create a description file
cat > project.txt << 'EOF'
Create a research agent system that:
- Searches multiple sources (web, papers, documentation)
- Analyzes and synthesizes findings
- Generates comprehensive reports with citations
- Maintains research history
EOF

# Then generate specs
python -m meta_agent_builder generate --file project.txt --verbose
"""

# Example 3: Check system status
"""
python -m meta_agent_builder status
"""

# Example 4: Using templates programmatically
"""
from meta_agent_builder.templates import TemplateManager

# List available templates
manager = TemplateManager()
templates = manager.list_templates()

print("Available templates:")
for template in templates:
    print(f"  - {template['id']}: {template['name']}")
    print(f"    Type: {template['project_type']}")
    print(f"    Complexity: {template['complexity']}")
    print()

# Load and use a template
research_template = manager.load_template("research_agent")
print(f"Template: {research_template['name']}")
print(f"Description: {research_template['description']}")

# Enhance user request with template
user_request = "Build a research assistant for academic papers"
enhanced = manager.enhance_user_request(user_request, "research_agent")
print(enhanced)
"""

# Example 5: Using custom middleware
"""
import asyncio
from meta_agent_builder.orchestrator import MetaOrchestrator
from meta_agent_builder.middleware import ValidationMiddleware, ProgressTrackingMiddleware

async def main():
    # Create orchestrator
    orchestrator = MetaOrchestrator()

    # Note: In future versions, you'll be able to add custom middleware like this:
    # orchestrator.add_middleware(ValidationMiddleware())
    # orchestrator.add_middleware(ProgressTrackingMiddleware())

    user_request = "Create an AI coding assistant"

    async for event in orchestrator.process_project_request(user_request):
        if "messages" in event:
            print(event["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
"""

# Example 6: Batch processing multiple projects
"""
import asyncio
from pathlib import Path
from meta_agent_builder.orchestrator import MetaOrchestrator

async def process_projects(project_descriptions: list[str]):
    orchestrator = MetaOrchestrator()

    for i, description in enumerate(project_descriptions, 1):
        print(f"\\n{'='*60}")
        print(f"Processing project {i}/{len(project_descriptions)}")
        print(f"{'='*60}\\n")

        thread_id = f"project-{i}"

        async for event in orchestrator.process_project_request(
            description,
            thread_id=thread_id
        ):
            if "messages" in event:
                # Process event
                pass

        # Get deliverables
        deliverables = orchestrator.get_deliverables(thread_id)
        print(f"\\nProject {i} complete:")
        for name, path in deliverables.items():
            print(f"  {name}: {path}")

projects = [
    "Create a chatbot for customer support",
    "Build a code review automation system",
    "Design a research paper summarization tool",
]

asyncio.run(process_projects(projects))
"""

print(__doc__)
