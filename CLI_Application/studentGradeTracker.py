class Grade_Tracker():

    def __init__(self):
        self.name = ''
        self.subject_grade = {}
        self.percentage = 0
        self.on = True
        self.main()

    def take_data(self):
        self.name = input("Enter the name: ")
        number_of_subjects = int(input("Enter the number of subjects: "))

        for _ in range(number_of_subjects):
            subject = input("Subject name: ")
            marks = int(input("Marks obtained: "))
            self.subject_grade[subject] = marks

    def subject_grades_show(self):
        print(f'\t Subject Name | Marks Obtained | Out of | Grade ')
        for subject, marks in self.subject_grade.items():
            if marks >= 90:
                grade = 'A+'
            elif marks >= 75:
                grade = 'A'
            elif marks >= 60:
                grade = 'B'
            elif marks >= 45:
                grade = 'D'
            else:
                grade = 'Fail'
            print(f'\t {subject}\t | \t {marks} \t | \t 100 \t | \t {grade}   ')

    def average_grade(self):
        total_marks_obtain = sum(self.subject_grade.values())
        total_marks = len(self.subject_grade) * 100
        self.percentage = (total_marks_obtain / total_marks) * 100

        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 75:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 45:
            return 'D'
        else:
            return 'Fail'
    
    def GPA(self):
        return (self.percentage / 100) * 5

    def show_data(self):
        print("\n \t \t Student Result ")
        print(f'Name of the student: {self.name} \n')
        self.subject_grades_show()
        overall_grade = self.average_grade()
        gpa = self.GPA()
        print(f'Overall Grade: {overall_grade} \t Percentage: {self.percentage:.2f}% \t GPA: {gpa:.2f} \n')

    def main(self):
        while self.on:
            self.take_data()
            self.show_data()
            self.save()

            if input("Do you want to Continue ? : (Y/n) ") != "Y":
                self.on = False
                print()

    def save(self):
        with open('studentgradefile.csv', 'a+') as file:
            content = f'Student name: {self.name} \n Subject-grade: {self.subject_grade} \n Overall Grade: {self.average_grade()} \n Percentage: {self.percentage} \n GPA: {self.GPA()}'
            file.write(content)

if __name__ == "__main__":
    student_grade_tracker = Grade_Tracker()
