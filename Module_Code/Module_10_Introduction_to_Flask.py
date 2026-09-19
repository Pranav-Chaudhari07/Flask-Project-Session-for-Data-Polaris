"""
=============================================================================
MODULE 10: Introduction to Flask
Project Story: Building our "Task Manager" Web App (Step 7)
=============================================================================
Welcome to Day 2!
Having learned Python foundations (Day 1) and Web HTTP theory (Modules 7-9),
we now write our VERY FIRST FLASK WEB APPLICATION!

What you will learn in this module:
1. What Flask is (a micro web framework in Python)
2. Creating the Flask app instance: app = Flask(__name__)
3. Defining your first web routes using the @app.route() decorator
4. Returning HTML text to a browser
5. Understanding Debug Mode (debug=True)

Next Module Connection:
In Module 11, we will add dynamic routes (like /tasks/<int:task_id>)
so users can view specific tasks!
=============================================================================
"""

from flask import Flask

# 1. Create the Flask application instance
# __name__ tells Flask where to look for resources
app = Flask(__name__)


# =============================================================================
# 2. DEFINING OUR FIRST WEB ROUTES
# =============================================================================

@app.route("/")
def home():
    """
    When a user visits http://127.0.0.1:5000/
    Flask runs this function and displays the HTML in the browser.
    """
    return "<h1>Welcome to Task Manager!</h1><p>Our Flask backend is live!</p>"


@app.route("/about")
def about():
    """
    When a user visits http://127.0.0.1:5000/about
    """
    return "<h2>About TaskFlow</h2><p>A simple, beginner-friendly task tracker built with Flask.</p>"


# =============================================================================
# 3. RUNNING OUR FLASK APP
# =============================================================================
if __name__ == "__main__":
    print("--- Starting our First Flask App ---")
    print("1. Visit http://127.0.0.1:5000/ for Homepage")
    print("2. Visit http://127.0.0.1:5000/about for About page")
    print("\nPress Ctrl+C in terminal to stop the server.")

    # debug=True automatically reloads the server when you make changes to code!
    # To run the live web server, uncomment the line below:
    # app.run(debug=True, port=5000)

    # Automated test of routes for quick verification:
    client = app.test_client()
    print("\nAutomated test of GET / :", client.get("/").data.decode("utf-8").strip())
    print("Automated test of GET /about :", client.get("/about").data.decode("utf-8").strip())
    print("\n[NEXT STEP] In Module 11, we will add dynamic routes to view specific tasks!")
