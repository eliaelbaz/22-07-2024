# 7
number = input("Enter a 2-digit number: ");
if len(number) == 2 and number.isdigit():
    sum_of_digits = int(number[0]) + int(number[1]);
    print("The sum of the digits is:", sum_of_digits);
else:
    print("Please enter a valid 2-digit number.");
