students = ["Kaisamba", "Foday", "Sharon"]
print(students)

# Accessing items in list by their index
print(f"my best friend is {students[0]}")
print(f"my best friend is {students[1]}")
print(f"my best friend is {students[2]}")

# get the index of an item in a list
print(students.index("Kaisamba"))
print(students.index("Sharon"))

# know the number of item in a list
print(f"The total items in the list is: {len(students) } ")

# Add items to a list
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]
print(students)
students.insert(4, "Donald")
print(students)

fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

 # Removing an item from a list
fruits.remove("Mango")
print(fruits)


students.pop()
students.pop()
thirditem = students.pop()
print(students)