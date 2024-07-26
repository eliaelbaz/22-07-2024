# 7
num1: int = int(input("Enter the first number: "));
num2: int = int(input("Enter the second number: "));
a, b = num1, num2;
while b != 0:
    a, b = b, a % b;
print(f"The greatest common divisor of {num1} and {num2} is: {a}");
