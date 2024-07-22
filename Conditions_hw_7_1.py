# 1
num1: float = float(input("Enter the first decimal number: "));
num2: float = float(input("Enter the second decimal number: "));
if num1 < num2:
    smaller_num = num1;
else:
    smaller_num = num2;
for _ in range(3):
    print(smaller_num);
