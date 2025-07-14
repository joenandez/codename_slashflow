
# Create a Task List with Parallel Sub-Agents

## Goal

The purpose of this prompt is to generate a detailed, step-by-step task list (Markdown) that will walk a developer through implementing a feature described in an **Input Specification** (Task Summary, Plan, PRD, Technical Spec, or any other requirements doc).

You will also identify opportunities for parallel execution and create a sub-agent strategy for efficient implementation.

## **Step 1 -- Identify Inputs for Context & Reference**

* If you are already working on a specific task in this session with the user, proceed to Step 2.

* If you recieved this prompt with no existing session context or active tasks from the user, you must first confirm with the user which active_task (or new task) they'd like you to create tasks for.

  * First, identify the current active_tasks at docs/active_tasks. each directory is an active task.

  * Then, reply to the user to confirm which task to work on, or if they'd like to create tasks for something else.

  * For example:

> "I found 3 active tasks. Which would you like me to create tasks for? (1) {task_name}, (2) {task_name}, or (3) {task_name}. I can also create tasks from any input specification if you'd like to share one with me."

## **Step 2 - Analyze Specifications**

Read all relevant documentation provided by the user and/or in the /docs/active_tasks/{task_name} directory, including
	* task_summary.md
	* initial_plan.md
	* any doc in /docs/active_tasks/{task_name}/session_logs directory
	* any other supporting documents in the directory
  * any additional docs shared by the user.

Pay special attention to functional requirements, user stories, constraints, etc.

## **Step 3 - Generate Parent Tasks**

- Create the tasks file in docs/active_tasks/{task_name} directory, titled `{task_name}_tasks.md`
- Draft ~5-8 high-level (parent) tasks that cover the full implementation scope
- When drafted, present only the parent tasks (no sub-tasks yet) and prompt the user:

> "I have generated the high-level tasks. Ready to expand into sub-tasks? Respond with 'Go' to proceed."

**Wait for the user's confirmation before proceeding**

Pause until the user replies "Go".

## **Step 4 - Generate Sub-Tasks and Parallel Analysis**

### Sub-Tasks & Parallel Tasks
- Break down each parent task into actionable sub-tasks
- Analyze sub-tasks for dependencies and independence
- Identify which tasks can be executed in parallel
- Group independent tasks into sub-agent assignments

### Create Sub-Agent Strategy
- Define execution waves based on dependencies
- Create detailed sub-agent specifications with:
  - Unique agent name and responsibilities
  - Required context/initialization information
  - Specific task assignments
  - Dependencies on other agents or tasks
  - Expected deliverables

### Identify Relevant Files
List any files likely to be created or modified, including test files.

### Generate Final Output
Combine all elements in the structure below.

### Save Task List
Update the tasks document in docs/active_tasks/{task_name} directory, `{task_name}_tasks.md`

### Expected Output Format

```markdown
# {Feature} Tasks: {Brief Description}

## Execution Strategy

This {feature} will be executed using parallel sub-agents coordinated by a master planner. The tasks are organized into waves based on dependencies.

## Parallel Agent Groups

### Wave 1: Independent Agents (Can Start Immediately)

#### 1. {Agent Name}
**Responsibilities:**
- Bullet list of key responsibilities
- Be specific about what this agent will do

**Context to Initialize:**
- List all information the agent needs
- Include file paths, branch names, etc.
- Reference documentation locations
- Specify any commands or tools needed

**Tasks:** {comma-separated task numbers}

**Expected Deliverables:**
- What files/changes this agent will produce
- Any documentation or test results

#### 2. {Next Agent Name}
[Same structure as above]

### Wave 2: {Dependency Description} (After {prerequisite} complete)

[Continue with dependent agents...]

### Wave N: Testing & Verification (After all implementation complete)

[Final wave agents...]

---

## Relevant Files

### {Category 1}
- `path/to/file.ts` – Brief reason this file matters
- `path/to/file.test.ts` – Unit tests for file.ts

### {Category 2}
- `path/to/other/files.tsx` – Description

### Notes
- Testing strategy notes
- Build/deployment notes
- Any special considerations

## Master Planner Execution Notes

1. **Initial Setup** - What the master planner must do first
2. **Wave Sequencing** - When to spawn each wave of agents
3. **Dependency Management** - How to track completion and dependencies
4. **Conflict Resolution** - When master planner intervention may be needed
5. **Progress Tracking** - How to monitor agent progress

## Tasks

- [ ] 1.0 **Parent Task Title** [{Responsible Agent/Role}]
  - [ ] 1.1 Sub-task description [{Agent Name}]
    - Status: not started
    - Notes:
  - [ ] 1.2 Sub-task description [{Agent Name}]
    - Status: not started
    - Notes:

- [ ] 2.0 **Parent Task Title** [{Responsible Agent/Role}]
  - [ ] 2.1 Sub-task description [{Agent Name}]
    - Status: not started
    - Notes:

[Continue with all tasks, each annotated with responsible agent]
```

### Sub-Agent Specification Guidelines

When creating sub-agents, ensure each specification includes:

1. **Clear Scope** - Agent should have a focused, well-defined area of responsibility
2. **Complete Context** - All information needed to complete tasks independently
3. **No Circular Dependencies** - Agents in the same wave must be truly independent
4. **Testable Deliverables** - Clear outputs that can be verified
5. **Error Handling** - What to do if blocked or encountering issues

### Dependency Analysis Rules

1. **File Dependencies** - Tasks modifying the same file cannot be parallel
2. **Logical Dependencies** - Tasks requiring output from other tasks must be sequenced
3. **Testing Dependencies** - Tests can only run after implementation
4. **Configuration Dependencies** - Package/build changes must complete before dependent work

### Wave Organization Principles

1. **Wave 1** - Truly independent tasks (documentation, file copies, new file creation)
2. **Wave 2** - Tasks dependent on initial setup or configuration
3. **Wave 3** - Complex integrations requiring multiple prerequisites
4. **Wave N-1** - Final implementation and polish
5. **Wave N** - Testing and verification

### Interaction Model

The assistant must pause after Phase 1 until the user types "Go". This ensures the high-level plan matches expectations before diving into sub-agent strategy and detailed sub-tasks.

### Target Audience

The final task list will be consumed by:
- **Master Planner AI** - To coordinate sub-agent execution
- **Sub-Agent AIs** - Each receiving their specific section
- **Human Developers** - For manual tasks or oversight

The document should be clear enough for all three audiences.

### Final Output

- **Format:** Markdown (`.md`)
- **Location:** `/docs/active_tasks/{task_name}`
- **Filename:** `{feature}_tasks.md` _(e.g., `live_activity_widget_tasks.md`)_