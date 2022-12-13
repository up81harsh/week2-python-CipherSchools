# Define a function which will take list as an argument and this function will return a reversed list
# examples

#[1,2,3,4]--> [4,3,2,1]
#['word1','word2']---> ['word2', 'word1']
#Note you simply do this with reverse method or [::-1]

#but try to do this with the help of Return and append method


#ans:
numbers = [1,2,3,4]
def reverse_list(l):
    l.reverse()
    return l

print(reverse_list(numbers))    


#      or

def reverse_list(l):
    return l[::-1]

numbers = [1,2,3,4] 
print(reverse_list(numbers))   


#      or
numbers = [1,2,3,4]
popped_item = numbers.pop()

print(reverse_list(numbers))

# or
def reverse_list(l):
    r_list = []
    for i in range (2,len(1)+1):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list    