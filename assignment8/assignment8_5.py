#5. Accept on character from user and check whether that character is vowel
#(a,e,i,o,u) or not.
#Input : E Output : TRUE
#Input : d Output : FALSE        


ch=input("Enter a character:")
if ch in('a','e','i','o','u','A','E','I','O','U'):
    print('True')
else:
     print("False")