#print first N natural number.
n=int(input("Enter a number: "))
for i in range(n):
    print(i,end=" ")

#Calculate factorial number using while loop
n=int(input("Enter the number: "))
f=1
i=1
while(i<=n):
    f=f*i
    i+=1
print(f"The factorial of {n} is: {f}")

#brea,continue and pass
#Break
n=int(input("Enter a number: "))
for i in range(n):
    print(i)
    if(i==4):
        print("The break statement is used.")
        break

# #Continue
n=int(input("Enter a number: "))
for i in range(n):
    if(i==4):
        continue
    print(i)
   

#pass
n=int(input("Enter a number: "))
for i in range(n):
    if(i!=4):
        pass
    else:
        print(i)

#print patterns using nested loop
a=5
for i in range(a):
    for j in range(i):
        print("*",end=" ")
    print()

#print patterns using nested loop
a=5
for i in range(a):
    for j in range(a-i):
        print("*",end=" ")
    print()

#step of 5 between 0 and 50
range(0,50,5)
for i in range(1,50,5):
    print(i)

#reverse loop
for n in range(10,0,-1):
    print(n)
    