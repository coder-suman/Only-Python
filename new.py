# even or odd
a=int(input("Enter a number: "))
if(a%2==0):
    print(a,"ia an even number")
else:
    print(a,"is an odd number")

#check positive negetive or zero
b=int(input("Enter a number: "))
if(b<0):
    print(b,"is a negetive number")
elif(b>0):
    print(b,"is a positive number")
else:
    print("The number is Zero")

#greatest among three number
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if((num1<num2) and (num2>num3)):
    print(num2 ," is greater")
elif((num2<num3) and (num3>num1)):
    print(num3 ,"is greater")
else:
    print(num1 ,"is greater")

#leap yearor not
year=2020
if((year%4)==0 and (year %100!=0)) or (year%400 ==0):
    print(year,"is a leap year")
else:
    print(year," is not a leap year")

#student gread calculetor
marks=int(input("Enter your marks: "))
percent= (marks/600)*100
print(percent)
if(percent>85):
    print("A grade.")
elif(percent<=85 and percent>=75):
    print("B grade")
elif(percent<75 and percent>=50):
    print("C grade")
elif(percent<50 and percent>=30):
    print("D grade")
elif(percent<30):
    print("Fail")