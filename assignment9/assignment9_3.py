#3.Write a program which accept number from user and display all its non factors.
#Input : 12
#Output : 5 7 8 9 10 11
#Input : 13
#Output : 2 3 4 5 6 7 8 9 10 11 12
#Input : 10
#Output : 3 4 6 7 8 9        

n=int(input("Enter a number:"))
b=[]

for i in range(1,n+1):
        if(n%i)!=0:
           b.append(i)
           
for i in b:
         print(i,end=" ")       