"""
=============================================================================
MODULE 01: Functions and Scope
Project Story: Building our "Task Manager" from Scratch (Step 1)
=============================================================================
Welcome to Day 1!
In this first module, we start our Task Manager project using basic Python
functions. Every backend application begins with simple functions that accept
inputs, perform an action, and return a result.

What you will learn in this module:
1. Writing basic functions (def) with parameters and return values
2. Default arguments (e.g. status="Pending")
3. Variable scope (global task list vs local variables)
4. *args (passing multiple items)
5. **kwargs (passing extra details like priority or due_date)

Next Module Connection:
In Module 02, we will take these functions and move them into a separate
module file so our code stays neat and organized!
=============================================================================
"""

# =============================================================================
# 1. SCOPE: Global List to Store Our Tasks
# =============================================================================
# This list lives in the global scope (available throughout this file).
tasks_list = []


# =============================================================================
# 2. BASIC FUNCTION & DEFAULT ARGUMENTS
# =============================================================================
def add_task(title, status="Pending"):
    """
    Adds a new task to our global tasks_list.
    - 'title' is a required parameter.
    - 'status' has a DEFAULT value of 'Pending'. If not provided, it uses 'Pending'.
    """
    # 'new_id' and 'task' are LOCAL variables (they only exist inside this function)
    new_id = len(tasks_list) + 1
    task = {
        "id": new_id,
        "title": title,
        "status": status
    }
    tasks_list.append(task)
    return task


# =============================================================================
# 3. RETURNING DATA FROM A FUNCTION
# =============================================================================
def get_all_tasks():
    """Returns the current list of tasks."""
    return tasks_list


# =============================================================================
# 4. *args (Passing Multiple Task Titles at Once)
# =============================================================================
def add_multiple_tasks(*titles):
    """
    *titles collects any number of task titles into a tuple.
    Example: add_multiple_tasks("Buy Milk", "Read Book", "Call Friend")
    """
    added = []
    for title in titles:
        task = add_task(title)
        added.append(task)
    return added


# =============================================================================
# 5. **kwargs (Passing Extra Custom Details)
# =============================================================================
def add_detailed_task(title, **extra_info):
    """
    **extra_info collects any extra keyword arguments into a dictionary.
    Example: add_detailed_task("Complete Homework", priority="High", due="Tomorrow")
    """
    task = add_task(title)
    # Add any extra details provided by the user
    for key, value in extra_info.items():
        task[key] = value
    return task


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    print("--- STEP 1: Adding Tasks with Default Arguments ---")
    t1 = add_task("Learn Python Functions")
    print("Created:", t1)

    t2 = add_task("Build Task Manager", status="In Progress")
    print("Created with custom status:", t2)

    print("\n--- STEP 2: Using *args to Add Multiple Tasks ---")
    batch = add_multiple_tasks("Setup Project", "Install Flask", "Run App")
    print(f"Added {len(batch)} tasks in one go!")

    print("\n--- STEP 3: Using **kwargs for Extra Details ---")
    detailed = add_detailed_task("Submit Assignment", priority="High", due_date="Friday")
    print("Task with extra details:", detailed)

    print("\n--- STEP 4: Viewing All Tasks ---")
    for t in get_all_tasks():
        print(f"  [ID {t['id']}] {t['title']} -> {t['status']}")

    print("\n[NEXT STEP] In Module 02, we will organize this code into separate modules!")
