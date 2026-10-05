class Student:
    school="Indiana University"

    def __init__(self,name,age,year):
        self.name=name
        self.age=age
        self.year=year
        self.courses=[]

    def enroll(self,course):

        if course in self.courses:
            print(f"{self.name} is already enrolled")
            return
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


    def show_courses(self):

        if not self.courses:
            print( "You are not enrolled in any courses")
            return 

        for c in self.courses:
            print(c.name)

