class Course:

    def __init__(self,name,course_code,teacher,credits,duration,capacity):
        self.name=name
        self.course_code=course_code
        self.teacher=teacher
        self.credits=credits
        self.duration=duration
        self.students=[]
        self.capacity=capacity