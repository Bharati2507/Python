def sum_f(lst):
    sum = 0
    for i in lst:
        sum = sum+i
    return sum

def mul_f(lst):
    mul=1;
    for i in lst:
        mul = mul*i
    return mul

n = input("Enter number of elements : ")
element = list()
for i in range(0,n):
      j = input("Enter element : ")
      element.append(j)
res_sum = sum_f(element)
res_mul = mul_f(element)
print("SUM is " + repr(res_sum) + " and MUL is " +  repr(res_mul))
    
