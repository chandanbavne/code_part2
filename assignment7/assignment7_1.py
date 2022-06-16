#1. Accept one number from user if number is less than 10 then print
#“Hello” otherwise print “Demo”.

def check(A):
    if(A<10):
        return "Hello"
    else:   
        return "Demo"


n=int(input("Enter a number:"))

result=check(n)
print(result)
