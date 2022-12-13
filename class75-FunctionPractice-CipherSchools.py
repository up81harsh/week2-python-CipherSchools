#FUNCTION PRACTICE 
def last_char(name):
    return(name[-1])

a =input("enter your name : ")    
print(last_char(a))




def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"   

print(odd_even(10))     

       # OR


def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"

print(odd_even(10))        

#2.

def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(9))

      #OR

def is_even(num):           # num is parameter
    return num%2==0     

print(is_even(9))           # 9 is arguement


#3.
def song():
    return "happy birthday song"

print(song())    

    