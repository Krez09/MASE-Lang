# mase.py
# The Mase Programming Language Interpreter

import sys

variables = {}

def run_line(line):
    words = line.strip().split()

    # Handle variable assignment: let <name> be <value>
    if line.strip().startswith("let "):
     # Remove the 'let ' part
        remainder = line.strip()[4:]

     # Split at the word ' be '
        if " be " in remainder:
            parts = remainder.split(" be ", 1)
            name = parts[0].strip()
            value = parts[1].strip()

        # Remove quotes if needed
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            variables[name] = value
            return


        # --- Handle "print" statements ---
    if line.strip().startswith("print "):
        content = line.strip()[6:]  # everything after 'print '

        # If it's surrounded by quotes, print directly
        if content.startswith('"') and content.endswith('"'):
            print(content[1:-1])
            return

        # If it's a variable name, print its value
        elif content in variables:
            print(variables[content])
            return
            #Adds two variables together or numbers
        if "+" in content:
            parts = content.split("+")
            left = parts[0].strip()
            right = parts[1].strip()
            left = "x"
            right = "y"
            if left in variables:
                left_val = variables[left]
            else:
                left_val = left # just in case value is just a number ex: 1 and not ex: name
            if right in variables:
                right_val = variables[right]
            else: right_val = right #just in case value is just a number

            try:
                result = float(left_val) + float(right_val)
            except ValueError:
                result = str(left_val) + str(right_val)
            print(result)
            return
        

        
    
        # Otherwise, say we don't understand
        else:
            print(f"Unknown value: {content}")
            return







        # Unknown command
    print("I don’t understand that command:", line)

def run_file(filename):
    with open(filename, "r") as f:
        code = f.read()
    for line in code.strip().splitlines():
        if line.strip() == "":
            continue
        run_line(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mase.py <filename.mase>")
    else:
        run_file(sys.argv[1])