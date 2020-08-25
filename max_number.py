def max_num( num1 ,  num2 , num3):
    if(num1>num2 and num1>num3 ):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    elif(num3>num1 and num3>num2):
        return num3
    else :
        
        if(num1==num2 and num1>num3):
           return num1
        elif(num1==num3 and num1>num2):
            return num1
        elif(num2==num3 and num2>num1):
            return num2
        else :
            return 0
    


num1 = input("Enter 1st number")
num2 = input("Enter 2nd number")
num3 = input("Enter 3rd number")

max_of_them = max_num(num1,num2,num3)


if(max_of_them == num1 or max_of_them == num2 or max_of_them ==num3):
   print("Maximum is %d"  % max_of_them)
else :
    print("You entered same numbers.")    
