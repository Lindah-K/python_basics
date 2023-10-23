class Students:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def display(self):
        print("Name: %s \nCourse: %s \nGender: %s \nAge: %d"
              %(self.name,self.course,self.gender,self.age))

myobj = Students("Lindah kima","Software Engineering", "female", 21)
myobj2 = Students("Brian zilla", "BBIT", "Male", 22)
myobj.display()
print()
myobj2.display()