class Student:
    school="Indiana University"

    def __init__(self,name,age,year):
        self.name=name
        self.age=age
        self.year=year
        self.courses=[]

    def enroll(self,course):
        if len(course.students) >= course.capacity:
            print(f"{course.name} is full")
        else:

            self.courses.append(course)
            course.students.append(self)
    def drop(self,course):
        if course in self.courses:
            self.courses.remove(course)
            course.students.remove(self)
        else:
            print(f"{course.name} is not in your course list")


