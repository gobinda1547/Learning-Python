# String
String is immutable. Performing operation on them doesn't change the actual object.</br>
Instead a new object will be returned.

## declaration
we can declare string by using both single quote and double quote.
```python
str1 = 'hello'
str2 = "python"

print(str1)
print(str2)
print(len(str1))
print(len(str2))

***Output***
hello
python
5
6
```


## Slicing or substring
```python
# strings are 0 base indexd
myString = 'Hello World'

# when slicing string / making substring
# all the start index will be inclusize
# all the end index will be exclusive

aSubString = myString[2:7] # 'llo W'
print(f"[{aSubString}]") 

# didn't mention end index so length will be used
bSubString = myString[4:] # 'o World
print(f"[{bSubString}]") 

# didn't mention start index so 0 will be used
cSubString = myString[:3] # 'Hel'
print(f"[{cSubString}]") 
```


## Case conversion
```python
s = "Hello, World!"
print(s.lower())   # hello, world!
print(s.upper())   # HELLO, WORLD!
print(s.capitalize())  # Hello, world!
```


## triming or striping
```python
s = "   Hello, World!   "
print(f'"{ s.strip() }"')  # will trim both side
print(f'"{ s.lstrip() }"') # will trim left side
print(f'"{ s.rstrip() }"') # will trim right side

***Output***
"Hello, World!"
"Hello, World!   "
"   Hello, World!"
```


## Spliting and joining
```python
s = "apple, banana, cherry"
# Splitting
fruits = s.split(", ")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Joining
joined = " & ".join(fruits)
print(joined)  # Output: apple & banana & cherry
```