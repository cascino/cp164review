# class
In many programming languages, classes define the attributes and methods that an instance of it will have. 

> an object is a specific instance of a class.

In Python, classes are defined using the `class` keyword. 

```python
class BarnAnimal:
    self.name = "Barn Animal"
```

# magic functions
there are some special functions that have a more than usual functionality. The most important of which is the `__init__` function. 

```python
class BarnAnimal:
    def __init__(self, name):
        self.name = name
```

> `__init__` is called when an instance of the class is created.

Attributes are accessible via the `class.attribute` syntax. 

```python
dolphin = BarnAnimal("Dolphin")
print(dolphin.name) # Dolphin
```

> `self` is a reference to the instance of the class.

Similar to attributes, you may also define functions within the class. 

```python
class BarnAnimal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says 'moo'")
```

It helps to think of a data structure as an object instance of a class. A problem or algorithm that requires a certain set of operations with specifications and constraints is called an abstract data type (ADT).

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self.build(left, start, mid)
            self.build(right, mid + 1, end)
            self.tree[node] = self.tree[left] + self.tree[right]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        left_sum = self.query(left, start, mid, l, r)
        right_sum = self.query(right, mid + 1, end, l, r)
        return left_sum + right_sum
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            if start <= idx <= mid:
                self.update(left, start, mid, idx, val)
            else:
                self.update(right, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left] + self.tree[right]
    
    def add(self, idx, val):
        self.update(0, 0, len(self.arr) - 1, idx, self.arr[idx] + val)
    
    def set(self, idx, val):
        self.update(0, 0, len(self.arr) - 1, idx, val)
    
    def delete(self, idx):
        self.update(0, 0, len(self.arr) - 1, idx, 0)
        build(0, 0, len(self.arr) - 1)
```