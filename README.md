# Slash Flow: Simple Context Engineering

Many Agentic Coding context management solutions like Cline's Memory Bank are impressively robust, but can be hard to understand if new to Agentic coding, include a large number of workflows to understand, and at times try to be overly magical.

Slash Flow is a stupid simple context management solution that gets and keeps you in a flow state without having to stress about context windows or project documentation.

## Overview

Slash Flow is made for Claude Code. It leverages Claude's `/commands`, MCP, sub-agents, and markdown docs to create a simple and straightforward Task & Context Management Workflow for Agentic Coding with Claude Code.

The workflow and commands are simple

1. `new_task` - start a new task, document the task, create an initial well researched implementation plan

2. `create_tasks` - creates a task list with detailed sub-tasks based on your implementation plan, including a sub-agent parralelization strategy

3. `session_handoff` - document progress/status to start a new thread with fresh context

4. `resume_task` - find active_tasks, read all documentation and session_log, and continue where you left off

5. `create_tasks` - generate detailed task lists with parallel sub-agent execution strategies

6. `code_review` - 3 stages of code_review conducted by an independent sub-agent to catch issues/gaps

7. `finish_task` - update session_log, dispatch independent agent to fully document the feature and PR description.

Its perfect for people new to Agentic Coding and Context Engineering who want to be more productive but aren't sure where to start.

The primary benefit -- a simple and straight-forward way to maintain context/continuity across AI Coding Agent threads.

## Key Benefits

- **Go Faster**: Simple, Repeatable, Starter workflow that you can customize and extend.

- **Never Lose Context**: Pick up exactly where you left off, even weeks later

- **Ship Higher Quality Code**: Catch bugs and issues at every development stage

- **Save Time on Documentation**: Auto-generate PR descriptions, feature docs, and architecture updates

- **Onboard New Agents Fast**: Complete task history and decision context in organized docs

## Workflow Commands

The workflow consists of six core commands that guide you through the complete development lifecycle:

### 🚀 `/new_task` - Task Creation
**Purpose**: Initialize new development tasks with proper context and planning.

**What it does**:
- Gathers task requirements and resources
- Researches relevant documentation and codebase
- Creates structured task summaries and initial plans
- Sets up organized task directory structure

**Output**:
- `docs/active_tasks/{task_name}/task_summary.md`
- `docs/active_tasks/{task_name}/initial_plan.md`

### 📋 `/create_tasks` - Parallel Task Generation
**Purpose**: Generate detailed, step-by-step task lists with parallel sub-agent execution strategies.

**What it does**:
- Analyzes task specifications and requirements
- Creates 5-8 high-level parent tasks covering full implementation scope
- Breaks down parent tasks into actionable sub-tasks
- Identifies dependencies and opportunities for parallel execution
- Creates sub-agent strategies with execution waves
- Generates detailed sub-agent specifications with context and deliverables

**Output**: `docs/active_tasks/{task_name}/{task_name}_tasks.md`

**Use when**: Breaking down complex features into manageable, parallelizable work units.

### 🔄 `/resume_task` - Session Resume
**Purpose**: Continue work on existing tasks with full context restoration.

**What it does**:
- Lists and helps select active tasks
- Reviews task summaries and session logs
- Analyzes current progress and roadblocks
- Proposes next steps based on previous work

**Use when**: Starting a new coding session or switching between tasks.

### 📝 `/session_handoff` - Session Logging
**Purpose**: Create detailed logs for seamless session transitions.

**What it does**:
- Reviews previous session logs
- Documents current session progress
- Records challenges and decisions made
- Outlines next steps for future sessions

**Output**: `docs/active_tasks/{task_name}/session_logs/{timestamp}.md`

### 🔍 `/code_review` - Multi-Stage Reviews
**Purpose**: Conduct thorough code reviews tailored to development stage.

**Review Types**:
- **Code Complete**: Basic functionality and structure review
- **Feature Complete**: Comprehensive logic and quality review
- **Pre-PR**: Production-ready polish and security review

**What it does**:
- Detects current development stage
- Generates detailed, stage-appropriate review prompts
- Dispatches an **independent Sub-Agent** to review code
- Creates comprehensive review reports
- Provides actionable improvement recommendations

**Output**: `docs/active_tasks/{task_name}/code_complete_code_review.md`

### ✅ `/finish_task` - Task Finalization
**Purpose**: Complete tasks with comprehensive documentation and cleanup.

**What it does**:
- Creates session logs for current work
- Dispatches an independent sub-agent
- Generates PR descriptions and feature documentation
- Updates project architecture documentation
- Provides coding rules recommendations
- Moves completed tasks to archive

**Output**: Multiple documentation files and clean task transition

## Documentation Directory Structure

The workflow creates and maintains this organized structure:

```
docs/
├── active_tasks/
│   └── {task_name}/
│       ├── task_summary.md
│       ├── initial_plan.md
│       ├── session_logs/
│       │   └── {timestamp}.md
│       └── {various_documentation}.md
└── completed_tasks/
    └── {task_name}/
        └── [archived task files]

commands/
├── new_task.md
├── resume_task.md
├── create_tasks.md
├── session_handoff.md
├── code_review.md
└── finish_task.md
```

When resuming tasks, your agent will look in active_tasks and confirm which task to resume (if you have multiple).

## Quick Start

### 1. Copy the commands into your command folder
Create a `commands/` directory in your Claude Code `.claude` directory and copy/paste the content from each command file:
- `new_task.md` - Task creation and planning
- `resume_task.md` - Session continuation
- `session_handoff.md` - Session logging
- `create_tasks.md` - Parallel task generation with sub-agent strategies
- `code_review.md` - Multi-stage code reviews
- `finish_task.md` - Task finalization

### 2. Configure the MCP servers using our mcp.json
Copy the included `mcp.json` file to your project directory (same level as your `.claude` folder). This provides:
- **Sequential Thinking** - Structured problem solving
- **Context7** - Up-to-date library documentation

### 3. Run new_task from a clean branch
Start with a clean git state and use `/new_task` to initialize your first development task.

That's it! You now have a complete AI agent development workflow.

## MCP Server Setup Guide

To fully utilize this workflow, you'll want to set up the recommended MCP servers. These enhance the AI agent's capabilities significantly.

### Prerequisites

**For Node.js-based servers:**
- Node.js (v18.0.0 or higher)
- npm package manager

**For Python-based servers:**
- Python 3.10 or higher
- pip package manager

### Sequential Thinking MCP Server

Sequential Thinking enables structured, step-by-step problem solving within conversations.

**Configuration for Claude Code:**

This repository includes a pre-configured `mcp.json` file that you can copy to your project directory (same directory as your `.claude` folder and `Claude.md`).

Alternatively, create your own `mcp.json` file with this configuration:
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

**What it enables:**
- Break down complex problems into manageable steps
- Track reasoning progress through multi-step problems
- Revise previous thinking when necessary
- Branch into alternative solution paths
- Maintain context throughout the reasoning process

### Context7 MCP Server

Context7 provides up-to-date library documentation and eliminates AI hallucination of outdated APIs.

**Configuration for Claude Code:**

This repository includes a pre-configured `mcp.json` file that you can copy to your project directory (same directory as your `.claude` folder and `Claude.md`).

Alternatively, create your own `mcp.json` file with this configuration:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

**What it enables:**
Simply add `use context7` to any coding prompt to get current, accurate documentation:
- `Create a basic Next.js project with app router. use context7`
- `Write error handling for React components. use context7`
- `Set up authentication with Supabase. use context7`

### Complete Configuration Example

Here's the complete `mcp.json` file (included in this repository) that includes all recommended MCP servers:

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
    "context7": {
      "command": "npx",
      "args": [
        "-y",
        "@upstash/context7-mcp@latest"
      ]
    }
  }
}
```

## Good For:

### Early Stage Development

- **Avoid over-engineering**: Stick to YAGNI + SOLID + KISS + DRY principles
- **Focus on MVP**: Prioritize functionality over perfect architecture
- **Continuity**: Maintain development context across AI Coding sessions

### New to Agentic Coding

- **Basic Context Engineering**: Learn how to manage context with a simple repeatable context management workflow for tasks
- **Think in tasks, not files**: Break work into discrete, resumable tasks rather than traditional file-based workflows
- **Build trust gradually**: Use code reviews to understand what AI agents do well vs. where you need oversight
- **Leverage AI memory**: Session logs mean you never lose context - even across weeks or months

## Troubleshooting

### Agent Not Following Command Instructions

**Problem**: The AI agent doesn't follow the specific workflow command instructions or seems to ignore the command prompt.

**Solution**: Simply nudge the agent by explicitly naming the command you want it to follow.

**Examples**:
- "Please follow the `/new_task` command to create a new task"
- "Use the `/resume_task` workflow to continue where we left off"
- "Run the `/code_review` command to review the current code"
- "Follow the `/session_handoff` process to document this session"

**Why this works**: Explicitly naming the command helps the agent focus on the specific workflow instructions rather than generic responses.

### Docs not being created where I like

Your project structure may have a specific approach to documentation. Now that you have the commands, you are welcome to adjust them! Just search for docs/active_task and replace all with the path to your docs directory.

## Contributing

This workflow is designed to be:
- **Extensible**: Add your own commands and processes
- **Adaptable**: Modify existing commands for your needs
- **Shareable**: Use as a foundation for team workflows

Feel free to fork, modify, and share your improvements!

## License

MIT License - Feel free to use, modify, and distribute as needed.

---

*This workflow represents a practical approach to AI-assisted development that balances structure with flexibility. It's designed to grow with your projects and adapt to your specific development needs.*
