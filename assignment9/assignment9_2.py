#2.Write a program which accept number from user and display its factors in
#decreasing order.
#Input : 12
#Output : 6 4 3 2 1

n=int(input("Enter a number:"))
b=[]
i=1
while i<n:
      if(n%i)==0:     
            b.append(i)
      i+=1
for i in b:
     print(i)
     
b.reverse()     
print("revers of b is:",b)      

#slicing of list
#c=b[1:3]
#print(c)