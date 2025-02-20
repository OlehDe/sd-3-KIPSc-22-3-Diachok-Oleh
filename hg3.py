for num in range(1, 11):
   print(num)

for num1 in range(1, 21):
   if num1 % 2 == 0:
       print(num1)

class Person:
   def __init__(self, name):
       self.name = name
   def greet(self):
       return f"Привіт, мене звуть {self.name}"


class Student(Person):
   def student_2(self):
       return True
student = Student("Олег")


print(student.greet())
print(student.student_2())

from abc import ABC, abstractmethod
import math

class Shape(ABC):
   @abstractmethod
   def area(self):
       pass

class Circle(Shape):
   def __init__(self, radius):
       self.radius = radius

   def area(self):
       return math.pi * self.radius ** 2

class Rectangle(Shape):
   def __init__(self, width, height):
       self.width = width
       self.height = height

   def area(self):
       return self.width * self.height

circle = Circle(50)
rectangle = Rectangle(30, 70)

print(f"Площа кола з радіусом {circle.radius}: {circle.area()}")
print(f"Площа прямокутника {rectangle.width}x{rectangle.height}: {rectangle.area()}")
