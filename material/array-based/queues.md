The queue ADT supports several methods, notably `push`, `pop`, and `peek`, all in $O(1)$ time complexity. A (relatively) low level implementation of a queue can be done using an array. The following is an (faulty) example of one. Can you spot the issue?


```python
class Queue_array():
    def __init__(self):
        self._values = []
        self._size = 0
    
    def push(self, value):
        self._values.append(value)
        self._size += 1
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._values[0]
    
    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self._size -= 1
        return self._values.pop(0)
```

While functionally, the `Queue_array` class works as expected, this implementation does not achieve the desired time complexity as described in the ADT.

> Test the differences between the implementations using the `time` library and a large input size $(>10^7)$

Trade offs are particularly common in data structures. For example, the `list` data structure in python accomplishes $O(1)$ appending, popping, and indexing, it loses out under the hood because it must be dynamically sized and incurs more cost overhead.

One particular way to accomplish the desired operations is to use a pointer approach. We will maintain an index pointing to the front of the queue and another pointing to the back. This way, we can achieve $O(1)$ time complexity for all operations.

```python
class Queue_array():
    def __init__(self):
        self._values = []
        self._size = 0
        self._front = 0
        self._back = 0
    
    def push(self, value):
        self._values.append(value)
        self._size += 1
        self._back += 1
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._values[self._front]
    
    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self._size -= 1
        self._front += 1
        return self._values[self._front - 1]
    
    def is_empty(self):
        return self._size == 0
```

There is another issue here. Can you spot it? 

> Test the differences between the implementations using the `tracemalloc` library and a large input size $(>10^7)$. 

While we have achieved the desired time complexity, we retain useless information about the queue. Since `front` is monotonically increasing, we never need, nor can access the data that is in front of this index. We can fix this by using a circular buffer.

```python
class Circular_Queue():
    def __init__(self, capacity):
        self._values = [None] * capacity
        self._size = 0
        self._front = 0
        self._back = 0
        self._capacity = capacity
    
    def push(self, value):
        if self._size == self._capacity:
            raise Exception("Queue is full")
        self._values[self._back] = value
        self._size += 1
        self._back = (self._back + 1) % self._capacity
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._values[self._front]
    
    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self._size -= 1
        value = self._values[self._front]
        self._front = (self._front + 1) % self._capacity
        return value
    
    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        return str(self._values[self._front:] + self._values[:self._front])
    
    def __len__(self):
        return self._size
```

This implementation achieves the desired time and space complexities, at the cost of having to manage the circular buffer.
