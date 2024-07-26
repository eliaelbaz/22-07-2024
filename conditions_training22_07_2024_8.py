# 8
number = input("Enter a 2-digit number: ");
if len(number) == 2 and number.isdigit():
    reversed_number = number[::-1];
    print("The reversed number is:", reversed_number);
else:
    print("Please enter a valid 2-digit number.");
