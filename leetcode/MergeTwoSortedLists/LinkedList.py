class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,):
        self.head = None
        self.size = 0
    
    def add(self, val) -> None:
        if self.head is None:
            self.head = Node(val)
            self.size += 1
            return
        
        current = self.head
        while (current.next is not None):
            current = current.next
        current.next = Node(val)
        self.size += 1
        return
    
    def remove(self, val) -> None:
        pass
    
    def get(self, idx) -> Node:
        assert self.size < idx, "Index out of range"
    
        current = self.head
        for _ in range(1, idx+1):
            current = current.next
        
        return current.val
    
    def print(self,) -> None:
        current = self.head
        while (current != None):
            print(current.val)
            current = current.next
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(6)
    ll.add(4)
    ll.add(5)
    
    ll.print()
    
    print(ll.get(4))