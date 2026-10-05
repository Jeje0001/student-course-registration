from student import Student
from course import Course
s1=Student("Jeje",20,"Freshman")
s2=Student("AMY",10,"Sophomore")
s3=Student("David",18,"Junior")


math=Course("MATH",123,"AMY",4,2,2)
english=Course("English",124,"Jenny",3,1,1)
s1.enroll(math)
s2.enroll(math)
s1.enroll(english)
s1.enroll(english)
s1.show_courses()
s3.enroll(math)

math.show_students()
s1.drop(math)
s1.show_courses()
math.show_students()
s1.drop(math)