The sorted set is a data structure that maintains a sorted collection of unique elements. The sorted set supports the following operations: `insert`, `remove`, and `contains`. 

However, since the set is sorted, there is a particular property that allows for a more efficient implementation of the `contains` operation, but at the cost of a slower implementation of the `insert` and `remove` operations.

Here is an implementation of the sorted set using an array:

```python
class SortedSet_array():

    def __init__(self):
        self._values = []
        self._size = 0
    
    def _binary_search(self, key):
        left = 0
        right = self._size - 1
        while left <= right:
            mid = (right-left)//2 + left

            if key > self._values[mid]:
                left = mid + 1
            else:
                high = mid
            
        return left

    def insert(self, value):
        index = self._binary_search(value)
        if index < self._size and self._values[index] == value:
            return -1
        else:
            self._values.append(None)
            for i in range(self._size, index, -1):
                self._values[i] = self._values[i-1]
            self._values[index] = value
            self._size += 1

    def remove(self, value):
        index = self._binary_search(value)
        if index < self._size and self._values[index] == value:
            for i in range(index, self._size-1):
                self._values[i] = self._values[i+1]
            self._size -= 1
        else:
            return -1

    def contains(self, value):
        index = self._binary_search(value)
        return index < self._size and self._values[index] == value 
```

