def reverse(str1):
    rev = ""
    for i in range(len(str1),0,-1):
        rev = rev+str1[i-1]
    return rev

str1 = raw_input("Enter String")
str2 = str1[::-1]
print(str2)
print(reverse(str1))
print(str1[1::-1])