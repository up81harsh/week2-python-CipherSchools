#SCOPE
x = 5    #global variable
def func():
    x = 7               #local variables
    return x
print(x)
print(func())
print(x) 
