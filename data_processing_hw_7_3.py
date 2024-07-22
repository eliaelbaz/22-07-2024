# 3
numbers = [];
for i in range(5):
    number = int(input(f"Enter number {i + 1}: "));
    numbers.append(number);
highest_number_index = numbers.index(max(numbers)) + 1;
print("The serial number of the highest value is:", highest_number_index);
