
## Priority Queue (Max Heap & Min Heap)
Here we will implement both max heap and min heap.

#### 1. Min heap (push & pop)

A simple example with normal integer list. The idea here is that the numbers will be stored in the list, but the list itself won't manage the priority or heap property. 
</br></br>
So while adding or removing items in the list we will be using a different function from heapq - so that the items in the list works like a priority queue.

```python
import heapq

# Initialization a normal list
customers = []

# adding items using heappush()
heapq.heappush(customers, 2)
heapq.heappush(customers, 4)
heapq.heappush(customers, 3)
heapq.heappush(customers, 1)

# removing items using heappop()
while len(customers) != 0:
     print(heapq.heappop(customers))

print("program ends")

# this will prints 1 -> 2 -> 3 -> 4
# then it will print 'program ends'
```


#### 2. Max heap

By default python doesn't provide any API for max heap. However we can implement that by simply multiplying the item/number with -1.
</br></br>
So, while pushing and poping a number, we have to multiply it with -1.
</br>
<b>For a better max heap implementation check 5th point</b>


#### 3. Heap peek

The first item of the list will be the peek item. You can directly access it.

```python
import heapq

# Initialization a normal list
customers = []

# adding items using heappush()
heapq.heappush(customers, 2)
heapq.heappush(customers, 4)
heapq.heappush(customers, 1)

# peeking the item
print(customers[0]) # will print 1
print(customers[0]) # will print 1
```

#### 4. Class based min heap implemenation


```python
import heapq

# A simple min heap implementation
class MinHeap:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        heapq.heappush(self.items, item)
    
    def pop(self):
        return heapq.heappop(self.items)
    
    def peek(self):
        return self.items[0]
# Ends of min heap implementation

# Initialization a normal list
heap = MinHeap()

heap.push(4)
heap.push(3)
heap.push(5)
heap.push(1)

print(heap.peek()) # print 1
print(heap.peek()) # print 1

while heap.isEmpty() == False:
    print(heap.pop()) # print 1 -> 3 -> 4 -> 5

#program ends
```


#### 5. Class based max heap implementation

```python
import heapq

# A simple min heap implementation
class MaxHeap:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        heapq.heappush(self.items, item * -1)
    
    def pop(self):
        return heapq.heappop(self.items) * -1
    
    def peek(self):
        return self.items[0] * -1
# Ends of min heap implementation

# Initialization a normal list
heap = MaxHeap()

heap.push(4)
heap.push(3)
heap.push(5)
heap.push(1)

print(heap.peek()) # print 5
print(heap.peek()) # print 5

while heap.isEmpty() == False:
    print(heap.pop()) # print 5 -> 4 -> 3 -> 1

#program ends
```


#### 6. Max heap implementation with class type items

```python
import heapq

class Student:
    def __init__(self, age, id, name):
        self.id = id
        self.age = age
        self.name = name
# End of student class implemenation

# Max heap implementation for Students
# whose age is large will be in first
# is age is same, whose id is small will be first
class MaxHeap:
    def __init__(self):
        self.studentList = []

    def isEmpty(self):
        return len(self.studentList) == 0
    
    def push(self, student):
        obj = (-student.age, student.id, student)
        heapq.heappush(self.studentList, obj)
    
    def pop(self):
        obj = heapq.heappop(self.studentList)
        return obj[2] # student object in position 2
    
    def peek(self):
        return self.studentList[0][2]
# Ends of min heap implementation

# Initialization a normal list
heap = MaxHeap()

heap.push(Student(22, 5, "gobinda"))
heap.push(Student(23, 7, "joy"))
heap.push(Student(22, 2, "bijoy"))
heap.push(Student(22, 3, "ayush"))

print(heap.peek().name) # print joy
print(heap.peek().name) # print joy

# print: joy -> bijoy -> ayush -> gobinda
while heap.isEmpty() == False:
    print(heap.pop().name)

# Program ends here
```