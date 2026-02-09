def is_paired(text):
    stack = []
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in text:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack:
                return False
            if stack.pop() != matching[char]:
                return False
    if len(stack) == 0:
        return True
    return False
