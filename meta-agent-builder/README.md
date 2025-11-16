# 🧠 Meta-Agent Builder

> **Automated Project Specification Generator using Deep Agents**

A sophisticated meta-agent system that automatically generates complete project specifications from a simple description.

## 🎯 What It Does

**Input:**
```
"Create a research agent with web search and document analysis"
```

**Output:**
- Complete system architecture
- Product Requirements Document (PRD)
- Technical specifications
- Implementation guides
- Code templates

All generated using a coordinated team of 7 specialist Deep Agents.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Anthropic API key
- Tavily API key (for web search)

### Installation

```bash
# Clone repository
cd meta-agent-builder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.template .env
# Edit .env and add your API keys
```

### Run Example

```bash
# Set environment variables
export ANTHROPIC_API_KEY='your-key-here'
export TAVILY_API_KEY='your-key-here'  # Optional

# Run the complete example with all 7 specialists
python examples/mvp_example.py
```

Or use programmatically:

```python
import asyncio
from meta_agent_builder.orchestrator import MetaOrchestrator

async def main():
    orchestrator = MetaOrchestrator()

    user_request = """
    Create a research agent system that searches the web,
    analyzes findings, and generates comprehensive reports.
    """

    async for event in orchestrator.process_project_request(user_request):
        if "messages" in event:
            print(event["messages"][-1].content)

asyncio.run(main())
```

---

## 📁 Project Structure

```
meta-agent-builder/
├── meta_agent_builder/          # Main package
│   ├── orchestrator/            # Meta-Orchestrator
│   ├── specialists/             # 7 Specialist Agents
│   ├── backends/                # CompositeBackend config
│   ├── middleware/              # Custom middleware
│   ├── tools/                   # Custom tools
│   ├── prompts/                 # Agent prompts
│   ├── validation/              # Validation pipeline
│   └── config/                  # Configuration
│
├── tests/                       # Test suite
├── templates/                   # Project templates
├── examples/                    # Example projects
└── meta-agent-builder-specs/   # Complete documentation
```

---

## 🏗️ Architecture

### 7 Specialist Agents

1. **Documentation Specialist** - Researches Deep Agents capabilities
2. **Architecture Specialist** - Designs system architecture
3. **PRD Specialist** - Creates product requirements
4. **Context Engineering Specialist** - Designs context management
5. **Middleware Specialist** - Designs middleware stacks
6. **Orchestration Specialist** - Designs agent orchestration
7. **Implementation Specialist** - Generates implementation guides

### Key Features

- **Self-Improving Agents** - Learn and evolve between executions
- **Persistent Knowledge** - Cross-session memory using StoreBackend
- **Automated Validation** - Built-in quality checks
- **Template Reuse** - 60% faster on similar projects
- **Intelligent Orchestration** - Parallel execution where possible

---

## 🔧 Implementation Status

### ✅ Completed (MVP)

- [x] Project structure
- [x] Backend configuration (CompositeBackend with routing)
- [x] Base specialist class
- [x] All 7 specialist agents implemented:
  - [x] Documentation Specialist (with internet search, code extraction, summarization)
  - [x] Architecture Specialist (with Mermaid diagrams, hierarchy validation, middleware suggestions)
  - [x] PRD Specialist (with requirements analysis, personas, acceptance criteria, metrics)
  - [x] Context Engineering Specialist (with prompt design, state management, memory strategies)
  - [x] Middleware Specialist (with middleware configuration, stack planning, optimization)
  - [x] Orchestration Specialist (with workflow patterns, coordination, error handling)
  - [x] Implementation Specialist (with code templates, project structure, implementation guides)
- [x] Meta-Orchestrator with all 7 specialists
- [x] 37 custom tools across all domains
- [x] Complete system prompts for all agents
- [x] Working end-to-end example
- [x] Comprehensive documentation

### 📋 Planned

- [ ] Custom middleware (ValidationMiddleware, ProgressTrackingMiddleware)
- [ ] CLI interface
- [ ] Validation pipeline
- [ ] Test suite
- [ ] Template library
- [ ] Performance optimizations

---

## 📚 Documentation

Complete technical specifications are available in `/meta-agent-builder-specs/`:

- [Technical Specification](../meta-agent-builder-specs/00-TECHNICAL_SPECIFICATION.md)
- [Implementation Guide](../meta-agent-builder-specs/implementation/IMPLEMENTATION_GUIDE.md)
- [Quick Start](../meta-agent-builder-specs/QUICK_START.md)
- [Complete Index](../meta-agent-builder-specs/INDEX.md)

---

## 🛠️ Development

### Setup Development Environment

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Format code
black meta_agent_builder/
ruff check meta_agent_builder/
```

### Project Configuration

- **pyproject.toml** - Project metadata and dependencies
- **requirements.txt** - Production dependencies
- **.env.template** - Environment variable template

---

## 🎓 Technology Stack

| Component | Technology |
|-----------|------------|
| Framework | DeepAgents 0.2.9+ |
| LLM | Claude Sonnet 4.5 |
| Storage | CompositeBackend (State + Store) |
| Tools | Tavily (web search) |
| Orchestration | LangGraph |

---

## 📊 Performance Targets

| Metric | Target |
|--------|--------|
| First execution | < 30 min |
| Subsequent execution | < 12 min |
| Token cost reduction | 30% |
| Quality score | > 95% |

---

## 🤝 Contributing

This is an active implementation of the specifications in `/meta-agent-builder-specs/`.

To contribute:
1. Review the specifications
2. Check the implementation status above
3. Pick a pending component
4. Follow the implementation guide

---

## 📄 License

[To be determined]

---

## 🙏 Acknowledgments

- **LangChain Team** - For Deep Agents framework
- **Anthropic** - For Claude
- **Community** - For feedback and support

---

**Status:** ✅ MVP Complete - Ready for Testing
**Version:** 0.1.0-mvp
**Last Updated:** 2025-11-16

All 7 specialists implemented and integrated. System generates complete project specifications from natural language descriptions.
