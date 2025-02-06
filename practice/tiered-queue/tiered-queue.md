# tiered-queue
The Tiered Priority Queue (TPQ) is a priority queue variant that categorizes elements into discrete tiers, each representing a fixed priority level. Unlike a conventional priority queue that orders all elements in a single sorted order, TPQ groups elements by tier, where each tier is internally managed (for example, with an array or circular buffer) and the tiers themselves are linearly ordered. 

# operations
You must support the following operations:
- `push(tier, value)`: Add the element `value` to the tier `tier`.
- `pop()`: Remove and return the element with the highest priority. 
- `peek()`: Return the element with the highest priority without removing it. 
- `shift(tier, target)` : Move all elements from the tier `tier` to the tier `target`. 
- `pop(tier)`: Remove and return the element with the highest priority from the tier `tier`. 
- `peek(tier)`: Return the element with the highest priority from the tier `tier` without removing it. 
- `split(tier, key, target)` : Move all elements from the tier `tier` with a value less than `key` to the tier `target`. 

Note that in python, classes can have multiple methods with the same name, as long as they have different arguments.

# examples
The following is an example of the basic operations
```python
tpq = TieredPriorityQueue()

tpq.push(1, 10)
tpq.push(2, 20)
tpq.push(1, 15)
tpq.push(3, 25)

tpq.pop() # 25
tpq.pop() # 20
tpq.pop() # 15
tpq.pop() # 10
```

```python
tpq = TieredPriorityQueue()

for i in range(10):
    tpq.push(1, i)
    tpq.push(2, 2*i)
    tpq.push(3, 3*i)

tpq.shift(1, 2) # move all elements from tier 1 to tier 2
tpq.split(2, 10, 1) # move all elements from tier 2 with value less than 10 to tier 1

# pop from each tier
for i in range(5):
    tpq.pop(3)
    tpq.pop(2) 
    tpq.pop(1)
```

# tips and hints
The tiered priority queue can be implemented using nested lists. To keep track of the tiers, you can put the tiers in a list of the form `[tier,values]`. You can approach the tiers by implementing the sorted pattern, or by iterating over the list each time. 

When using `pop`, `peek`, and `shift`, you can iterate over the tiers and find the highest priority element. When using `split`, you can iterate over the tier and move the elements to the target tier.



# implementation
```python
class TieredPriorityQueue():
    def __init__(self):
        self.tiers = []
    
    def push(self, tier, value):
        pass
    
    def pop(self):
        pass
    
    def peek(self):
        pass
    
    def shift(self, tier, target):
        pass
    
    def pop(self, tier):
        pass
    
    def peek(self, tier):
        pass
    
    def split(self, tier, key, target):
        pass
```


