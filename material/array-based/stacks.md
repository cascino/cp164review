The stack ADT supports several methods, notably `push`, `pop`, and `peek`, all in $O(1)$ time complexity. A (relatively) low level implementation of a stack can be done using an array. The following is an example of one with a fixed capacity.

```python
class Stack_array():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.size = 0

    def push(self, value):
        if self.size == self.capacity:
            return -1
        self.stack[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        self.size -= 1
        return self.stack[self.size]

    def peek(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return str(self.stack[:self.size])
    
    def __len__(self):
        return self.size
```

A more familiar implementation of a stack that uses the built in list data structure is as follows:

```python
class Stack_array():
    def __init__(self):
        self._values = []
        self._size = 0
    
    def push(self, value):
        self._values.append(value)
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self._size -= 1
        return self._values.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._values[-1]
    
    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        return str(self._values)
    
    def __len__(self):
        return self._size
```

Stacks are often used in conjunction with other data structures or algorithms, such as in the implementation of a depth-first search (DFS) algorithm (not formally introduced in lecture). 

# examples

## Balanced Parentheses
Given a string of parentheses, determine if the parentheses are balanced. For example, the string `"(())"` is balanced, while the string `"(()"` is not. 

```python
def is_balanced_parentheses(s):
    stack = Stack_array(len(s))
    for c in s:
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
```

## Reverse a String
Given a string, reverse it using a stack. You must accomplish this by using exactly one stack. 

```python
def reverse_string(s):
    stack = Stack_array(len(s))
    for c in s:
        stack.push(c)
    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop()
    return reversed_s
```

## Evaluate Postfix Expression
Given a postfix expression, evaluate it. For example, given the postfix expression `["2", "3", "+", "4", "*"]`, the result is `20`. 

```python
def postfix(string):
    l = string.split()
    sta = []
    ops = ['+',"-",'/','*']
    for t in l:
        if not t.isnumeric():
            b = sta.pop()
            a = sta.pop()
            s = [a+b,a-b,a/b,a*b]
            for i in range(4):
                if ops[i] == t:
                    t = s[i]
        sta.append(int(t))
    return sta[-1]
```

