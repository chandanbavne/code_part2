#3. Write a program which accept number from user and print even factors of that number.
#Input : 36
#Output: 2 6 12 18


n=int(input("Enter a number:"))
for i in range(1,n+1):
    if(n%i==0):
        if(i%2==0):
            print(i,end="  ")
print()        
