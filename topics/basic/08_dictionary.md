
## Dictionary (key-value pair)
Key/Value both could be of different types.
Internally maintain the item's order according to their arrival.

#### 1. Initialization, length

```python
# declaring a non empty dictionary
myDict = {"BDT" : 120.2, "CAD" : 1.4, 5: 10, 8: "c"}
print("myDict:", myDict)
print("myDict length:", len(myDict))

#declaring empty dictionary
emptyDict = {}
print("EmptyDict:", emptyDict)
print("EmptyDict length:", len(emptyDict))

**Output**
myDict: {'BDT': 120.2, 'CAD': 1.4, 5: 10, 8: 'c'}
myDict length: 4
EmptyDict: {}
EmptyDict length: 0
```

#### 2. Getters

```python
my_dict = {'a': 1, 'b': 2}

# accessing - existing key
print("a = ", my_dict['a']) # prints 1
print("b = ", my_dict.get('b')) # prints 2

# accessing - non existing key
print("x = ", my_dict['x']) # crash
print("x = ", my_dict.get('x')) # prints None

# accessing with default value - Existing key
value1 = my_dict.get('a', 5)  # Returns 1 (value of 'a')
print(value1)

# accessing with default value - Non existing key
value2 = my_dict.get('d', 0)  # Returns 0 (default value)
print(value2)
```

#### 3. Setters

```python
# setting values when initialization
my_dict = {'a': 1, 'b': 2}

# setting values later
my_dict['c'] = 3  # Adds a new key 'c' with value 3
my_dict['a'] = 10 # Updates the value of key 'a' to 10

print("my_dict = ", my_dict)

**Output**
my_dict =  {'a': 10, 'b': 2, 'c': 3}
```

#### 4. Loop Through Both Keys and Values

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using items() to loop through both keys and values
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
```

#### 5. Loop Through Only Keys

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using keys() to loop through only keys
for key in my_dict.keys():
    print(f"Key: {key}")
```

#### 6. Loop Through Only Values

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using values() to loop through only values
for value in my_dict.values():
    print(f"Value: {value}")
```

#### 7. Loop Through Only Values

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using values() to loop through only values
for value in my_dict.values():
    print(f"Value: {value}")
```

#### 8. sorting
Though dictionary can have different types of keys and values. But be mindful that if your dictionary has different type of keys (ie: Integer and String) then the keywise sorting will be resulted a crash. Same rules go for value wise sorting.

```python
my_dict = {'b': 6, 'a': 7, 'c': 5}

# by default sorting will be keywise
sorted_items = sorted(my_dict.items())
sorted_dict = dict(sorted_items)
print("Keywise sorting:", sorted_dict)

# manual valuewise sorting
sorted_items = sorted(my_dict.items(), key=lambda item:item[1])
sorted_dict = dict(sorted_items)
print("Valuewise sorting:", sorted_dict)
```