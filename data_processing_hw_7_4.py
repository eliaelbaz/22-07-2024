
num1: int = int(input("Enter the first number: "));
num2: int = int(input("Enter the second number: "));
product = 0;
for _ in range(abs(num2)):
    product += num1;
if num2 < 0:
    product = -product;
print("The product of the two numbers is:", product);
