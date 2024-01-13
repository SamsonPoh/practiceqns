# Sample Python


# Data Types
n1 = 2            # int
n2 = 100.23         # decimal
name = 'John'      # string
list1 = ['apple', 'orange', 'kiwi'] # list
dict1 = {'name': 'John Doe', 'age': 21, 'country': 'SG'} # dictionary
v1 = True           # boolean
v2 = False          # boolean
print(n1)
print(n2)
print(name)
print(list1)
print(dict1)
print(v1)
print(v2)

# Reassignment of Variable
variable = 222
print(n1)
variable = 'Brave new World'
print(n1)

## If-else Condition
example = 'Sagar'
if example == 'sagar':
    print("Success!")
else:
    print("Failed")

## If-elif-else Condition
num = 311
if num > 200:
    print("More than 200")
elif num > 100:
    print("More than 100")
else:
    print("Less than equal 100")

## While Loop
num = 10
while num < 100:
    num = num + 20
    print("Value of num: " + str(num))

## For Loop
fruits = ['apple', 'orange', 'kiwi']
for fruit in fruits:
    print(f"I like to eat {fruit}")

## For Loop
for index in range(len(fruits)):
    print(f"I grow {fruits[index]}")

## Functions
def sum_numbers(a, b):
    return a + b
n1 = 73
n2 = 32
result = sum_numbers(n1,n2)
print(f"The result of sum_numbers({n1}, {n2}) is {result}")
