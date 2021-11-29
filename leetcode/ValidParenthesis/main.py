from Stack import Stack

def valid_parenthesis(s : str) -> bool:
    # valid_chars = ["(", ")", "[", "]", "{", "}"]
    valid_chars = ["(", "[", "{"]
    valid_combinations = {"(": ")",
                          "[": "]",
                          "{": "}",}
    
    stack = Stack()
    
    for ch in s:
        # if ch not in valid_chars:
        #     return False
        if ch in valid_chars:
            stack.push(ch)
            continue
        elif (stack.peek() is not None) and (valid_combinations[stack.pop()] == ch):
            continue
        else:
            return False

    if stack.size() > 0:
        return False
        
    return True


if __name__ == '__main__':
    print(valid_parenthesis("(((") == False)
    print(valid_parenthesis(")") == False)
    print(valid_parenthesis("") == True)
    print(valid_parenthesis("()") == True)
    print(valid_parenthesis("(]") == False)
    print(valid_parenthesis("()[]{}") == True)
    print(valid_parenthesis("([)]") == False)
    print(valid_parenthesis("{[]}") == True)