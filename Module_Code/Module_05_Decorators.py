"""
=============================================================================
MODULE 05: Python Decorators
Project Story: Building our "Task Manager" from Scratch (Step 5)
=============================================================================
Previously in Module 04:
We learned how JSON connects Python backends to web clients.

Now in Module 05:
In Flask, almost every URL endpoint is defined with a line starting with '@':
    @app.route("/tasks")
    def get_tasks(): ...

To understand Flask without fear, we must understand what a Decorator is.
A decorator is simply a function that adds extra behavior before or after
another function runs (like logging or timing).

What you will learn in this module:
1. Writing a simple decorator (@log_task_action)
2. How decorators wrap functions
3. How Flask uses this exact concept to register web routes!

Next Module Connection:
In Module 06, we will learn Exception Handling so our backend handles errors
gracefully without crashing!
=============================================================================
"""

# =============================================================================
# 1. WRITING A SIMPLE DECORATOR
# =============================================================================
def log_task_action(func):
    """
    A decorator that prints a message before and after our task function runs.
    """
    def wrapper(*args, **kwargs):
        print(f" [LOG] Starting task operation: '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f" [LOG] Finished '{func.__name__}' successfully!")
        return result
    return wrapper


# =============================================================================
# 2. APPLYING THE DECORATOR WITH THE '@' SYNTAX
# =============================================================================
@log_task_action
def create_new_task(title):
    print(f"  --> Writing task '{title}' into database...")
    return {"id": 1, "title": title, "status": "Pending"}


# =============================================================================
# 3. HOW FLASK USES THIS EXACT PATTERN (Mini Router Demo)
# =============================================================================
# A dictionary that maps URL paths to functions
routes = {}

def my_route(path):
    """Mini version of Flask's @app.route decorator!"""
    def decorator(func):
        routes[path] = func  # Save the function for this URL
        return func
    return decorator

# Let's register a route using our custom decorator:
@my_route("/tasks")
def show_tasks_page():
    return "Here are your tasks!"


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    print("--- STEP 1: Calling Our Decorated Function ---")
    task = create_new_task("Learn Flask Decorators")
    print("Result:", task)

    print("\n--- STEP 2: Demystifying Flask's @app.route ---")
    print("Routes registered in our dictionary:", routes)
    print("When a user visits '/tasks', the server runs:", routes["/tasks"]())

    print("\n[NEXT STEP] In Module 06, we will learn Exception Handling to catch errors!")
