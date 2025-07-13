# Slash Flow: Simple Context Engineering

Many Agentic Coding context management solutions like Cline's Memory Bank are impressively robust, but can be complex,  hard to get started with, and try to be overly magical.

Slash Flow is a stupid simple context management solution that gets and keeps you in a flow state without having to stress about context windows or project documentation.

## Overview

Slash Flow is made for Claude Code. It leverages Claude's `/commands`, MCP, sub-agents, and markdown docs to create a simple and straightforward Task & Context Management Workflow for Agentic Coding with Claude Code.

The workflow and commands are simple

1. `new_task` - start a new task, document the task, create an initial plan

2. `session_handoff` - document progress/status to start a new thread with fresh context

3. `resume_task` - find active_tasks, read all documentation and session_log, and continue where you left off

4. `code_review` - 3 stages of code_review conducted by an independent sub-agent to catch issues/gaps

5. `finish_task` - update session_log, dispatch independent agent to fully document the feature and PR description.

Its perfect for people new to Agentic Coding and Context Engineering who want to be more productive but aren't sure where to start.

The primary benefit -- a simple and straight-forward way to maintain context/continuity across AI Coding Agent threads.

## Key Benefits

- **Go Faster**: Simple, Repeatable, Starter workflow that you can customize and extend.

- **Never Lose Context**: Pick up exactly where you left off, even weeks later

- **Ship Higher Quality Code**: Catch bugs and issues at every development stage

- **Save Time on Documentation**: Auto-generate PR descriptions, feature docs, and architecture updates

- **Onboard New Agents Fast**: Complete task history and decision context in organized docs

## Workflow Commands

The workflow consists of five core commands that guide you through the complete development lifecycle:

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
├── session_handoff.md
├── code_review.md
└── finish_task.md

yolo-mode/
├── settings.json
└── yolo_mode_safety_hook.py
```

When resuming tasks, your agent will look in active_tasks and confirm which task to resume (if you have multiple).

## Quick Start

### 1. Copy the commands into your command folder
Create a `commands/` directory in your Claude Code `.claude` directory and copy/paste the content from each command file:
- `new_task.md` - Task creation and planning
- `resume_task.md` - Session continuation
- `session_handoff.md` - Session logging
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

## Bonus - 🚨 Yolo Mode - Enhanced Permissions with Safety (Claude Hooks)

Run Claude Code in `--dangerously-skip-permissions` mode with a PreToolUse safety hook that prevents dangerous file deletion commands.

Learn about Claude Code hooks here -> https://docs.anthropic.com/en/docs/claude-code/hooks

> ⚠️ **Use with caution**: While the safety hook when properly configured prevents common destructive commands, `--dangerously-skip-permissions` mode should still be used carefully and only in sandboxed development environments.

**What it enables:**
- Claude can run terminal commands without permission prompts
- Faster development workflow with fewer interruptions
- Safety net prevents accidental file system damage

**Safety Hook:**
The included `yolo_mode_safety_hook.py` script blocks dangerous commands (`rm`, `sudo`) before they execute, preventing accidental file deletion and privilege escalation.

**Setup:**

1. **Copy the safety files** from the `yolo-mode/` directory to your global `.claude` directory:
   - `.claude/settings.json` - Claude Code configuration with PreToolUse hook
   - `.claude/yolo_mode_safety_hook.py` - Python script that blocks dangerous commands (rm, sudo)

2. **Run Claude Code in Yolo Mode:**
   ```bash
   claude-code --dangerously-skip-permissions
   ```

3. **What happens:**
   - Claude runs terminal commands automatically
   - Before any Bash command executes, the safety hook checks it
   - Dangerous commands (`rm`, `sudo`) are blocked
   - All other commands proceed normally

4. **Important - Test First! (highly recommend to ensure proper setup):**
    - Exit Claude Code and start a new session w/`--dangerously-skip-permissions`
    - Have Claude Create and attempt to delete a test file
    - verify that rm commands are blocked

**Files included:**
- `yolo-mode/settings.json`: Configures the PreToolUse hook
- `yolo-mode/yolo_mode_safety_hook.py`: Python script that prevents dangerous commands (rm, sudo)

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
