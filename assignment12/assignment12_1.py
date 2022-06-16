#1. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 4
#Output :   A B C D
#           A B C D
#           A B C D
#           A B C D

n=int(input("Enter a number of rows:"))
m=int(input("Enter a number of column:"))

for i in range(n):
    for j in range(0,m):
        print(chr(j+65),end=" ")
    print()    