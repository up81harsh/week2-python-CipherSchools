# break and continue keyword

# break : it is used to break a loop

#1 to 10 print
for i in range (1,11):
    if i ==5:
        break
    print(i)


#continue keyword
#print 1 to 10 , but not 5
#1,2,3,4,6,7,8,9,10
for i in range (1,11):
    if i ==5:
        continue
    print(i)
    