# prefix set
A prefix data structure usually contains information about... prefixes. I.e., they will contain information about everything preceding each element. The prefix of an element defined in this context is the set of all elements that are smaller than (but not including) the element. Additionally, a prefix set can only contain one copy of each element.

# You must suppor the following operations:
- `insert(value)`: Insert a value into the prefix set.
- `remove(value)`: Remove a value from the prefix set.
- `contains(value)`: Check if a value is in the prefix set.
- `count(value)`: Return the number of elements in the prefix set that are less than `value`.
- `prefix_sum(value)`: Return the sum of all elements in the prefix set that are less than `value`.
- `prefix(value)`: Return the prefix of the value, i.e., all the elements in the prefix set that are less than `value`.

BONUS: implement the `difference`, `union`, `intersection`, and `symmetric_difference` operations.

# examples
The following is an example of the basic operations `insert`, `remove`, and `contains`.
```python
ps = PrefixSet()

ps.insert(1)
ps.insert(2)
ps.insert(3)

ps.contains(1) # True
ps.contains(2) # True
ps.contains(3) # True
ps.contains(4) # False

ps.remove(2)
ps.contains(2) # False
```

The following is an example of the `count`, `prefix_sum`, and `prefix` operations.
```python
ps = PrefixSet()

for i in range(10):
    ps.insert(i)
    temp = ps.prefix_sum(i) 

ps.count(5) # 5
ps.prefix_sum(5) # 10 (1+2+3+4)
ps.prefix(5) # [0,1,2,3,4]
```

# tips and hints
You can implement the prefix set as an extension of a sorted list. When inserting a value, you can use binary search to find the correct position. When removing a value, you can use binary search to find the value and remove it. When counting, summing, or finding the prefix, you can iterate over the list and find the values that are less than the given value.

