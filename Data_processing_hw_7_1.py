# 1
total_sum = 0;
while True:
    number = int(input("Enter a number (or -99 to stop): "));
    if number == -99 and total_sum == 0:
        print(None);
        break
    if number == -99:
        break
    total_sum += number;
if total_sum != 0:
    print("The total sum is:", total_sum);
