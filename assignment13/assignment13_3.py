#3. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 5 iCol = 5
#Output : $ * * * *
#         * $ * * *
#         * * $ * *
#         * * * $ *
#         * * * * $

row=int(input("Enter anumber of rows:"))
col=int(input("Enter anumber of column:"))
for i in range(row):
    for j in range(col):
        if(i==j):
            print('$',end=" ")
        else:
            print("*",end=" ")
    print()        