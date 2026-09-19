"""
=============================================================================
MODULE 02: Modules and Packages
Project Story: Building our "Task Manager" from Scratch (Step 2)
=============================================================================
Previously in Module 01:
We wrote functions to add and view tasks inside a single file.

Now in Module 02:
As our Task Manager grows, putting all code in one file becomes messy.
In this module, we learn how to:
1. Create our own reusable Python module (task_operations.py)
2. Use the 'import' statement to use code from other files
3. Use Python's built-in modules (like datetime) to timestamp our tasks
4. Understand pip, virtual environments (venv), and requirements.txt

Next Module Connection:
In Module 03, we will use Object-Oriented Programming (OOP) to represent
a Task as a Class instead of a basic dictionary!
=============================================================================
"""

# =============================================================================
# 1. IMPORTING A BUILT-IN PYTHON MODULE
# =============================================================================
# Python comes with many ready-to-use modules in its Standard Library:
from datetime import datetime

# =============================================================================
# 2. IMPORTING OUR OWN CUSTOM MODULE (task_operations.py)
# =============================================================================
try:
    from task_operations import create_task, list_tasks
except ImportError:
    from Module_Code.task_operations import create_task, list_tasks


# =============================================================================
# 3. ENHANCING TASK MANAGER WITH IMPORTED CODE
# =============================================================================
def add_timestamped_task(title, status="Pending"):
    """
    Creates a task using our imported module function, and adds a timestamp
    using Python's built-in datetime module.
    """
    task = create_task(title, status)
    # Add current date and time
    task["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return task


# =============================================================================
# 4. QUICK GUIDE FOR STUDENTS: VENV & PIP
# =============================================================================
"""
How to setup your project in real life:
1. Create virtual environment:  python -m venv venv
2. Activate it:
     Windows: venv\\Scripts\\activate
     Mac/Linux: source venv/bin/activate
3. Install packages:            pip install flask
4. Save packages:               pip freeze > requirements.txt
"""


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    print("--- STEP 1: Using Functions Imported from task_operations.py ---")
    t1 = add_timestamped_task("Learn Python Modules")
    t2 = add_timestamped_task("Install Virtual Environment", status="Completed")

    print("\n--- STEP 2: Viewing Our Timestamped Tasks ---")
    for t in list_tasks():
        print(f"  [ID {t['id']}] {t['title']} (Status: {t['status']}, Created: {t['created_at']})")

    print("\n[NEXT STEP] In Module 03, we will turn our tasks into a real Python Class!")
