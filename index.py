class Person:
    name = "Ivan"
    age = 10

    def init(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course = 1

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
igor = Student ("vasia", 19)
#igor.set ("igor", 19)
igor.set ("�����", 23, 5)
print ("���: ", igor.name, ", �������� - ", igor.age, ", ���� - ", igor.course)

vlad = Person ("����", 25)
#vlad.set ("����", 25)
print (vlad.name + " " + str(vlad.age))

ivan = Person ("����", 56)
#ivan.set ("����", 56)
print (ivan.name + " " + str(ivan.age))

