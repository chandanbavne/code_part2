#2. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 4
#Output:    A B C D
#           a b c d
#           A B C D
#           a b c d

row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))
for i in range(1,row+1):
    for j in range(0,col):
        if(i%2!=0):
            print(chr(j+65),end=" ")
        else:
            print(chr(j+97),end=" ")
    print()
    