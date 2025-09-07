# AI Calculator
# Author: Your Name

import math

# Allowed names for evaluation
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

def ai_calculator():
    print("Welcome to AI Calculator!")
    print("Type 'exit' to quit.")
    
    while True:
        query = input("\nEnter your math expression (e.g., 2+3*5) or command: ")
        
        if query.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            # Evaluate math expression safely
            result = eval(query, {"__builtins__": None}, allowed_names)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    ai_calculator()
