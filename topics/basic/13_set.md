# Set

Set is a data structure which contains unique items. These unique items could be of different types (number, string, boolean).

## Basic use of set

```python
# declaring the set with empty values
# using {} will make it as dictionary
# so, don't use {} for set declaration
my_set = set()

# adding and removing
my_set.add(3) # adding new item
my_set.add(5) # adding new item
my_set.add(6) # adding new item
my_set.add(5) # adding duplicate item
my_set.discard(6) # removing existing item
my_set.discard(7) # removing unknown item

# printing the length and the set itself
print("Length of my set:", len(my_set))
print("Set value:", my_set)

# checking if set contains an item
print("Does set contains 5:", 5 in my_set)
print("Does set not contains 6:", 6 not in my_set)


***Output***
Length of my set: 2
Set value: {3, 5}
Does set contains 5: True
Does set not contains 6: True
```

## printing all the items using for loop
```python
# declaring the set with some initial values
my_set = {1,2,3,6}

# printing all the items using for loop
for item in my_set:
    print(item)


***Output***
1
2
3
6
```

## Array to set conversion
```python
my_list = [1, 2, 2, 3, 4, 4, 5]

# converting list to set
unique_set = set(my_list)
print("Set value:", unique_set)

# Clear all from set
unique_set.clear()
print("Set value:", unique_set)


***Output***
Set value: {1, 2, 3, 4, 5}
Set value: set()
```