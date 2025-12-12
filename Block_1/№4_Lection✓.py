# Lection №8
# Task 1
a=int(input("Enter number:"))
while a<100:
    a=a+5
    print(a)
print("\n")

# Task 2
while a<0 or a>10:
    a=int(input("Enter number for 0 to 10:"))
    if a>10 or a<0:
        print("Number is out of range")

print("\n")
print("What number did the other player guess? (For 0 to 10)")
b=int(input("Enter number:"))
while a!=b:
    print("Wrong number, try again.")
    b=int(input("Enter number:"))
print("\n")
print("You guessed it!","\n")

# Task 3
a=float(1000)
print(f"Deposit amount {a}")
print("The annual percentage rate is 25%.")
b=float(input("Enter the deposit term (in years):"))
sum=a*((1.25)**b)
print(f"At the end of the term, the deposit amount will be {sum}","\n")

# Task 4
n=int(input("Enter value of n:"))
a=int(input("Enter value of a:"))
sum=n/2*(2*a+(n-1)*5)
print(f"The final value is {sum}","\n")

# Task 5
a=int(input("Enter number:"))
a=b
if a<0:
    print("The factorial of a negative number does not exist.")
if a==0 or a==1:
    print(f"The factorial of {a} is 1.")
fact=1
i=1
while i<=a:
    fact *=i
    i+=1
print(f"!{b}={fact}","\n")