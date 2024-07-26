# 10
salary: float = float(input("Enter your salary: "));
tax = 0;
if salary > 50000:
    tax += (salary - 50000) * 0.51;
    salary = 50000;

if salary > 35000:
    tax += (salary - 35000) * 0.45;
    salary = 35000;

if salary > 25000:
    tax += (salary - 25000) * 0.40;
    salary = 25000;

if salary > 18000:
    tax += (salary - 18000) * 0.30;
    salary = 18000;

if salary > 12000:
    tax += (salary - 12000) * 0.20;
    salary = 12000;

if salary > 6000:
    tax += (salary - 6000) * 0.10;

print(f"The tax to be paid is: {tax:.2f} NIS");
