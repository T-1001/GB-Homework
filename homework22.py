# Task 2

elcount = int(input("Enter the number of list items "))
mylist = []
i = 0
el = 0
while i < elcount:
    mylist.append(input("Enter the next list value"))
    i += 1

for elem in range(int(len(mylist)/2)):
        mylist[el], mylist[el + 1] = mylist [el + 1], mylist[el]
        el += 2
print(mylist)


