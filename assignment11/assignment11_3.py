#3. Accept number of rows and number of columns from user and display
#below pattern.
#Input : iRow = 3 iCol = 5
#Output :   5 4 3 2 1
#           5 4 3 2 1
#           5 4 3 2 1
n=int(input("Enter a number of rows:"))
for i in range(n):
    for j in range(n+2,0,-1):
        print(j,end=" ")
    print()    