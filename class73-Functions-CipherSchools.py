#FUNCTIONS
# name = "function"
# print(len(name))

# in python we used def keyword for a function

def add_two(a,b):
    return a+b

total = add_two(5,4)    
print(total)            # OR print(add_two(5,4))


def add_two (num1,num2):
    return num1+num2

# a = int(input("enter a first number: "))
# b = int(input("enter a second number: "))
# total = add_two(a,b) 
# print(total)   


first_name = input("enter first name: ")
last_name = input("enter last name : ")
print(add_two(first_name,last_name))