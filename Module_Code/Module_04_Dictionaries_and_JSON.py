"""
=============================================================================
MODULE 04: Dictionaries and JSON Thinking
Project Story: Building our "Task Manager" from Scratch (Step 4)
=============================================================================
Previously in Module 03:
We represented tasks as Python classes and converted them to dictionaries.

Now in Module 04:
Web browsers, React frontends, and mobile apps do NOT understand Python objects.
They exchange data using JSON (JavaScript Object Notation), which is plain text.

What you will learn in this module:
1. json.dumps() -> Converts a Python dictionary into a JSON text string (Sending data)
2. json.loads() -> Converts a JSON text string into a Python dictionary (Receiving data)
3. The complete Request-Response JSON cycle of an API

Next Module Connection:
In Module 05, we will learn about Python Decorators, which Flask uses
extensively for defining web routes (@app.route)!
=============================================================================
"""

import json

# Sample tasks in Python dictionary format (like we made in Module 03)
my_tasks = [
    {"id": 1, "title": "Learn JSON basics", "status": "Completed"},
    {"id": 2, "title": "Connect Frontend to Flask", "status": "Pending"}
]

# =============================================================================
# 1. SERIALIZATION: Python Data -> JSON String (Sending to Frontend)
# =============================================================================
def send_tasks_as_json():
    """
    json.dumps() takes Python data (list/dict) and turns it into a JSON string.
    In Flask, the function jsonify() does this automatically!
    """
    json_string = json.dumps(my_tasks, indent=2)
    return json_string


# =============================================================================
# 2. DESERIALIZATION: JSON String -> Python Data (Receiving from Frontend)
# =============================================================================
def receive_new_task_from_client(incoming_json_string):
    """
    json.loads() takes raw JSON text sent by a client and turns it into
    a Python dictionary so our backend can process it.
    """
    task_dict = json.loads(incoming_json_string)
    task_dict["id"] = len(my_tasks) + 1
    my_tasks.append(task_dict)
    return task_dict


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    print("--- STEP 1: Converting Python Tasks to JSON String (dumps) ---")
    json_output = send_tasks_as_json()
    print("Data formatted as JSON text:")
    print(json_output)

    print("\n--- STEP 2: Receiving a New Task from Client JSON (loads) ---")
    # Simulating what a browser or Postman sends to our server:
    incoming_data = '{"title": "Learn Flask Routes", "status": "Pending"}'
    print("Raw text received from client:", incoming_data)

    new_task = receive_new_task_from_client(incoming_data)
    print("Parsed into Python dictionary and added:", new_task)

    print(f"\nTotal tasks in our list now: {len(my_tasks)}")

    print("\n[NEXT STEP] In Module 05, we will learn Decorators before starting Flask!")
