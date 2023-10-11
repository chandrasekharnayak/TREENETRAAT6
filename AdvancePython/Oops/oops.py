# What is class
''' In python everything is an object, class is model and blue print or a plan, which
is nothing but a class

2. we define a class with the help class keyword.

'''

# class Car:  ---- model
#
#     def Streeing
#     def Accerator
#     def clustch
#     def break
#     def gear
#     def seats
#     def wheel
#     fuel
#     lights
#     engine


#How to write a class
#Syntax
# import ossaudiodev

'''
class ClassName:
    """ doc_string """
    statements
    variable :- instance variable,static variable, local variable
    method :- instance method, static method, class method

'''

# class Students:
#     '''This class for students information'''
#
#     def __init__(self):
#         self.name = 'Utkala'
#         self.age = 25
#         self.lang = 'Python'
#
#     def legend(self):
#         '''this method of legend of method'''
#         pass
#
# print(Students.__doc__)
# print(help(Students))


# What is a object reference


#
# class Students:
#     '''This class for students information'''
#
#     def __init__(self):
#         self.name = 'Utkala'
#         self.age = 25
#         self.lang = 'Python'
#
#     def legend(self):
#         '''this method of legend of method'''
#         pass
#
#
# # variable ----- objectReferenece
#
# obj = Students()
# # print(obj.__dict__)
# print(dir(Students))
# obj.legend()

# What is Constructor

# class Students:
#
#     def __init__(self,name,age,lang):
#         self.name = name
#         self.age = age
#         self.lang = lang
#
#     def display(self):
#         print(f'The name of students is {self.name}, and he/her age is {self.age}, lang is :- {self.lang}')
#
# obj = Students('Rabi',24,'Java')
# # print(obj.__dict__)
# obj.display()




# class Dmart:
#
#     def __init__(self,rice,dal,oil):
#         self.rice = rice
#         self.dal = dal
#         self.oil = oil
#
#     def d_rice(self):
#         buy = int(input('Enter how much you want to buy:-'))
#         self.rice = self.rice-buy
#         print(f'Current Rice is in KG:-{self.rice}')
#
#     def d_dal(self):
#         buy = int(input('Enter how much you want to buy:-'))
#         self.dal = self.dal-buy
#         print(f'Current Dal is in KG:-{self.dal}')
#
#     def d_oil(self):
#         buy = int(input('Enter how much you want to buy:-'))
#         self.oil = self.oil-buy
#         print(f'Current OIL is in ltr:-{self.oil}')
#
#     def current_stock(self):
#         print (f'Rice:- {self.rice}kg,Dal:- {self.dal}kg,oil:- {self.oil}ltr')
#
#
# obj = Dmart(90,78,50)
# print(obj.__dict__)
# obj.d_rice()
# obj.d_dal()
# obj.d_oil()
# obj.current_stock()

# Instance variable, Class variable and Static Variable

# who is chnage is value from object to object it's know as instance variable

# class Students:
#
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def a(self,location):
#         self.location = location
#
# obj = Students('Utakala',25,67070.89)
# obj.pincode = 751003
# obj.post = 'Ghatikia'
# obj.a('Marathahalli')
# print(obj.__dict__)

#Inside the constructor with the help of self keyword
#Inside the  method with the help of self keyword
#Outside Class help of object reference

# Access

# class Students:
#
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def a(self,location):
#         self.location = location
#
#
#     def check_the_data(self):
#         print(self.name,self.age,self.salary,self.location)
#
# obj = Students('Utakala',25,67070.89)
# # del obj.salary
# obj.a('Marathahalli')
# obj.check_the_data()

# write a class declare a bus, bus have owner,driver,condoctor, create 3method for owner,driver,condutor
# write the perosnal data, name,age,salary

# class Bus:
#     def __init__(self,owner,driver,conductor):
#         self._owner = owner
#         self._driver = driver
#         self._conductor = conductor
#
#     def owner(self,o_name,o_age,o_salary):
#         self.o_name = o_name
#         self.o_age = o_age
#         self.o_salary = o_salary
#         print(f'Owner Name:- {self.o_name},Owner Age :- {self.o_age}, Owner salary :- {self.o_salary}')
#
#     def driver(self,d_name,d_age,d_salary):
#         self.d_name = d_name
#         self.d_age = d_age
#         self.d_salary = d_salary
#         print(f'driver Name:- {self.d_name},driver Age :- {self.d_age}, driver salary :- {self.d_salary}')
#
#
#     def conductor(self,c_name,c_age,c_salary):
#         self.c_name = c_name
#         self.c_age = c_age
#         self.c_salary = c_salary
#         print(f'conductor Name:- {self.c_name},conductor Age :- {self.c_age}, conductor salary :- {self.c_salary}')
#
#     def total_salary(self):
#         total = self.c_salary+self.d_salary+self.o_salary
#         print(total)
# bus_obj = Bus('Dolphin Owner','Doplhin Driver','Dolphin Conductor')
#
# # bus_obj.owner('BO',45,90000)
# # bus_obj.driver('BD',32,78000)
# # bus_obj.conductor('BC',35,78000)
# # bus_obj.total_salary()
# #
# # bus_obj.owner()
# print(bus_obj.owner())

# Write a class for water tank, if water tak have 1000ltrs water then write a method remove the water
#and write a another method insert the water and finsla a another method check how much water is exit
#in water tank.


# class Animal:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def qwerty(self,c):
#         self.c = c
#
# obj = Animal(10,20)
# obj.qwerty(30)
# obj.d = 40
# print(obj.__dict__)


#instance variable create inside a constructor with help of self keyword
#instance varibale create inside a method with help of self keyowrd
#instance variaable create with object reference


# class A:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def func(self,c):
#         self.c = c
#
#
# obj = A(10,20)
# obj.func(30)
# obj.d = 40
# obj.e = 50
# print(obj.__dict__)


# Static Variable---- global variable
#When a variable declare in inside a class and outside a method , then it is known as static variable
#Inside a constructor and method it's access via class name
#Outside a of class with the help of object reference it's accessed.
#cls variable in class method-----

# class A:
#
#     a = 10   # static variable
#     def __init__(self):
#         pass
#
#     def func(self):
#         print(A.a)
#
# obj = A()
# # obj.func()
# print(obj.a)


#Local Variable

# class A:
    #
    # def __init__(self):
    #     pass
    #
    # def method1(self):
    #     global b
    #     b = 20   # local variable
    #
    # def method2(self):
    #     print(b)


#Types of methods

#instance method, class method, static method

# class Student:
#
#     def subjects(self,math,science,history):
#         self.math = math
#         self.science = science
#         self.history = history
#
#     def rabi(self):
#         print(self.math-21)
#         print(self.science-27)
#         print(self.history-6)
#
#
#
#
#
#
# obj = Student()
# obj.subjects(100,100,50)
# obj.rabi()

#Write a class Student therea re 3 subjects math(100), science(100) and history(50) ,
# we have 3 candidates A(17,19,4),B(16,18,3),C(20,21,9), now how much mark scored by A B C.
#i want all 3 math sum mark

#
# class Student:
#
#     def subjects(self,math,science,history):
#         self.math = math
#         self.science = science
#         self.history = history
#
#     def a(self,math_deduct,science_deduct,history_deduct):
#         self.math_deduct= math_deduct
#         self.science_deduct = science_deduct
#         self.history_deduct = history_deduct
#
#         value_a_in_math = self.math- self.math_deduct
#         value_a_in_science = self.science - self.science_deduct
#         value_a_in_history = self.history - self.history_deduct
#         print(f'Mark of A:- Math Mark:-{value_a_in_math},Science Mark:- {value_a_in_science},History Math :- {value_a_in_history}')
#
#     def b(self,math_deduct,science_deduct,history_deduct):
#         self.math_deduct= math_deduct
#         self.science_deduct = science_deduct
#         self.history_deduct = history_deduct
#
#         value_a_in_math = self.math- self.math_deduct
#         value_a_in_science = self.science - self.science_deduct
#         value_a_in_history = self.history - self.history_deduct
#         print(f'Mark of B:- Math Mark:-{value_a_in_math},Science Mark:- {value_a_in_science},History Math :- {value_a_in_history}')
#
#     def c(self,math_deduct,science_deduct,history_deduct):
#         self.math_deduct= math_deduct
#         self.science_deduct = science_deduct
#         self.history_deduct = history_deduct
#
#         value_a_in_math = self.math- self.math_deduct
#         value_a_in_science = self.science - self.science_deduct
#         value_a_in_history = self.history - self.history_deduct
#         print(f'Mark of C:- Math Mark:-{value_a_in_math},Science Mark:- {value_a_in_science},History Math :- {value_a_in_history}')
#
#
# obj = Student()
# obj.subjects(100,100,50)
# obj.a(17,19,4)
# obj.b(16,18,3)
# obj.c(20,21,9)



#ClassMethod

# class A: # 25mb --- more
#
#     a = 10
#
#     @classmethod
#     def class_method(cls):
#         print(cls.a)
#
# obj = A()
# obj.class_method()


# class CheckNumberisPrimeAndFindFibonacy():
#     a = 23 # static
#
#     @classmethod
#     def prime_or_not(cls):
#
#         if cls.a<=1:
#             return False
#
#         flag = True
#         for i in range(2,int(cls.a**0.5)):
#             if cls.a%i==0:
#                 flag = False
#                 break
#         return flag
#
#     @classmethod
#     def fibionacy(cls):
#         fib_series = [0,1]
#
#         while len(fib_series)<cls.a:
#             fib_series.append(fib_series[-1]+fib_series[-2])
#         return fib_series
#
#
# obj = CheckNumberisPrimeAndFindFibonacy()
# print(obj.a,obj.prime_or_not())
# print(obj.a,obj.fibionacy())


#StataicMethod

# class Claculator:
#
#     @staticmethod
#     def add(a,b):
#         re = a+b
#         return re
#
#     @staticmethod
#     def sub(a,b):
#         re  = a-b
#         return re
#
#     @staticmethod
#     def mul(a,b):
#         re = a*b
#         return re
#
#     @staticmethod
#     def div(a,b):
#         re= a/b
#         return re


# class Fib():
#     def fibonacci(self,n):
#         if n < 0:
#             raise ValueError('n must be a non-negetive number')
#         elif n == 0 or n == 1:
#             return n
#         else:
#             return self.fibonacci(n - 1) + self.fibonacci(n - 2)
#
#
#     def print_fibonacci_till(self,n):
#         for i in range(n+1):
#             print(self.fibonacci(i))
#
#
# obj = Fib()
# obj.print_fibonacci_till



#INHERITANCE


# class Parent():---- Parent
#
#     def have_150cr
#
#     def have_5kg_gold
#
#     def have_500_trucks
#
#
# class Child(Parent):----- Child Class
#
#     def have_2kg_dimond:
#
#     def have_200_buses:

#Single Inheritance
#Multiple Inheritance
#Multilevel Inheritance
#Hirechical Inehritnace
#Hybrid Inheritance

#Single Inheritance

# class Animal: #------------------parent class
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print(f'{self.name} make a sound')
#
#
# class Dog(Animal): # ------child class of animal
#     def brak(self):
#         print(f'{self.name} braks')
#
# my_dog = Dog('Charlee')
# my_dog.brak()
# my_dog.speak()

#Write Program take class Person and person have name and age and write information method
#and in a another class Employee and employee have emp_id , display person info and employee info
#
# class Person:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def person_information(self):
#         print(f'Name is :- {self.name} and age is :- {self.age}')
#
# class Employee(Person):
#
#     def __init__(self,name,age,emp_id):
#         self.emp_id = emp_id
#         super().__init__(name,age)
#
#     def employee_info(self):
#         print(f'ID:-{self.emp_id}')
#         print(f'Name:-{self.name}')
#         print(f'Age:-{self.age}')
#
#
# emp_obj = Employee('Shankar','25',101)
# emp_obj.person_information()
# emp_obj.employee_info()


#MULTIPLE INHHERITANCE

# class A
#
# class B
#
# class C
#
# class D
#
# class E(A,B,C,D)


# class Engine:
#
#     def start(self):
#         print('Engine Start')
#
# class Wheels:
#
#     def rolls(self):
#         print('Wheels rolling')
#
# class Vechile(Engine,Wheels):
#     def move(self):
#         print('Vechile moving')
#
# v_obj = Vechile()
# v_obj.start()
# v_obj.rolls()
# v_obj.move()

# single and multiple both
# class MathOperation:
#
#     def __init__(self,operand1,operand2):
#         self.operand1 = operand1
#         self.operand2 = operand2
#
# class Addition(MathOperation):
#
#     def add(self):
#         result = self.operand1+ self.operand2
#         return result
#
# class Multiplication(MathOperation):
#
#     def mul(self):
#         result = self.operand1*self.operand2
#         return result
#
# class MathResult(Addition,Multiplication):
#
#     def math_display_result(self):
#         result_of_addition = self.add()
#         result_of_multiplication = self.mul()
#         print(f'result_of_addition:- {result_of_addition}')
#         print(f'result_of_multiplication:- {result_of_multiplication}')
#
#
# obj = MathResult(10,20)
# print(obj.math_display_result())



#Multi Level Inhheritance

# class Jeje:
#
#
# class Bapa(Jeje):
#
# class Mu(Bapa):
#
# class MoPua(Mu):

#
# class MathOperation:
#
#     def __init__(self,operand1,operand2):
#         self.operand1 = operand1
#         self.operand2 = operand2
#
# class Addition(MathOperation):
#
#     def add(self):
#         result = self.operand1+ self.operand2
#         return result
#
# class Squre(Addition):
#     def squre_result(self):
#         return self.add()**2
#
# class MathResult(Squre):
#
#     def result_display(self):
#         result_of_add = self.add()
#         result_of_squre =self.squre_result()
#         print(self.operand2,self.operand1)
#         print(f'result_of_add:-{result_of_add}')
#         print(f'result_of_squre:-{result_of_squre}')
#
# obj = MathResult(10,20)
# obj.result_display()



#H In

# class A:  - 60
#
# class B(A):- 20   - 80
#
# class C(A)- 40   100
#
# class D(A) - 50 --- 110


#
# class MathOperation:
#
#     def __init__(self,operand1,operand2):
#         self.operand1 = operand1
#         self.operand2 = operand2
#
# class Addition(MathOperation):
#
#     def add(self):
#         result = self.operand1+ self.operand2
#         return result
#
# class Multiplicattion(MathOperation):
#
#     def mul(self):
#         result = self.operand1*self.operand2
#         return result
#
#
# class Division(MathOperation):
#     def div(self):
#         result = self.operand1/self.operand2
#         return result
#
# obj_add = Addition(10,20)
# obj_mul = Multiplicattion(10,20)
# obj_div = Division(10,20)
# print(obj_add.add())
# print(obj_mul.mul())
# print(obj_div.div())


# Singale
#
# one -- clas ---- one child
# class A   class B(A)  -
# multiple
#
# multiple class ---- one child
#
#
# class A class B class C   class D(A,B,C)
#
#
# one class --- anothe one class and it's repeat
#
#
# class A class B(A) class C(B) class D(C)
#
# single class -- inherrite multiple clasess
#
# class A  class B(A)  class C(A)   class D(A)


class A:

    def __init__(self,obj1,obj2):
        self.obj1 = obj1
        self.obj2 = obj2


class B(A):

    def __init__(self,obj1,obj2,obj3):
        self.obj3 = obj3
        super().__init__(obj1,obj2)


Intro
Keyowrd
Identifier
data type/data structure
opeartor
input
flow control

Function
File Handeling
exception handeling
madule and package
oops

# list-dict-- compil
# shallow - deep
# excel handeling






