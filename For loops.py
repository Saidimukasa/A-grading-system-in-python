#aprogram that checks for grade A, B, C, D, F
print("Enter a grade:")
grade = input()
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Fair")
elif grade == "D":
    print("Poor")
elif grade == "F":
    print("Fail")
else:
    print("Invalid grade")
    