# 2
numbers = [];
while True:
    number = int(input("Enter a number (or a negative number or 0 to stop): "));
    if number == -99 and not numbers:
        print(None);
        break
    if number <= 0:
        break
    numbers.append(number);
if numbers:
    highest_number = max(numbers);
    lowest_number = min(numbers);
    print("The highest number is:", highest_number);
    print("The lowest number is:", lowest_number);
