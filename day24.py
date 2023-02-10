fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = [x for x in fruits if "a" in x]

print(newList)

numbers = [5,8,6,3,1]

for i, y in enumerate(numbers):
    print(f"{y} is the number for count {i+1}")
