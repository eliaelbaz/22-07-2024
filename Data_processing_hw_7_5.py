# 5
base = int(input("Enter the base number: "));
exponent = int(input("Enter the exponent: "));
result = 1;
for _ in range(abs(exponent)):
    result *= base;
if exponent < 0:
    result = 1 / result;
print(f"The result of {base} raised to the power of {exponent} is: {result}");
