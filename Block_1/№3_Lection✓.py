import math

    # Lection 5
    
#Task 1
import math
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print("a^b",math.pow(a,b))
print("b^a",math.pow(b,a))
print("a^b-1",math.pow(a,b-1))
print("b^a-1",math.pow(b,a-1))
print("(a*b)^a+b=",math.pow(a*b,a+b),"\n")

#Task 2
r=float(input("Enter the radius of the circle: "))
C=2*math.pi*r
S =math.pi*(2*r)**2
print("Circle length:",C)
print("Area of a circle:",S,"\n")

#Task 3
a=int(input("Enter number:"))
b=math.factorial(a)
print("Factorial of a given number =",b,"\n")

    # Lection 6
    
#Task 1.a
a=int(input("Enter number:"))
print("Number > 0")
if a>0:
    print("True")
else:
    print("False")
print("Number < 0")
if a<0:
    print("True")
else:
    print("False","\n")

#Task 1.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if a==b:
    print("True. Equal numbers")
else:
    print("False. Numbers are not equal")

if a>b:
    print("True. First number is greater")
else:
    print("False. First number is smaller")
    
if a<b:
    print("True. Second number is greater")
else:
    print("False. Second number is smaller")
    
if a**2>b**2:
    print("True. Square of the first number is greater than the square of the second number")
else:
    print("False. Square of the first number is less than the square of the second number")
    
if a+b>a*b:
    print("True. Sum of these numbers is greater than their product")
else:
    print("False. Sum of these numbers is less than their product","\n")

#Task 2
a=input("Enter first two numbers of ticket: ")
b=input("Enter second two numbers of ticket: ")
sum1=int(a[0])+int(a[1])
sum2=int(b[0])+int(b[1])
if sum1==sum2:
    print("Lucky ticket")
else:
    print("Unlucky ticket","\n")
    
    # Lection 7
    
#Task 1 (0;100) 
a=float(input("Enter number:"))
if 100>a>0:
    print("The number falls within the range","\n")
else:
    print("The number is not included in the range","\n")

#Task 2 [-33;150)U(151)
a=float(input("Enter number:"))
if -33<a<150 or a==151:
    print("The number falls within the range","\n")
else:
    print("The number is not included in the range","\n")

#Task 3 (-100;0)U(0;100) 
a=float(input("Enter number:"))
if -100<a<0 or 00>a>0:
    print("The number falls within the range","\n")
else:
    print("The number is not included in the range","\n")

#Task 4 if 4, 7, 2 then 2<4<7
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
# 1) a < b < c
if a < b and b < c:
    print(f"{a}<{b}<{c}")
# 2) a < b = c
elif a < b and b == c:
    print(f"{a}<{b}={c}")
# 3) a = b < c
elif a == b and b < c:
    print(f"{a}={b}<{c}")
# 4) a = b = c
elif a == b and b == c:
    print(f"{a}={b}={c}")
# 5) a < c < b
elif a < c and c < b:
    print(f"{a}<{c}<{b}")
# 6) a = c < b
elif a == c and c < b:
    print(f"{a}={c}<{b}")
# 7) b < a < c
elif b < a and a < c:
    print(f"{b}<{a}<{c}")
# 8) b < a = c
elif b < a and a == c:
    print(f"{b}<{a}={c}")
# 9) b = a < c
elif b == a and a < c:
    print(f"{b}={a}<{c}")
# 10) c < a < b
elif c < a and a < b:
    print(f"{c}<{a}<{b}")
# 11) c < a = b
elif c < a and a == b:
    print(f"{c}<{a}={b}")
# 12) b < c < a
elif b < c and c < a:
    print(f"{b}<{c}<{a}")
# 13) c < b < a
elif c < b and b < a:
    print(f"{c}<{b}<{a}")
# 14) b = c < a
elif b == c and c < a:
    print(f"{b}={c}<{a}")
# 15) c = a < b
elif c == a and a < b:
    print(f"{c}={a}<{b}")
# 16) a < c = b
elif a < c and c == b:
    print(f"{a}<{c}={b}")
print("\n")

#Task 5 Does the triangle exist?
a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
if (a+b>c) and (a+c>b) and (b+c>a):
    print("This triangle exists","\n")
else:
    print("A triangle with these sides does not exist","\n")

#Task 6 a/(x-3)=b, а and b - ? 
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
x=(a/b)+3
print("x =",x,"\n")

#Task 7 (a+b)/((x-3)*(x+2))=c, x - ?
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
if c == 0:
    print("c cannot be equal to 0.")
else:
    A=c
    B=-c
    C=-(6*c+a+b)
    D=B**2-4*A*C
    if D<0:
        print("There are no valid solutions.")
    else:
        x1=(-B+math.sqrt(D))/(2*A)
        x2=(-B-math.sqrt(D))/(2*A)
        print("Solutions to the equation:")
        print("x1=", x1)
        print("x2=", x2)