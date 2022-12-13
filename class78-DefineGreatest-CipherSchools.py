#DEFINE GREATEST:
def greater(a,b,c):
    if(a>b>c):
        return a
    elif (b>a>c):
        return (b)
    else:
        return c 

num1 = int(input("enter first number: ")) 
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))      
bigger = greater(num1,num2,num3) 
print(f"{bigger} is greater")        