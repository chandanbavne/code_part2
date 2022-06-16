#3. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 3 iCol = 5
#Output :   A A A A A
#           B B B B B
#           C C C C C
row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))

for i in range(0,row+1):
    for j in range(0,col):
        
        print(chr(i+65),end=" ")
    print()    