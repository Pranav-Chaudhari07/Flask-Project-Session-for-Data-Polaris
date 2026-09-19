"""
=============================================================================
HELPER MODULE: task_operations.py
Created for Module 02 to demonstrate creating your own Python module!
=============================================================================
"""

# Reusable task functions moved from Module 01
tasks = []

def create_task(title, status="Pending"):
    """Adds a task to our list."""
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "status": status
    }
    tasks.append(task)
    return task

def list_tasks():
    """Returns all current tasks."""
    return tasks
