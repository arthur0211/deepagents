"""Script to test Meta-Agent Builder with investment portfolio analysis project."""
import sys
import os
import asyncio

# Add necessary paths to Python path
sys.path.insert(0, '/home/user/deepagents/libs/deepagents')
sys.path.insert(0, '/home/user/deepagents/meta-agent-builder')

# Read the project description
with open('/home/user/deepagents/test_investment_portfolio.txt', 'r') as f:
    project_description = f.read()

print("="*80)
print("META-AGENT BUILDER TEST")
print("="*80)
print("\nProject Description:")
print("-" * 80)
print(project_description)
print("-" * 80)

# Import Meta Orchestrator
try:
    from meta_agent_builder.orchestrator import MetaOrchestrator
    print("\n✅ Successfully imported MetaOrchestrator")
except ImportError as e:
    print(f"\n❌ Failed to import MetaOrchestrator: {e}")
    sys.exit(1)

# Create orchestrator
try:
    print("\n📦 Creating MetaOrchestrator...")
    orchestrator = MetaOrchestrator()
    print("✅ MetaOrchestrator created successfully")
except Exception as e:
    print(f"❌ Failed to create MetaOrchestrator: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Generate specification
async def generate_spec():
    """Generate the project specification."""
    print("\n🚀 Generating project specification...")
    print("This may take a few minutes as the agents analyze your requirements...\n")

    try:
        # Stream events from the orchestrator
        last_event = None
        async for event in orchestrator.process_project_request(user_request=project_description):
            last_event = event
            # Print progress
            if 'messages' in event:
                messages = event['messages']
                if messages:
                    last_msg = messages[-1]
                    if hasattr(last_msg, 'content') and last_msg.content:
                        # Print agent messages to show progress
                        content = last_msg.content
                        if len(content) > 200:
                            print(f"📝 {content[:200]}...")
                        else:
                            print(f"📝 {content}")

        return last_event
    except Exception as e:
        print(f"\n❌ Error during generation: {e}")
        import traceback
        traceback.print_exc()
        return None

# Run the async function
if __name__ == "__main__":
    result = asyncio.run(generate_spec())

    if result:
        print("\n" + "="*80)
        print("✅ SPECIFICATION GENERATION COMPLETE")
        print("="*80)

        # Save results to files
        output_dir = "/home/user/deepagents/test_output"
        os.makedirs(output_dir, exist_ok=True)

        # Extract deliverables
        if 'deliverables' in result:
            deliverables = result['deliverables']

            for key, value in deliverables.items():
                if value:
                    filename = f"{output_dir}/{key}.md"
                    with open(filename, 'w') as f:
                        f.write(f"# {key.replace('_', ' ').title()}\n\n")
                        f.write(value)
                    print(f"📄 Saved {key} to {filename}")

        # Save full result
        import json
        with open(f"{output_dir}/full_result.json", 'w') as f:
            # Convert result to JSON-serializable format
            serializable_result = {}
            for k, v in result.items():
                if isinstance(v, (str, int, float, bool, list, dict)) or v is None:
                    serializable_result[k] = v
                else:
                    serializable_result[k] = str(v)
            json.dump(serializable_result, f, indent=2)
        print(f"📄 Saved full result to {output_dir}/full_result.json")

        print("\n" + "="*80)
        print("All deliverables saved successfully!")
        print("="*80)
    else:
        print("\n❌ Failed to generate specification")
        sys.exit(1)
