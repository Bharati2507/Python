def is_member(str1,liste):
    flag=0
    for i in range(len(liste)):
        if(liste[i]==str1):
            flag=1
            break
        else:
            flag=0
    if(flag==1):
        return 1
    else:
        return 0
    
liste = list()
len_of_list = input("Enter no of elements in list ")
for i in range(0,len_of_list):
    element = raw_input("Enter element : ")
    liste.append(element)

str1 = raw_input("Enter elemnt u want to find")

op = is_member(str1,liste)
if(op==1):
    print("Element is present ")
else:
    print("Element is not present ")