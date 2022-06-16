
#2. Write a program which accept number from user and print  factors of that
#number.
#Input : 24
#Output:  2 4 6 8 12      

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if(n%i==0):
        
            print(i,end="  ")
print()        
