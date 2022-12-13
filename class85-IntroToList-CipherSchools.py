# data structures
# lists ---> ordered collection of items
# you can store anything in lists int , float , string

numbers= [1,2,3]
print(numbers)
print(numbers[2])

words =["word1","word2","word3"]
print(words)
print(words[:1])

mixed = [1,2,3,"five","six",2.3,None]
print(mixed)
print(mixed[-1])

mixed[1]="two"
print(mixed)
mixed[1]=["three","four"]
print(mixed)