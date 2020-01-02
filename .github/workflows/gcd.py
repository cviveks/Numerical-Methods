print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
if num1 > num2:
    rem = num1%num2
    while rem != 0:
        gcd = rem
        num1 = num2
        num2 = rem
        rem = num1%num2
    print("The greatest common divisor :"+str(gcd))
else:
    rem = num2%num1
    while rem != 0:
        gcd = rem
        num2 = num1
        num1 = rem
        rem = num2%num1
    print("The greatest common divisor :"+str(gcd))
