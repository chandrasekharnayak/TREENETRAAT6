# def add():
#     result = 10+20
#     print(result)
#
# add()

#what is parameter


# def add(a,b):
#     result = a+b
#     print(result)
#
# add(10,20,30)


#even or odd

# def even_odd(a):
#     if a%2==0:
#         print('even')
#     else:
#         print('odd')
#
# even_odd(10)
# even_odd(11)
# even_odd(19)


#return keyword

#
# def even_odd(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
#
# print(even_odd(10))
# even_odd(11)
# even_odd(19)


#Type of arguments

# def function(a,b,c): :-  parameter   -------- formal arguments
#     logic
#
# fucntion(v1,v2,v3) ------ arguments ----------- actual arguments

#positional arguments
#keyword
#deafult
#variable length


# positional arguments

# def sub(a,b,c):
#     re = a-b
#     return re
#
# print(sub(20,10,40,50))


#keyword arguments

# def wish(name,msg,dt):
#     return f'hi {name}, {msg} on {dt}'
#
# print(wish('Ashutosh','Good Afternoon','19-923'))

#positiona arg, head arg


#default:-
#--------

# def wish(guest='Bhai'):
#     return f'{guest} welcome'
#
# print(wish('Sibashis'))
# print(wish('Anoml'))
# print(wish())
# print(wish('Suvam'))

# write a function in this function provide fibonacy series
# write a function check the number is palledrom or not


#Variable length arg:- nth of arg

# nth *args
# , kwrag nth :- **kwargs


# def cal(*args):
#     sum = 0
#     for i in args:
#         sum = sum+i
#     print(sum)
#
# cal(102,209,1678,1678,674,4684,87384,3768.4567,345,567,56,4567,567)

# def mrg_event(*args):
#     for i in args:
#         if i[0]=='S' or i[0]=='s':
#             print(i)
#
# mrg_event('Sudeep','Utkala','shankar','Satya','Shreeya','Papun')

#kwargs


# def data(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# data(Name='A',Salary=50000,org=['Citrix','Harman','Honeywell'])


# data({'Name':'A','Salary':50000,'org':'Citrix'},{'Name':'B','Salary':70000,'org':'KPMG'},{'Name':'C','Salary':43000,'org':'EverSana'},{'Name':'D','Salary':32000,'org':'Infosys'},{'Name':'E','Salary':80000,'org':'Calsoft'},{'Name':'F','Salary':20010,'org':'Citi'},)


# Types of variable
# global variable
#local variable

# a = 5 #global
# print(a)
# def fun():
#     global b
#     b = 10 #local
#     c = a+b
#     print('fun',c)
#
#
# fun()
#
# def fun1():
#     print('func1',b)
#
# fun1()

# Nested Function

# def outer():
#     print('Outer function excution')
#     def inner():
#         print('Inner function execution')
#         print('Inner function completed')
#     inner()
#     print('outer function completed')
#
# outer()


# def add(a,b):
#     result = a+b
#     def even(num):
#         if num%2==0:
#              print('Even')
#     even(result)
#     return result
#
# print(add(10,'erty'))


#ananyomous function :- lambda fubntion
#map(),reduce(),filter()
#list com and dict com
#decorator and genetor


# write a function in this function provide fibonacy series
# write a function check the number is palledrom or not

# def fib(n):
#     a = 0
#     b  = 1
#     while a<n:
#         print(b)
#         a  = a+b
#         a,b = b,a
# fib(10)
# a = 0
# b = 1
#
# a,b = b,a
# print(a)
# print(b)

from functools import *
# def list_even_check(list):
#     var = reduce(lambda a,b:a+b,list)
#     def inner(var):
#         print(var)
#     inner(var)
#
#
# li = [16,19,21,24,26,29,34,35,56,45]
#
# result =list_even_check(li)
# sum = 0

# def func(a,b):
#     sum = a+b
#     print(sum)
#     def inner(sum):
#         if sum%2==0:
#             print('even')
#         else:
#             print('odd')
#     inner(sum)
#
# func(11,'tfgy')

#Lambda :- Anonymyous
# Syntax:-
'''
lambda parameter:statement

def func(parameter):
    statement
'''

# def add(a,b):
#     sum = a+b
#
# a = lambda a,b:a+b
# print(a(10,20))

# even = lambda a:a%2==0
# print(even(11))


# filter,map, reduce

'''
syntax :- filter(func_name,collection)

'''

# li = [10,20,23,12,25,24,36,45,67,68]

# var = list(filter(lambda i:i%2==0,li))
# print(var)

# def even_list(i):
#         if i%2==0:
#             return True
#
# var = list(filter(even_list,li))
# print(var)

#map
'''
var = map(function,collection)
'''
# li = [10,20,23,12,25,24,36,45,67,68]

# def mul_list(i):
#     sum =i*i
#     return sum
# var= list(map(mul_list,li))
# print(var)

# var = list(map(lambda i:i*i,li))
# print(var)

#reduce

# from functools import *
#
# li = [10,20,23,12,25,24,36,45,67,68]
#
# var = reduce(lambda a,b:a+b,li)
# print(var)

#
# decorator, genetor
# list com, dict com

# def ashutosh(add):
#     def divison(a,b):
#         div = a/b
#         return div,add(a,b)
#     return divison
#
# def abhishek(add):
#     def multiple(c,d):
#         mul = c*d
#         return mul,add(c,d)
#     return multiple
#
#
# @ashutosh
# @abhishek
# def add(a,b):
#     sum = a+b
#     return sum
#
# print(add(10,20))


# def div_decore(function_name):
#     def divison(parameter):
#         var = logic
#         return var,function_name(parameter)
#     return divison
#
#
# def mul_decore(function_name):
#     def multiple(parameter):
#         var =logic
#         return var,function_name(parameter)
#     return multiple
#
#
# @div_decore
# @mul_decore
# def function_name:
#     addition kariba
#     return value
#
# function(parameter,)

#generator

# def gen(li):
#     for i in li:
#         yield i
# li = [56,90,78,65,34]
# obj = gen(li)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

#with the help of range print 1 to 5 in generator

# def gen():
#     for i in range(1,6):
#         yield i
# var = gen()
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))

# function
# parameter
# types of args - position,keyword,default,var length,kw
# type variable
# nested function
# lambda :- filter,map,reduce
# decorator
# generator

# addition:-
# list com, dict com
# syntax
# var = [value interation with condtion]

# range(1,11)

# def lis():
#     li = []
#     for i in range(1,11):
#         if i%2 ==0:
#             li.append(i)
#     return li
# print(lis())
#
# var = [i for i in range(1,11) if i%2 ==0]
# print(var)
# print(var)


# def number_mul_five():
#     li = []
#     for i in range(1,6):
#         li.append(i*5)
#     return li
#
# print(number_mul_five())
#
# var = [i*5 for i in range(1,6)]
# print(var)




















