Similarly to its mathematical definition, a set is an unordered collection of distinct elements, where the types of the elements may differ.

Sets support the `insert`, `remove`, and `contains` operations, in addition to the `union`, `intersection`, and `difference` operations.

Typically, due to the pairwise distinct and unordered nature of sets, they can utilize hash based indexing to achieve an amortized $O(1)$ time complexity. 

The `set` and `naiveset` are two implementations of the aformentioned `set` ADT. Below is a (relatively) low level implementation of a the basic `insert`, `remove`, and `contains` operations of a set using an array.

```python
class NaiveSet:
    def __init__(self):
        self._values = []
        self._size = 0
    
    def insert(self, value):
        for i in range(self._size):
            if self._values[i] == value:
                return -1
        self._values.append(value)
        self._size += 1
    
    def remove(self, value):
        found = -1
        for i in range(self._size):
            if self._values[i] == value:
                del self._values[i]
                self._size -= 1
                found = None
        return found
    
    def contains(self, value):
        found = False
        for i in range(self._size):
            if self._values[i] == value:
                found = True
        return found
```

The logic for handling the `insert`, `remove`, and `contains` operations is straightforward!  Let's look at the implementation of the other functions. 

```python
def union(set1,set2):
    union_set = NaiveSet()
    for i in range(set1._size):
        union_set.insert(set1._values[i])
    for i in range(set2._size):
        union_set.insert(set2._values[i])
    return union_set
```

The `union` function creates a new set and inserts all the elements from the two input sets into the new set. Since a set is a collection of distinct elements, we can use the `insert` function to ensure that no duplicates are added.

```python
def intersection(set1,set2):
    intersection_set = NaiveSet()
    for i in range(set1._size):
        if set2.contains(set1._values[i]):
            intersection_set.insert(set1._values[i])
    return intersection_set
```

The `intersection` function creates a new set and inserts all the elements that are common to both input sets. We can use the `contains` function to check if an element is in the second set.

```python
def difference(set1,set2):
    difference_set = NaiveSet()
    for i in range(set1._size):
        if not set2.contains(set1._values[i]):
            difference_set.insert(set1._values[i])
    return difference_set
```

The `difference` function creates a new set and inserts all the elements that are in the first set but not in the second set. We can use the `contains` function to check if an element is in the second set.


