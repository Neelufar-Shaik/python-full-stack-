#1. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


person1 = Person("Neelufar", 21)
person1.display()
#2. Encapsulation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student = Student("Neelufar", 85)

print("Student Name:", student.name)
print("Marks:", student.get_marks())

student.set_marks(90)
print("Updated Marks:", student.get_marks())
#3. Inheritance and super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        super().display()
        print("Model:", self.model)


car = Car("Toyota", "Camry")
car.display()
#4. Polymorphism
class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


square = Square(5)
triangle = Triangle(10, 6)

print("Square Area:", square.area())
print("Triangle Area:", triangle.area())
#5. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Sum:", v3)