#. Accept two numbers from user and display first number in second
#number of times.
#Input : 12 5
#Output : 12 12 12 12 12

n=int(input("Enter a first number:"))
m=int(input("Enter a second number:"))

for i in range(m):
    print(n,end=" ")
