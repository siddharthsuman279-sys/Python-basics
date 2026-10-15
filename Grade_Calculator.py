
# Student Grade Calculator

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def main():
    print("Student Grade Calculator")
    name = input("Enter student name: ")
    subjects = ["Python", "Mathematics", "Computer Science"]
    marks = []
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks in {subject} (0-100): "))

                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)
    grade = calculate_grade(average)
    print("Result")
    print("Student:", name)
    print("Average:", average)
    print("Grade:", grade)

    if grade == "F":
        print("Keep practising. You can improve!")
    else:
        print("Result calculated successfully.")

if __name__ == "__main__":
    main()
