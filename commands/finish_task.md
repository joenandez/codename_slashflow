## Task

This is the final task in our feature development cycle.

Your task is to finalize the current task by dispatching a single independent sub-agent to complete critical project documentation tasks.

## Step 0: IMPORTANT! Save Session Details

Before you proceed to Step 1, save the details of the currently active thread in a session_log.

If this is a new thread with no previous context or in progress work, skip to step 2.

If this is an active thread with in progress work, first use the /session_handoff command in your commands directory (.cluade/commands/session_handoff.md) to create a session_log in active_tasks/{task_name}/session_logs directory.

Do not proceed to Step 1 unless you have completed this step

## Step 1: Confirm Branch Details

The sub-agent needs to know what code to review. Identify the current branch, identify where the current branch branched from, and confirm with the user the scope of the code that is going to be reviewed by the sub-agent before continuing.

e.g.,:  "Before I kick off the sub-agent's task, let's confirm the code changes we want to review. It looks like we're on Branch B, which branched from Branch A. Are we reviewing the changes between these two branches?"

## Step 2: Copy and Use This Sub-Agent Prompt

Copy the following complete prompt and send it to initiate a new sub-agent conversation. Replace `{task_name}`, `{branch_details}`, and `{scope_details}` with the appropriate values:

---

**SUB-AGENT PROMPT START:**

You are a documentation specialist sub-agent tasked with finalizing project documentation for a completed feature implementation.

## Context
- **Task Name**: {task_name}
- **Branch Details**: {branch_details}
- **Scope of Changes**: {scope_details}

## Your Mission
Complete all 5 tasks below in sequence. Each task builds on the previous one, so complete them in order.

### Task 1: Gather Complete Context
Before starting any documentation, you must:
- Review all code changes in the current branch relative to where it originally branched from
- Read and understand: `docs/active_tasks/{task_name}/task_summary.md`, `initial_plan.md`, `tasks.md` (if available), and all files in `session_logs/` directory
- Familiarize yourself with the implementation details and decisions made

### Task 2: Write Pull Request Description
Create a concise yet complete pull request description that:
- Summarizes the feature/changes implemented
- Highlights key technical decisions
- Notes any breaking changes or dependencies
- Save as `docs/active_tasks/{task_name}/PR_description.md`

### Task 3: Write Feature Documentation
Create comprehensive feature documentation that:
- Explains what the feature does and how it works
- Includes usage examples and integration points
- Documents any new APIs, components, or services
- Is thorough enough for a new developer to understand, test, and be productive working on or fixing this feature.
- Save as `docs/active_tasks/{task_name}/{task_name}-documentation.md`

### Task 4: Update Project Architecture README
Update `app/README.md` to:
- Add a concise description of the new feature/changes
- Update any architecture diagrams or component lists if relevant
- Keep additions proportional to the feature size (aim for ≤15 lines total)
- Maintain the existing structure and style

### Task 5: Generate Coding Rules Recommendations
Based on your review of the code and session logs, identify:
- New patterns or utilities that should be reused
- Technical decisions that future work should be aware of
- Lessons learned that could improve future development
- Any coding standards or practices that emerged

Create specific, actionable recommendations for our AI coding agent rules.

Save as `docs/active_tasks/{task_name}/coding_rules_update_recommendations.md`

## Completion Requirements
When finished, confirm you have created all 5 required files:
1. `PR_description.md`
2. `{task_name}-documentation.md`
3. Updated `app/README.md`
4. `coding_rules_update_recommendations.md`
5. Verified all files contain substantial, useful content

Return the coding rules recommendations in your final response.

**SUB-AGENT PROMPT END**

---

## Step 3: Complete Task Finalization

Once the sub-agent has completed all documentation tasks, you must:

### 3.1 Verify Sub-Agent Completion
Confirm all required files exist and contain content:
- [ ] `docs/active_tasks/{task_name}/PR_description.md`
- [ ] `docs/active_tasks/{task_name}/{task_name}-documentation.md`
- [ ] `app/README.md` has been updated
- [ ] `docs/active_tasks/{task_name}/coding_rules_update_recommendations.md`

### 3.2 Move Task to Completed
Use the following commands to move the task from active to completed:

1. **Copy the task directory:**
   ```bash
   cp -r docs/active_tasks/{task_name} docs/completed_tasks/{task_name}
   ```

2. **Verify the copy was successful:**
   ```bash
   ls -la docs/completed_tasks/{task_name}/
   ```

3. **Remove from active tasks:**
   ```bash
   rm -rf docs/active_tasks/{task_name}
   ```

### 3.3 Final Response
Provide a summary response that includes:
- ✅ Confirmation that the task has been moved from active_tasks to completed_tasks
- 📄 Links to all documentation created
- 🔧 The complete coding rules recommendations from the sub-agent
- 🎉 Congratulations on completing the task and excitement for next steps

## Self‑Review Checklist

✅ All five required files exist and are non‑empty
✅ README updated concisely (≤15 added lines)
✅ coding_rules_update_recommendations.md returned in final response
✅ active_tasks/{task_name} moved to completed_tasks/ using cp and rm commands
✅ Verified completed task directory structure matches other completed tasks
