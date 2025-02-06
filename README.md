# To-do-list-
A simple Python-based To-Do List application that allows users to add, edit, delete, and mark tasks as completed, with task persistence through file storage.

# To-Do List Application

## Overview
This is a simple To-Do List application that allows users to add, edit, delete, display, and mark tasks as completed. Tasks are stored in a text file, allowing the app to remember the tasks even after closing and reopening.

## Features
- **Add Task**: Add a new task to the list.
- **Delete Task**: Delete a task by its number.
- **Edit Task**: Modify an existing task.
- **Mark Task as Completed**: Mark a task as completed by appending `- Completed` to it.
- **Display Tasks**: View all tasks currently in the list.
- **Persistent Storage**: Tasks are saved to a file (`tasks.txt`) and loaded when the app restarts.

## Requirements
- Python 3.x

## Installation
1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git

Usage
Start the app by running the Python script.
You will be presented with a menu:
1: Add Task
2: Delete Task
3: Edit Task
4: Display Tasks
5: Mark Task as Completed
6: Exit the app and save tasks to a file.
Follow the prompts to manage your tasks.
Tasks will be saved to tasks.txt and will persist even after the app is closed.

Example
To-Do List
1. Add Task
2. Delete Task
3. Edit Task
4. Display Tasks
5. Mark Task as Completed
6. Exit

Choose an option: 1
Enter a new task: Buy groceries
Task 'Buy groceries' added.

Choose an option: 4
Your tasks:
1. Buy groceries

Code Explanation
add_task(): Adds a new task to the list.
delete_task(): Removes a task by its number.
edit_task(): Edits an existing task.
mark_completed(): Marks a task as completed.
save_tasks_to_file(): Saves tasks to a text file.
load_tasks_from_file(): Loads tasks from the text file on startup.
