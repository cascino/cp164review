Similarly to the queue, the priority queue supports the following operations: `push`, `pop`, and `peek`. The `push` operation adds an element to the priority queue, the `pop` operation removes and returns the element with the highest priority, and the `peek` operation returns the element with the highest priority without removing it. 

Dissimilarly to the queue, the order in which the elements are stored is determined entirely by the attributes of the elements themselves.

A (relatively) low level implementation of a priority queue can be done using an array. The following is an example of one. 

```python
class PriorityQueue_array():
    def __init__(self):
        self._values = []
        self._size = 0
        self._front = None
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, value):
        if self.is_empty():
            self._values.append(value)
        else:
            self._values.append(value)
            if self._values[self._front] < value:
                self._front = self._size
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        
        value = self._values[self._front]
        del self._values[self._front]
        self._size -= 1
        if size == 0:
            self._front = None
        else:
            self._set_front()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        return self._values[self._front]
    
    def _set_front(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        temp = self._values[0]
        for i in range(1, self._size):
            if self._values[i] > temp:
                temp = self._values[i]
                self._front = i
```

The `PriorityQueue_array` class maintains an array of values and a pointer to the front of the queue. 