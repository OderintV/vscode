class Student:
    def __init__(self, name):
        self.name = name
        self.teachers = []
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def introduce(self):
        print(f"Hi, I am a student {self.name}")

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
        student.add_teacher(self)
    def introduce(self):
        print(f"Hello I am teach {self.name}")

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)

class School:
    def __init__(self, name):
        self.name = name
        self.classrooms = []
        self.teachers = []
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def display_info(self):
        print(f"school name: {self.name}")
        print("classroom: ")
        for classroom in self.classrooms:
            print(f"- {classroom.name}")
        print("teachers: ")
        for teacher in self.teachers:
            print(f"- {teacher.name}")

my_school = School("Greenfield High")
# making class
class_1A = Classroom("Class 1A")
class_2B = Classroom("Class 2B")
my_school.add_classroom(class_1A)
my_school.add_classroom(class_2B)

# making teach
teacher_alice = Teacher("Alice")
teacher_bob = Teacher("Bob")
my_school.add_teacher(teacher_alice)
my_school.add_teacher(teacher_bob)
# make student
student_nupur = Student("Nupur")
student_ishika = Student("Ishika")
student_ravi = Student("Ravi")

# student to classroom
class_1A.add_student(student_nupur)
class_1A.add_student(student_ishika)
class_2B.add_student(student_ravi)

# teach to student
teacher_alice.add_student(student_nupur)
teacher_alice.add_student(student_ravi)
teacher_bob.add_student(student_ishika)
teacher_bob.add_student(student_nupur)

print("\nIntroductions:")
teacher_alice.introduce()
teacher_bob.introduce()
student_nupur.introduce()
student_ishika.introduce()
student_ravi.introduce()

print("\nStudents taught by each teacher:")
for teacher in my_school.teachers:
    student_names = [student.name for student in teacher.students]
    print(f"{teacher.name} teaches: {', '.join(student_names) if student_names else 'No students'}")
    

print("\nSchool Information:")
my_school.display_info()
