#4. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 5
#Output : 4 4 4 4 4
#         3 3 3 3 3
#         2 2 2 2 2
#         1 1 1 1 1

row=int(input("Enter a number of row:"))
col=int(input("Enter a number of collumn:"))

for i in range(row,0,-1):
    for j in range(col):
        print(i,end=" ")
    print()    
