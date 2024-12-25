## Playing with variables

#### Total 8 types of variables.
- Numbers (Int)
- Numbers (Float)
- String
- Boolean (True, False)
- List (Mutable list)
- Tuple (Immutable list)
- Set
- Dictionary (key-value pair)


## Int
Python 3 integers are not limited by <b>32-bit or 64-bit</b> boundaries. They can grow to an arbitrary length, only limited by the available memory of your system.

```python
myage = 22
print("My age is", myage)

**Output**
My age is 22
```

## Float
Python's float type is a double-precision floating-point format, typically following the IEEE 754 standard.
- Max value: 1.79 x 10^308
- Min value: 2.22 x 10^-308

```python
myheight = 6.2
print("My heigth is", myheight)

**Output**
My heigth is 6.2
```


## String
Python string can be declared with single quote or double quote.

```python
myname = "Gobinda Paul"
print("My name is" , myname)

**Output**
My name is Gobinda Paul
```


## Bool
Careful about the spelling (True/False)

```python
areYouBengali = True
areYouCanadian = False
print("I am Bangladeshi:", areYouBengali)
print("I am Canadian:", areYouCanadian)

**Output**
I am Bangladeshi: True
I am Canadian: False
```


## Mutable list - normal list
List can store different type of items and it's resizeable.

```python
mylist = [1, 2, "hello", False, 4.6, "world"]
print("My list items are:", mylist)
print("Fist item from my list:", mylist[0])
print("Third item from my list:", mylist[2])
print("Size of my list:", len(mylist))

**Output**
My list items are: [1, 2, 'hello', False, 4.6, 'world']
Fist item from my list: 1
Third item from my list: hello
Size of my list: 6
```


## Immutable list - tuple
Tuple can store different type of items but it's not resizeable.

```python
mytuple = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print("My touple items are:", mytuple)
print("Today is:", mytuple[3])
print("My tuple size:", len(mytuple))

**Output**
My touple items are: ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
Today is: Thu
My tuple size: 7
```


## Set - Unique items
Can store different type of items as unique.

```python
mycousins = {"noyon", "bijoy", "ayush"}
print("My cousins are:", mycousins)
print("noyon is my cousin:", 'noyon' in mycousins)
print("joy is my cousin:", 'joy' in mycousins)
print("My total cousins :", len(mycousins))

**Output**
My cousins are: {'ayush', 'noyon', 'bijoy'}
noyon is my cousin: True
joy is my cousin: False
My total cousins : 3
```


## Dictionary (key-value pair)
Key/Value both could be of different types.

```python
oneUsd = {"BDT" : 120.2, "CAD" : 1.4, "INR" : 98.5}
print("One USD equivalent", oneUsd["BDT"], "Bangladeshi Taka")
print("One USD equivalent", oneUsd["CAD"], "Canadian Dollar")
print("One USD equivalent", oneUsd.get("KRW"), "Korean Won")
print("My dictionary size", len(oneUsd))

**Output**
One USD equivalent 120.2 Bangladeshi Taka
One USD equivalent 1.4 Canadian Dollar
One USD equivalent None Korean Won
My dictionary size 3
```