# 11
age: int = int(input("Enter your age: "));
height: int = int(input("Enter your height in cm: "));
if (age >= 8 and age <= 18 and height > 115) or (age > 18 and height > 100):
    print("Allowed to ride the roller coaster");
else:
    print("Not allowed to ride the roller coaster");
