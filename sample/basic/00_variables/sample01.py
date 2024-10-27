
# variable type #1
# simple integer
myage = 22
print("My age is", myage)


# variable type #2
# simple float
myheight = 6.2
print("My heigth is", myheight)


# variable type #3
# simple string
myname = "Gobinda Paul"
print("My name is" , myname)


# variable type #4
# simple bool
areYouBengali = True
areYouCanadian = False
print("I am Bangladeshi:", areYouBengali)
print("I am Canadian:", areYouCanadian)


# variable type #5
# mutable list - normal list
mylist = [1, 2, "hello", False, 4.6, "world"]
print("My list items are:", mylist)
print("Fist item from my list:", mylist[0])
print("Third item from my list:", mylist[2])
print("Size of my list:", len(mylist))


# variable type #6
# immutable list - tuple
mytuple = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print("My touple items are:", mytuple)
print("Today is:", mytuple[3])
print("My tuple size:", len(mytuple))


# variable type #7
# Dictionary: key-value pair
oneUsd = {"BDT" : 120.2, "CAD" : 1.4, "INR" : 98.5}
print("One USD equivalent", oneUsd["BDT"], "Bangladeshi Taka")
print("One USD equivalent", oneUsd["CAD"], "Canadian Dollar")
print("My dictionary size", len(oneUsd))