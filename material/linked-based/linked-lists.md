# Linked Lists

Linked lists use many methods including: `push`, `append`, `pop`, `peek`, `remove`, `find`, `is_empty`, `length`.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def pop(self):
        if not self.head:
            return -1
        val = self.head.val
        self.head = self.head.next
        return val
    
    def peek(self):
        if not self.head:
            return -1
        return self.head.val
    
    def remove(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next
    
    def find(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def is_empty(self):
        return self.head is None
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

```

