"""
=============================================================================
MODULE 11: Flask Routing
Project Story: Building our "Task Manager" Web App (Step 8)
=============================================================================
Previously in Module 10:
We created static routes like '/' and '/about'.

Now in Module 11:
In our Task Manager, we need to show individual tasks:
- Task 1: /tasks/1
- Task 2: /tasks/2
Instead of writing 100 separate routes, Flask provides DYNAMIC ROUTES!

What you will learn in this module:
1. Static routes vs Dynamic routes with variables
2. Using the integer converter: <int:task_id>
3. Using the string converter: <string:category>
4. Generating URLs dynamically with url_for()

Next Module Connection:
In Module 12, we will learn Query Parameters (like /tasks?status=Pending)
and how to read data sent from forms!
=============================================================================
"""

from flask import Flask, url_for

app = Flask(__name__)

# Our list of tasks
tasks = [
    {"id": 1, "title": "Learn Flask Basics", "status": "Completed"},
    {"id": 2, "title": "Understand Dynamic Routing", "status": "In Progress"},
    {"id": 3, "title": "Connect HTML Templates", "status": "Pending"}
]

# =============================================================================
# 1. STATIC ROUTE: List all tasks
# =============================================================================
@app.route("/tasks")
def list_tasks():
    output = "<h2>All Tasks:</h2><ul>"
    for t in tasks:
        output += f"<li><a href='/tasks/{t['id']}'>{t['title']}</a> ({t['status']})</li>"
    output += "</ul>"
    return output


# =============================================================================
# 2. DYNAMIC ROUTE WITH INTEGER CONVERTER (<int:task_id>)
# =============================================================================
@app.route("/tasks/<int:task_id>")
def get_single_task(task_id):
    """
    <int:task_id> automatically converts the URL segment into an integer.
    If a user visits /tasks/hello, Flask automatically returns 404!
    """
    for t in tasks:
        if t["id"] == task_id:
            return f"<h3>Task #{t['id']} Details</h3><p>Title: {t['title']}</p><p>Status: {t['status']}</p>"

    return f"<h3>Task #{task_id} not found!</h3>", 404


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    client = app.test_client()

    print("--- STEP 1: Testing /tasks (Static List) ---")
    r1 = client.get("/tasks")
    print("Status:", r1.status_code)

    print("\n--- STEP 2: Testing /tasks/1 (Dynamic Integer Route) ---")
    r2 = client.get("/tasks/1")
    print(r2.data.decode("utf-8"))

    print("\n--- STEP 3: Testing /tasks/99 (Not Found) ---")
    r3 = client.get("/tasks/99")
    print("Status:", r3.status_code, "->", r3.data.decode("utf-8"))

    print("\n[NEXT STEP] In Module 12, we will filter tasks using query parameters (e.g. ?status=Pending)!")
