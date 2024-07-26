# 3
n: int = int(input("Enter a natural number (positive integer): "));
if n >= 0:
    for i in range(0, n + 1, 2):
        print(i);
else:
    print("Please enter a positive integer.");
