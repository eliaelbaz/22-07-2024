# 5
number = input("Enter a 4-digit number: ");
if len(number) == 4 and number.isdigit():
    rightmost_digit = number[-1];
    print("The rightmost digit is:", rightmost_digit);
else:
    print("Please enter a valid 4-digit number.");
