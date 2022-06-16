#4. Accept number of rows and number of columns from user and display
#below pattern.
#Input : iRow = 3 iCol = 4
#Output :   * # * #
#           * # * #
#           * # * #

n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n-1):
        print('*','#',end=' ')
    print()    