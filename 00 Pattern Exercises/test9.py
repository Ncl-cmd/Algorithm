def isValid(s: str) -> bool:
    # Hash map to instantly look up corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # If the character is a closing bracket
        if char in mapping:
            # Pop the top element from stack if not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'

            # The popped opening bracket must match the required one
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0


# Testing the example
print(isValid("()"))  # Output: True
