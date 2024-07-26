# 4
minutes: int = int(input("Enter the length of the movie in minutes: "));
hours = minutes // 60;
remaining_minutes = minutes % 60;
print(f"{hours} hour(s) and {remaining_minutes} minute(s)");
