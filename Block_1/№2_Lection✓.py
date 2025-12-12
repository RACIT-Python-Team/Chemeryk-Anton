    # Lection 3
# 1 A program that asks the user for a number and prints its integer part.
a=float(input("Enter a valid number: "))
print(int(a),"\n")

# 2 A program that asks the user for an integer and prints it with an exclamation mark at the end.
a=int(input("Enter an integer: "))
print(str(a)+"!","\n")

# 3 A program that asks the user for two numbers and print plural with them.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("These numbers form a plural:","{",a,",",b,"}","\n")

# 4 Say my name.
b=str("Heisenberg")
a=str(input("Say my name: "))
if a==b:
    print("You're goddamn right!","\n")
else:
    print("Damn fool...","\n")

    # Lection 4
    
# 1 Write result of:          
#             3
#    ( a + 2 ) - 5
#     -------
#        4
a=int(input("Enter value of a: "))
a=((((a-2)**3)/4)-5)
print("Result:",a,"\n")

# 2 Calculator for real numbers.
a=float(input("Enter a: "))
b=float(input("Enter b: "))
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)
print(b,"/",b,"=",b/a,"\n")

# 3 Finds the min and max of three numbers.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
minNumber=int(min(a,b,c))
maxNumber=int(max(a,b,c))
print("Min = ",minNumber,"Max = ",maxNumber,"\n")

# 4 Solving equations.

a=int(input("Enter vulue of a: "))
    # Equation 1: 7x-a=0
x=a/7
print("x=",x)
    # Equation 2: 45/(a*x)=3
if a !=0:
    x=15/a
    print("x=",x)
else:
    print("Division by zero is not possible.")
    # Equation 3: 4x+a*(x-1)=4
if a !=-4:
    x=(4+a)/(4+a)
    print("x=",x,"\n")
else:
    print("Division by zero is not possible.","\n")

# 5 Program will count how many integers are located between the given numbers.
    # Task 1 
num1=3.17
num2=20.56
minNum=min(num1, num2)
maxNum=max(num1, num2)
fmin=int(minNum)
fmax=int(maxNum)
count=fmax-fmin-1
print("Number of integers between",num1,"and",num2,"=",count)
    # Task 2
num1=56.5
num2=2
minNum=min(num1, num2)
maxNum=max(num1, num2)
fmin=int(minNum)
fmax=int(maxNum)
count=fmax-fmin-1
print("Number of integers between",num1,"and",num2,"=",count)
    # Task 3
num1=147.65
num2=34+45.13
minNum=min(num1, num2)
maxNum=max(num1, num2)
fmin=int(minNum)
fmax=int(maxNum)
count=fmax-fmin-1
print("Number of integers between",num1,"and",num2,"=",count,"\n")

# 6 Converting numbers to the binary number system and the hexadecimal number system.
a=int(input("Enter number: "))
x=bin(a)
y=hex(a)
print(a,"In Binary number system =",x ,"In Hexadecimal number system =",y,"\n")

# 7 Program must output the product of the text and the number.
a=str(input("Enter text:"))
b=int(input("Enter an integer:"))
print("(",a*b,")")

# 8 Complete action.
txt=str(input("Enter text:"))
a=int(input("Enter an integer: "))
print("[‘|’","+",(a*txt),"+","‘|’]")
print("[",a,"*‘!’+",txt+(a-1),"*","‘!’]")
print("[",(a*2/3+4-5)*txt,"]")