#1.Write a program which accept number from user and display its multiplication of
#factors.
#Input : 12
#Output : 144 (1 * 2 * 3 * 4 * 6)
#Input : 13
#Output : 1 (1)
#Input : 10
#Output : 10 (1 * 2 * 5)



n=int(input("Enter a number:"))
mult=1
i=1
while i<n:
    if(n%i==0):
          mult=mult*i
    i+=1   
print("multiplication of its factor is:",mult )
