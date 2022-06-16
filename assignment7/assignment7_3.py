#. Accept number from user and check whether number is even or odd    

def check(A):
    if(A>0):
        return "Even number"
    elif(A<0):
        return "Odd number"
        

n=int(input("Enter a first number:"))

result=check(n)
print(f" {n} is:",result)
