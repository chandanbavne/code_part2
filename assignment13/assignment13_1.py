#1. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 4
#Output : * # # #
#         * * # #
#         * * * #
#         * * * *
row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))

for i in range(1,row+1):
    for j in range(1,col+1):
        if(j<=i):
            print('*',end=" ")
        else:
            print("#",end=" ")
    print()
