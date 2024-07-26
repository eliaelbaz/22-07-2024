# 1
temperatures = [];
for _ in range(12):
    try:
        temp = input("Enter the average temperature for the month: ");
        temp = float(temp);
        if temp < -5 or temp > 40:
            print("wrong data");
            break
        if len(temperatures) >= 1 and temperatures[-1] == 0 and temp == 0:
            print("Ignoring consecutive zeros, please re-enter.");
            continue
        temperatures.append(temp);

    except ValueError:
        print("Invalid input. Please enter a numeric value.");
        break
else:
    print("correct data");
    average_temp = sum(temperatures) / len(temperatures);
    highest_temp = max(temperatures);
    lowest_temp = min(temperatures);
    print(f"The average temperature is: {average_temp:.2f}°C");
    print(f"The highest temperature is: {highest_temp}°C");
    print(f"The lowest temperature is: {lowest_temp}°C");
