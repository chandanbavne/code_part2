#5. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 3 iCol = 4
#Output :1  2   3   4
#        5  6   7   8
#        9  10  11  12

row=int(input("Enter a number of row:"))
col=int(input("Enter a number of column:"))
for i in range(row):
    for j in range(1,col+1):
        print(j+i*4,end=" ")
    print()
