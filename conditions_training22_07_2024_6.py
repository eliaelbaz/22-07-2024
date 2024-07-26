# 6
number = input("Enter a 4-digit number: ");
if len(number) == 4 and number.isdigit():
    second_rightmost_digit = number[-2];
    print("The second rightmost digit is:", second_rightmost_digit);
else:
    print("Please enter a valid 4-digit number.");
