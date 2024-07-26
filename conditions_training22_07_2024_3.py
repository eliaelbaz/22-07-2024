# 3
num1: int = int(input("Enter the first integer: "));
num2: int = int(input("Enter the second integer: "));
num3: int = int(input("Enter the third integer: "));
if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2;
else:
    largest_num = num3;
print("The largest number among the three is:", largest_num);
