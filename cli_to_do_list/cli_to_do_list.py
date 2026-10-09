# CLI To-Do List App: A terminal application to add, delete, edit, and mark tasks as completed using JSON file persistence

# ------Core Functional Requirements--------
# Add Task: Create a new task with a description. Automatically assign a unique identifier (ID) and default status (incomplete/pending).
# List / View Tasks: Display all tasks in a clean, readable format in the terminal (e.g., showing ID, Status, Description).
# Edit / Update Task: Modify the description of an existing task using its ID.
# Mark Completed: Toggle or set a task’s status to "completed" using its ID.
# Delete Task: Remove a task completely from the list using its ID.
# JSON File Persistence: Read existing tasks from a .json file when the app starts, and automatically write/save changes back to the JSON file whenever tasks are created, edited, marked completed, or deleted.
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    # 1. Create file with empty array if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
    # 2. Safely read and parse the JSON file
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Fallback if file is empty or corrupted
        return []

tasks = load_tasks()
len_tasks = len(tasks)

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task_dict = dict()
    task_dict["id"] = max([t["id"] for t in tasks], default=0) + 1
    task_dict["description"] = input("Enter the todo-item: ")
    task_dict["status"] = False
    tasks.append(task_dict)
    # Save the list of tasks to the JSON file
    save_tasks()

def show_tasks():
    for item in tasks:
        print(f"Id: {item['id']}. Description: {item['description']}")

def edit_task(id):
    for item in tasks:
        if item['id'] == id:
            item['description'] = input("Enter updated task: ")
    save_tasks()

def mark_complete(id):
    for item in tasks:
        if item['id'] == id:
            item['status'] = True
    save_tasks()

def delete_task(id):
    for item in tasks:
        if item['id'] == id:
            tasks.remove(item)
    save_tasks()

while True:
    try:
        query = int(input("Enter your choice: \n1. Add Task\n2. Show Tasks\n3. Edit Task\n4. Mark Completed\n5. Delete Task\n6. Exit\n"))
    except ValueError:
        print("Enter number 1-6.")
        continue
    if query == 1:
        add_task()
    elif query == 2:
        show_tasks()
    elif query == 3:
        identifier = int(input("Enter the 'id' of the task, you want to edit: "))
        edit_task(identifier)
    elif query == 4:
        identifier = int(input("Enter the 'id' of the task, you want to mark as complete: "))
        mark_complete(identifier)
    elif query == 5:
        identifier = int(input("Enter the 'id' of the task, you want to delete: "))
        delete_task(identifier)
    elif query == 6:
        break
    else:
        continue