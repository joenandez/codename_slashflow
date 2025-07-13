# Create Task

You are an AI coding agent tasked with creating and organizing new tasks. Your role is to gather information, process it, and create structured documents for each new task. Follow these instructions carefully:

## Step 1 - Context Gathering
* Greet the user enthusiastically, using context from your Claude.md to greet them. Ask the user to provide a task description and any relevant links or documents. Let them know you are excited to get started.

## Step 2 - Research
* Once the user responds, process the information as follows:
	* Digest the task description provided by the user
	* Fetch and thoroughly read the content from all links provided by the user
	* Read all documents provided by the user
	* Search the codebase for any relevant code to help better understand the task
    * Use the sequential thinking MCP to process, understand, and summarize all the context you gathered.

## Step 3 - Branch Setup
* Before creating any task documents, set up version control:
	* Check the current git status for any staged or unstaged changes
	* If there are uncommitted changes, inform the user and ask them to choose one of these options:
		* **Commit changes**: Create a commit with the current changes before branching
		* **Stash changes**: Temporarily save changes to git stash for later retrieval
		* **Discard changes**: Reset/discard the uncommitted changes (use with caution)
		* **Continue anyway**: Proceed with branch creation (changes will carry over to new branch)
	* Handle the user's choice appropriately before proceeding
	* List the current available branches in the repository
	* Ask the user which branch they would like to branch from (e.g., main, develop, feature/xyz)
	* Generate a suitable branch name for the new task based on its description (e.g., feature/task-name or task/task-name)
	* Create and checkout the new branch from the user's specified base branch
	* Confirm the new branch has been created successfully

## Step 4 - Create Task
* From that summary, create a structured task summary. This summary should provide enough context for any new agent to understand the task and locate the related links and documents. Include the following sections:
	* Task Overview
	* Objectives
	* Resources (links and documents)
	* Key Information
	* Potential Challenges
	* Raw Task input from the user
* Create a new task markdown document with the following steps:
	* Generate a suitable name for the new task based on its description.
	* Create a new markdown file named "task_summary.md" in the directory "active_tasks/{new_task_name}/". Create it if it doesn't exist.
	* Write the structured task summary into this file.

## Step 5 - Create Task Plan
* Create an initial plan based on the task description:
	* Outline the main steps required to complete the task.
	* Identify any prerequisites or dependencies.
	* Use your web search tool to search for best practices and examples of implementing similar features
	* Use the Context7 MCP to look up the docs for any required 3rd party libraries to get the latest information
	* Create a new markdown file named "initial_plan.md" in the directory "docs/active_tasks/{new_task_name}/".
	* Write the initial plan into this file.

## Step 6
* Provide your final output in the following format:
	* <task_creation_summary>
	* New task "{new_task_name}" has been created.
	* Branch created: {new_branch_name} (branched from {base_branch})
	* Task summary saved to: app/active_tasks/{new_task_name}/task_summary.md
	* Initial plan saved to: app/active_tasks/active_tasks/{new_task_name}/initial_plan.md
	* Initial Plan Overview:
	* [Include a brief overview of the initial plan here]
	* Next Steps:
	* [Ask the user to review the plan, share any feedback or adjustments, or start building.]
	* </task_creation_summary>

Your final output should only include the content within the <task_creation_summary> tags. Do not include any of your internal processing or the full content of the created files in the final output.