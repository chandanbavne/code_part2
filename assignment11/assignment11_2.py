#2. Accept number of rows and number of columns from user and display
#below pattern.
#Input : iRow = 4 iCol = 3
#Output :   1 2 3
#           1 2 3
#           1 2 3
#           1 2 3
n=int(input("Enter a number of rows:"))
for i in range(n):
    for j in range(1,n):
        print(j,end=" ")
    print()    