def greater(a,b):
    if a>b:
        return a
    return b     

def greatest(a,b,c):
    if(a>b>c):
        return a
    elif (b>a>c):
        return (b)
    else:
        return c 



#FUNCTION INSIDE FUNCTION:

# greater(a,b)----> a or b 
# greater (a or b ,c) ----> greatest

def new_greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger , c)

print(new_greatest(10,20,30))
    
