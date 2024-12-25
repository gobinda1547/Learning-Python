# Deque


## Basic operation
As the name suggested - it can insert and delete items from both ends.</br>
All the deque related operations are O(1) complexity. 

```python
from collections import deque

# Create a deque
dq = deque()
dq.append(10)        # [10]
dq.append(20)        # [10, 20]
dq.append(30)        # [10, 20, 30]
print("Initial:", dq)

# Append and remove elements
dq.append(40)        # [10, 20, 30, 40]
dq.appendleft(5)     # [5, 10, 20, 30, 40]
dq.pop()             # [5, 10, 20, 30]
dq.popleft()         # [10, 20, 30]
print("After op:", dq)

# size of the deque
print("Size:", len(dq)) # 3

# clear all the items
dq.clear()
print("Size:", len(dq)) # 0

***Output***
Initial: deque([10, 20, 30])
After op: deque([10, 20, 30])
Size: 3
Size: 0
```

## Create a deque from array

```python
from collections import deque

# Create a deque from an array
myArray = [7, 3, 9]
myDeque = deque(myArray)
print("current state:", myDeque)

***Output***
current state: deque([7, 3, 9])
```