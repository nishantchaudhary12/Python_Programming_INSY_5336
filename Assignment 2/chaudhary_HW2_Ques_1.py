
def determine_grade(grade):
    if grade >= 90:
        print('The grade for this course is: A')
    elif 80 <= grade < 90:
        print('The grade for this course is: B')
    elif 70 <= grade < 80:
        print('The grade for this course is: C')
    elif 60 <= grade < 70:
        print('The grade for this course is: D')
    else:
        print('The grade for this course is: F')

    return grade


def calc_average(grade1,grade2,grade3,grade4,grade5):
    average = (grade1 + grade2 + grade3 + grade4 + grade5)/5
    print('The average score is:',format(average,'.2f'))


def main():
    grade1 = float(input("Enter the first grade: "))
    determine_grade(grade1)
    grade2 = float(input("Enter the second grade: "))
    determine_grade(grade2)
    grade3 = float(input("Enter the third grade: "))
    determine_grade(grade3)
    grade4 = float(input("Enter the fourth grade: "))
    determine_grade(grade4)
    grade5 = float(input("Enter the fifth grade: "))
    determine_grade(grade5)

    calc_average(grade1,grade2,grade3,grade4,grade5)

if __name__ == "__main__":
    main()
