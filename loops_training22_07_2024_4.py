# 4
max_num: int = int(input("Enter the maximum number (max): "));
den: int = int(input("Enter the divisor (den): "));
if max_num >= 0 and den > 0:
    for i in range(0, max_num + 1):
        if i % den == 0:
            print(i);
else:
    print("Please enter positive integers for both max and den.");
