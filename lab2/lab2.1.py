MyStr = str(input("Enter the line - "))
length = len(MyStr)
mylist = list(map(str, MyStr))
for x in range(length):
    if mylist[x] == ":":
        print("colon is found")
        print("the position is ",(x + 1))
        break 

     