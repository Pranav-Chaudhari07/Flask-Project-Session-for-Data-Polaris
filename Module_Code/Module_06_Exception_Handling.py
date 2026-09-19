"""
=============================================================================
MODULE 06: Exception Handling
Project Story: Building our "Task Manager" from Scratch (Step 6)
=============================================================================
Previously in Module 05:
We learned about decorators and how Flask maps URLs to functions.

Now in Module 06:
What happens if a user searches for a task ID that doesn't exist?
Without error handling, Python crashes and the web server throws an ugly error!
In this module, we learn defensive programming to catch and handle errors.

What you will learn in this module:
1. The try...except...finally block
2. Creating a custom exception (TaskNotFoundError)
3. Preventing crashes and returning friendly error messages

Next Module Connection:
Modules 07, 08, and 09 cover the theory of Web, HTTP Verbs, and Status Codes
(covered in the Preparation Guide text files).
In Module 10, we will launch our FIRST REAL FLASK APPLICATION!
=============================================================================
"""

# Sample tasks list in our Task Manager
tasks = [
    {"id": 1, "title": "Learn Python Foundation", "status": "Completed"},
    {"id": 2, "title": "Start Flask Web App", "status": "Pending"}
]

# =============================================================================
# 1. CUSTOM EXCEPTION
# =============================================================================
class TaskNotFoundError(Exception):
    """Custom exception raised when a requested task does not exist."""
    pass


# =============================================================================
# 2. FUNCTION THAT RAISES AN EXCEPTION DEFENSIVELY
# =============================================================================
def find_task_by_id(task_id):
    """Finds a task or raises TaskNotFoundError if missing."""
    for task in tasks:
        if task["id"] == task_id:
            return task
            
    # If not found, raise our custom error
    raise TaskNotFoundError(f"Task with ID {task_id} not found.")


# =============================================================================
# 3. HANDLING THE ERROR WITH TRY...EXCEPT
# =============================================================================
def safe_get_task(task_id):
    """
    Safely retrieves a task without crashing the server.
    """
    try:
        task = find_task_by_id(task_id)
        print(f" [SUCCESS] Found Task: {task['title']}")
        return task
    except TaskNotFoundError as error:
        print(f" [HANDLED ERROR] {error}")
        return {"error": str(error)}
    finally:
        print(" [CLEANUP] Search attempt finished.")


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    print("--- STEP 1: Fetching a Task that Exists (Happy Path) ---")
    safe_get_task(1)

    print("\n--- STEP 2: Fetching a Task that Does NOT Exist (Error Path) ---")
    safe_get_task(99)

    print("\n[NEXT STEP] Review Modules 07-09 theory in Preparation_guide/.")
    print("Then in Module 10, we begin FLASK WEB DEVELOPMENT!")
