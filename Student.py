class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)

s1 = Student("Rahul", 20, 85)
s1.display()
