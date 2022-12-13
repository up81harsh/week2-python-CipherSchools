# split method 
# convert string to list

user_info = "harshit,19".split(",")
print(user_info)

name , age ="harshit,19".split(",")
print(name)
print(age)

name , age = input("enter your name and age : ").split(",")
print(name)
print(age)


# JOIN METHOD 
# convert list to string
user_info = ["harshit" , 24]
",".join(user_info)
print(user_info)