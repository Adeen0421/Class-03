def grading_system(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        print("Marks must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Enter a number.")

print(f"Grade: {grading_system(marks)}")
