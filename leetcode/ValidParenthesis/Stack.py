from collections import deque

class Stack():
    def __init__(self) -> None:
        self.__stack = deque()
    
    def push(self, value):
        self.__stack.append(value)
    
    def pop(self):
        if len(self.__stack) > 0:
            return self.__stack.pop()
        else: 
            return None
    
    def peek(self):
        if len(self.__stack) > 0:
            return self.__stack[-1]
        else: 
            return None

    def size(self):
        return len(self.__stack)

    def print(self):
        for s in self.__stack:
            print(s)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    
    s.print()
    
    s.pop()
    s.print()
    
    s.pop()
    s.print()
