"""
=============================================================================
MODULE 03: Object-Oriented Programming (OOP) for Backend
Project Story: Building our "Task Manager" from Scratch (Step 3)
=============================================================================
Previously in Module 02:
We used basic dictionaries to represent tasks.

Now in Module 03:
In real backend development, data records are modeled as Python CLASSES.
A class allows us to bundle data (attributes) and actions (methods) together.

What you will learn in this module:
1. Defining a Class (class Task:)
2. The __init__() constructor to set initial values (id, title, status)
3. Adding methods to update state (mark_completed())
4. Converting an object to a dictionary (to_dict()) for web responses

Next Module Connection:
In Module 04, we will learn how to convert our Task objects into JSON
so that web browsers and mobile apps can communicate with our backend!
=============================================================================
"""

class Task:
    """
    Represents a single Task in our Task Manager.
    """
    def __init__(self, task_id, title, status="Pending"):
        # Instance attributes (data stored on the object)
        self.id = task_id
        self.title = title
        self.status = status

    def mark_completed(self):
        """Action/Method: changes the task status to 'Completed'."""
        self.status = "Completed"
        print(f"Task #{self.id} ('{self.title}') marked as Completed!")

    def to_dict(self):
        """
        Converts the object into a simple Python dictionary.
        This is crucial for web APIs when sending data over the internet.
        """
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status
        }


# =============================================================================
# RUNNING AND TESTING OUR CODE
# =============================================================================
if __name__ == "__main__":
    print("--- STEP 1: Creating Task Objects ---")
    task1 = Task(1, "Learn Object-Oriented Programming")
    task2 = Task(2, "Prepare for Flask Introduction")

    print(f"Task 1 created: ID={task1.id}, Title='{task1.title}', Status='{task1.status}'")
    print(f"Task 2 created: ID={task2.id}, Title='{task2.title}', Status='{task2.status}'")

    print("\n--- STEP 2: Calling Methods to Update State ---")
    task1.mark_completed()
    print("Task 1 status after method call:", task1.status)

    print("\n--- STEP 3: Converting Objects to Dictionaries ---")
    print("Task 1 dict:", task1.to_dict())
    print("Task 2 dict:", task2.to_dict())

    print("\n[NEXT STEP] In Module 04, we will convert these task dictionaries into JSON!")
