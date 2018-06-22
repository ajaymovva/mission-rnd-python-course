list1=input("enter string").split(" ")
print(list1[-1]+" "+" ".join(list(map(lambda x:x[::-1],list1[1:len(list1)-1])))+" "+list1[0])

