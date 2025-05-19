class Calculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other
    
    def __sub__(self, other):
        return self.value - other
    
    def __mul__(self, other):
        return self.value * other
    
    def __truediv__(self, other):
        return self.value / other


calc = Calculator(123)
result = calc + 334
print(result)  

result = calc - 334
print(result) 

result = calc * 334
print(result) 

result = calc / 3
print(result)

#3
s = 'Hello World~'

print(s.upper())

#5
a = 1
b = 1
c = 2
d = 3
e = 3

print(a is b)
print(a is c)
print(d is e)
print(c is d)

#7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"이름은 {self.name}이고 나이는 {self.age}살입니다."

my_dog = Dog("Mango", 3)
print(my_dog)

#9
class Counter:
    def __init__(self, number=0):
        self.__number = number if 0 <= number < 100 else 0
    
    def reset(self):
        self.__number = 0
    
    def inc(self):
        self.__number += 1
        if self.__number >= 100:
            self.__number = 0
    
    def dec(self):
        self.__number -= 1
        if self.__number <= -1:
            self.__number = 0
    
    def __str__(self):
        return f"C({self.__number})"
    
    def __add__(self, other):
        new_number = self.__number + other.__number
        return Counter(new_number if new_number < 100 else 0)
    
    def __sub__(self, other):
        new_number = self.__number - other.__number
        return Counter(new_number if new_number >= 0 else 0)

c1 = Counter(18)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)

#11
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.korean_quiz = 0
        self.math_quiz = 0
        self.science_quiz = 0
        self.total_score = 0
    
    def __str__(self):
        avg = self.total_score / 3
        return f"이름 : {self.name}, 학번 : {self.student_id}\n국어 성적 : {self.korean_quiz}, 수학 성적 : {self.math_quiz}, 과학 성적 : {self.science_quiz}\n합계 : {self.total_score}, 평균 : {avg:.1f}"
    
    def get_name(self):
        return self.name
    
    def get_student_id(self):
        return self.student_id
    
    def get_korean_quiz(self):
        return self.korean_quiz
    
    def get_math_quiz(self):
        return self.math_quiz
    
    def get_science_quiz(self):
        return self.science_quiz
    
    def set_korean_quiz(self, score):
        self.korean_quiz = score
        self._update_total()
    
    def set_math_quiz(self, score):
        self.math_quiz = score
        self._update_total()
    
    def set_science_quiz(self, score):
        self.science_quiz = score
        self._update_total()
    
    def _update_total(self):
        self.total_score = self.korean_quiz + self.math_quiz + self.science_quiz
    
    def get_total_score(self):
        return self.total_score
    
    def get_avg_score(self):
        return self.total_score / 3

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')
student = Student(name, student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))
student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)

#13
class Rectangle:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    
    def __str__(self):
        area = self._width * self._height
        return f"Rectangle : (x = {self._x}, y = {self._y}, w = {self._width}, h = {self._height}), 면적 : {area}"
    
    def set_x(self, x):
        self._x = x
    
    def get_x(self):
        return self._x
    
    def set_y(self, y):
        self._y = y
    
    def get_y(self):
        return self._y
    
    def set_width(self, width):
        self._width = width
    
    def get_width(self):
        return self._width
    
    def set_height(self, height):
        self._height = height
    
    def get_height(self):
        return self._height
    
    def area(self):
        return self._width * self._height
    
    def overlaps(self, r):
        return not (self._x + self._width < r._x or 
                    r._x + r._width < self._x or 
                    self._y + self._height < r._y or 
                    r._y + r._height < self._y)
    
    def contains(self, r):
        return (self._x <= r._x and 
                self._y <= r._y and 
                self._x + self._width >= r._x + r._width and 
                self._y + self._height >= r._y + r._height)

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))
