"""Template manager for common project patterns."""

import yaml
from pathlib import Path
from typing import Optional


class TemplateManager:
    """Manages project templates for common patterns."""

    def __init__(self, template_dir: Optional[Path] = None):
        """Initialize template manager.

        Args:
            template_dir: Directory containing template files.
                         Defaults to built-in templates.
        """
        if template_dir is None:
            template_dir = Path(__file__).parent
        self.template_dir = Path(template_dir)

    def list_templates(self) -> list[dict[str, str]]:
        """List all available templates.

        Returns:
            List of template metadata dictionaries
        """
        templates = []

        for template_file in self.template_dir.glob("*.yaml"):
            if template_file.name == "template_manager.py":
                continue

            try:
                template = self.load_template(template_file.stem)
                templates.append({
                    "id": template_file.stem,
                    "name": template.get("name", template_file.stem),
                    "description": template.get("description", "No description"),
                    "complexity": template.get("complexity", "unknown"),
                    "project_type": template.get("project_type", "general"),
                })
            except Exception as e:
                # Skip invalid templates
                continue

        return sorted(templates, key=lambda x: x["name"])

    def load_template(self, template_id: str) -> dict:
        """Load a template by ID.

        Args:
            template_id: Template identifier (filename without .yaml)

        Returns:
            Template dictionary

        Raises:
            FileNotFoundError: If template doesn't exist
            yaml.YAMLError: If template is invalid
        """
        template_path = self.template_dir / f"{template_id}.yaml"

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_id}")

        with open(template_path) as f:
            template = yaml.safe_load(f)

        return template

    def get_template_description(self, template_id: str) -> str:
        """Get detailed template description for prompting.

        Args:
            template_id: Template identifier

        Returns:
            Formatted description for use in prompts
        """
        template = self.load_template(template_id)

        description = f"""# {template.get('name', template_id)}

**Description**: {template.get('description', 'No description')}
**Type**: {template.get('project_type', 'general')}
**Complexity**: {template.get('complexity', 'unknown')}

## Agents

"""

        # Add agents
        for agent in template.get("agents", []):
            description += f"### {agent['name']}\n"
            description += f"- **Type**: {agent['type']}\n"
            description += f"- **Description**: {agent['description']}\n"
            description += f"- **Capabilities**: {', '.join(agent.get('capabilities', []))}\n"
            if "tools" in agent:
                description += f"- **Tools**: {', '.join(agent['tools'])}\n"
            description += "\n"

        # Add architecture
        if "architecture" in template:
            arch = template["architecture"]
            description += f"""## Architecture

- **Pattern**: {arch.get('pattern', 'unknown')}
- **Coordination**: {arch.get('coordination', 'unknown')}

"""

        # Add features
        if "features" in template:
            description += "## Features\n\n"
            for feature in template["features"]:
                description += f"- {feature}\n"
            description += "\n"

        # Add use cases
        if "use_cases" in template:
            description += "## Use Cases\n\n"
            for use_case in template["use_cases"]:
                description += f"- {use_case}\n"
            description += "\n"

        # Add complexity estimate
        if "estimated_complexity" in template:
            est = template["estimated_complexity"]
            description += f"""## Estimated Complexity

- **Development Time**: {est.get('development_time', 'unknown')}
- **Lines of Code**: {est.get('lines_of_code', 'unknown')}
- **Specialists**: {est.get('specialist_count', 'unknown')}
- **Tools**: {est.get('tool_count', 'unknown')}
"""

        return description

    def enhance_user_request(self, user_request: str, template_id: str) -> str:
        """Enhance user request with template context.

        Args:
            user_request: Original user request
            template_id: Template to use

        Returns:
            Enhanced request with template context
        """
        template_desc = self.get_template_description(template_id)

        enhanced_request = f"""# Project Request

{user_request}

---

# Reference Template

{template_desc}

---

**Instructions**: Use the reference template as a starting point, but customize based on the specific requirements in the project request above. The template provides a proven pattern, but adapt it to the user's needs.
"""

        return enhanced_request

    def save_template(self, template_id: str, template_data: dict):
        """Save a new template.

        Args:
            template_id: Template identifier
            template_data: Template dictionary to save
        """
        template_path = self.template_dir / f"{template_id}.yaml"

        with open(template_path, "w") as f:
            yaml.safe_dump(template_data, f, default_flow_style=False, sort_keys=False)

    def get_template_for_project_type(self, project_type: str) -> Optional[str]:
        """Get recommended template for a project type.

        Args:
            project_type: Type of project (e.g., "research_assistant", "chatbot")

        Returns:
            Template ID or None if no match
        """
        templates = self.list_templates()

        # Exact match
        for template in templates:
            if template["project_type"] == project_type:
                return template["id"]

        # Fuzzy match
        project_type_lower = project_type.lower()
        for template in templates:
            if project_type_lower in template["project_type"].lower():
                return template["id"]
            if project_type_lower in template["name"].lower():
                return template["id"]

        return None
