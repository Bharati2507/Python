def is_palindrome(s):
    j = len(s)-1
    i= 0 ;
    flag = 0
    # for i in range(len(s)):
    #     print(s[i])
    # return 1
    while(i<=j):
      if(s[i]==s[j]):
        flag = 1
      else:
        flag =0
      i=+1
      j=-1
    if(flag==1):
       return 1
    else:
        return 0

input_string = raw_input("Enter string : ")
op = is_palindrome(input_string)
if(op==1):
    print("True : Entered String is pallindrome")
else:
    print("False : Entered String is not pallindrome")
    
       