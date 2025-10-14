# mase.py
# The Mase Programming Language Interpreter

import sys

variables = {}

def run_line(line):
    words = line.strip().split()

    # Handle variable assignment: let x be something
    if len(words) >= 4 and words[0] == "let" and words[2] == "be":
        name = words[1]
        value = " ".join(words[3:])
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]  # remove quotes
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