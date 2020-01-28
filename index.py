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
igor.set ("Игорь", 23, 5)
print ("Имя: ", igor.name, ", возвраст - ", igor.age, ", курс - ", igor.course)

vlad = Person ("Влад", 25)
#vlad.set ("Влад", 25)
print (vlad.name + " " + str(vlad.age))

ivan = Person ("Иван", 56)
#ivan.set ("Иван", 56)
print (ivan.name + " " + str(ivan.age))

