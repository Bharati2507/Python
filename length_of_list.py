list1 = list()
n = input("Enter no of elements")
for i in range(0,n) :
    m1 = input("Enter element")
    list1.append(m1)
c=0
for l in list1 :
     c = c+1 
print("Length of the list is %d" % c)