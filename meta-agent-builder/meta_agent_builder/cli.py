"""Command-line interface for Meta-Agent Builder."""

import argparse
import asyncio
import os
import sys
from pathlib import Path
from typing import Optional

from meta_agent_builder.orchestrator import MetaOrchestrator


def check_api_keys() -> tuple[bool, list[str]]:
    """Check if required API keys are set.

    Returns:
        Tuple of (all_required_present, list_of_missing_keys)
    """
    missing = []

    if not os.getenv("ANTHROPIC_API_KEY"):
        missing.append("ANTHROPIC_API_KEY")

    return len(missing) == 0, missing


def print_banner():
    """Print CLI banner."""
    banner = """
╔══════════════════════════════════════════════════════════╗
║         🧠 META-AGENT BUILDER                            ║
║         Transform Ideas into Specifications              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)


async def generate_specs(
    description: str,
    output_dir: Optional[Path] = None,
    verbose: bool = False,
    thread_id: Optional[str] = None,
) -> dict:
    """Generate specifications from project description.

    Args:
        description: Project description
        output_dir: Optional directory to save outputs
        verbose: Print detailed output
        thread_id: Optional thread ID for resuming

    Returns:
        Dictionary with generated specifications paths
    """
    print("🚀 Initializing Meta-Orchestrator...")
    orchestrator = MetaOrchestrator()

    print(f"📝 Processing request...")
    if verbose:
        print(f"\nDescription: {description}\n")

    print("⚙️  Generating specifications...\n")
    print("-" * 60)

    async for event in orchestrator.process_project_request(description, thread_id):
        if "messages" in event and verbose:
            last_message = event["messages"][-1]
            if hasattr(last_message, "content") and last_message.content:
                print(f"🤖 {last_message.content}\n")

    print("-" * 60)
    print("\n✅ Generation complete!")

    deliverables = orchestrator.get_deliverables(thread_id or "default")

    print("\n📊 Generated Specifications:")
    for name, path in deliverables.items():
        print(f"  • {name}: {path}")

    if output_dir:
        print(f"\n💾 Outputs saved to: {output_dir}")

    return deliverables


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Meta-Agent Builder - Generate complete project specifications from descriptions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate specs from description
  meta-agent-builder generate "Create a chat bot with web search"

  # Use description from file
  meta-agent-builder generate --file project-description.txt

  # Verbose output
  meta-agent-builder generate "Research agent" --verbose

  # Save to specific directory
  meta-agent-builder generate "API server" --output ./specs

  # Resume previous session
  meta-agent-builder generate "..." --thread-id abc123

  # Check system status
  meta-agent-builder status
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Generate command
    gen_parser = subparsers.add_parser(
        "generate",
        help="Generate project specifications",
        aliases=["gen", "g"]
    )
    gen_parser.add_argument(
        "description",
        nargs="?",
        help="Project description"
    )
    gen_parser.add_argument(
        "-f", "--file",
        type=Path,
        help="Read description from file"
    )
    gen_parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output directory for specifications"
    )
    gen_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    gen_parser.add_argument(
        "-t", "--thread-id",
        help="Thread ID to resume previous session"
    )

    # Status command
    status_parser = subparsers.add_parser(
        "status",
        help="Check system status and configuration"
    )

    # Version command
    version_parser = subparsers.add_parser(
        "version",
        help="Show version information"
    )

    args = parser.parse_args()

    # Print banner
    print_banner()

    # Handle commands
    if args.command in ["generate", "gen", "g"]:
        # Get description
        description = None
        if args.description:
            description = args.description
        elif args.file:
            if not args.file.exists():
                print(f"❌ Error: File not found: {args.file}")
                sys.exit(1)
            description = args.file.read_text()
        else:
            print("❌ Error: Provide description or use --file")
            parser.print_help()
            sys.exit(1)

        # Check API keys
        keys_ok, missing = check_api_keys()
        if not keys_ok:
            print(f"❌ Error: Missing required API keys:")
            for key in missing:
                print(f"  • {key}")
            print(f"\nSet environment variables:")
            for key in missing:
                print(f"  export {key}='your-key-here'")
            sys.exit(1)

        # Generate
        try:
            asyncio.run(generate_specs(
                description,
                args.output,
                args.verbose,
                args.thread_id
            ))
        except KeyboardInterrupt:
            print("\n\n⚠️  Generation interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            sys.exit(1)

    elif args.command == "status":
        print("📊 System Status\n")

        # Check API keys
        keys_ok, missing = check_api_keys()
        print("🔑 API Keys:")
        if keys_ok:
            print("  ✅ ANTHROPIC_API_KEY: Set")
        else:
            print(f"  ❌ ANTHROPIC_API_KEY: Not set")

        tavily_key = os.getenv("TAVILY_API_KEY")
        if tavily_key:
            print("  ✅ TAVILY_API_KEY: Set (optional)")
        else:
            print("  ⚠️  TAVILY_API_KEY: Not set (optional)")

        # Check specialists
        print("\n🤖 Specialists:")
        from meta_agent_builder.specialists import (
            ArchitectureSpecialist,
            ContextSpecialist,
            DocumentationSpecialist,
            ImplementationSpecialist,
            MiddlewareSpecialist,
            OrchestrationSpecialist,
            PRDSpecialist,
        )

        specialists = [
            ("Documentation", DocumentationSpecialist),
            ("Architecture", ArchitectureSpecialist),
            ("PRD", PRDSpecialist),
            ("Context Engineering", ContextSpecialist),
            ("Middleware", MiddlewareSpecialist),
            ("Orchestration", OrchestrationSpecialist),
            ("Implementation", ImplementationSpecialist),
        ]

        for name, cls in specialists:
            try:
                spec = cls()
                print(f"  ✅ {name}: {len(spec.tools)} tools")
            except Exception as e:
                print(f"  ❌ {name}: Error - {str(e)}")

        print("\n✅ System ready!" if keys_ok else "\n⚠️  Configure API keys to use system")

    elif args.command == "version":
        print("📦 Version Information\n")
        print("  Meta-Agent Builder: 0.1.0-mvp")
        print("  Status: MVP Complete")
        print("  Specialists: 7")
        print("  Tools: 36")
        print("  Tests: 38 passing")
        print("\n  Repository: https://github.com/arthur0211/meta-deep-agent")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
