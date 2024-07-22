# 8
number: int = int(input("Enter a number: "));
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"The number {number} is prime.");
else:
    print(f"The number {number} is not prime.");
