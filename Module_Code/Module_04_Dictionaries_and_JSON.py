"""
=============================================================================
MODULE 04: Dictionaries and JSON Thinking
Topic: The Language of Web Data Exchange (Foundation Phase)
=============================================================================
Welcome to Module 04!
In web applications, Python backends process data as Dictionaries,
but browsers, mobile apps, and frontends communicate in JSON (plain text).

What you will learn in this module:
1. Python Dictionaries (key-value data records)
2. What JSON is (JavaScript Object Notation text)
3. json.dumps() -> Serialization: Python Dictionary -> JSON String (Sending data)
4. json.loads() -> Deserialization: JSON String -> Python Dictionary (Receiving data)
=============================================================================
"""

import json

# 1. Python Dictionary (lives in Python memory)
user_data = {
    "id": 101,
    "name": "Sarah Connor",
    "skills": ["Python", "Flask", "SQL"],
    "is_admin": False
}

# =============================================================================
# 2. SERIALIZATION: Python Dict -> JSON String (json.dumps)
# =============================================================================
def convert_to_json(data):
    """Converts Python dictionary to a plain text JSON string."""
    json_string = json.dumps(data, indent=2)
    return json_string


# =============================================================================
# 3. DESERIALIZATION: JSON String -> Python Dict (json.loads)
# =============================================================================
def parse_from_json(json_text):
    """Converts a raw JSON text string into a Python dictionary."""
    data_dict = json.loads(json_text)
    return data_dict


# =============================================================================
# DEMONSTRATION
# =============================================================================
if __name__ == "__main__":
    print("--- 1. Python Dictionary ---")
    print("Data type:", type(user_data))
    print("Value:", user_data)

    print("\n--- 2. Serializing to JSON String (json.dumps) ---")
    json_result = convert_to_json(user_data)
    print("Data type:", type(json_result))
    print("JSON Text sent to web clients:\n" + json_result)

    print("\n--- 3. Deserializing from JSON String (json.loads) ---")
    incoming_client_json = '{"product": "Laptop", "price": 899.99, "in_stock": true}'
    parsed_dict = parse_from_json(incoming_client_json)
    print("Data type:", type(parsed_dict))
    print("Product Name:", parsed_dict["product"])
    print("Product Price: $", parsed_dict["price"])

    print("\n[NOTE] In Modules 01-10, we learn foundational concepts.")
    print("Our hands-on Project Implementation officially starts in Module 11!")
