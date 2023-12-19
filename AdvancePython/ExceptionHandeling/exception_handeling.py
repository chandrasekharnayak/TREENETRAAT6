# runtime time
#syntax error

#Attribute Error
# class Myclass:
#     def __init__(self):
#         self.a = 42
#
# my_obj = Myclass()
# print(my_obj.b)

# # ZeroDivisionError
# c = 23/0
# print(c)

# FloatingPointError
# a = 0.1+0.1+0.1
# print(a)
# b = 0.3

# OverflowError
# result = 2**100000000000000000000000000000000000
# result = 2**10
# print(result)


## EOFError
user_input = input('Enter a number  ')
print(user_input)

# NameError
# print(variable_name_nor_exit)



# IndexError
# li = [12,78,90]
# print(li[3])

# KeyError

# di = {'A':101,'B':203}
# print(di['C'])

#
# while True:
#     pass


# TypeError

# 5+'6'

# s = {1,2,3}
# s[0]

# ValueError

# value = int('asd')
# import math
# math.sqrt(-1)

# try:
#     #Risky code
#
# except ExceptionName:
#     #Error Handeling
#
# finally:
#     #Final code


#sittuation1
# try:
#     a = eval(input('Enter a number 1st:-'))
#     b = eval(input('Enter a number 2nd:-'))
#     c = a/b
#     print(c)
#
# except ZeroDivisionError:
#     print('Ok error handel Zero')
#
# except TypeError:
#     print('Ok error handel Type')


#Sittuation2

# try:
#     a = eval(input('Enter a number 1st:-'))
#     b = eval(input('Enter a number 2nd:-'))
#     c = a/b
#     print(c)
#
# except (ZeroDivisionError, TypeError) as msg:
#     print('Ok error handel',msg)

#sittuation3

# try:
#     a = eval(input('Enter a number 1st:-'))
#     b = eval(input('Enter a number 2nd:-'))
#     c = a/b
#     print(c)
#
# except ZeroDivisionError as msg:
#     print('Ok error handel Zero')
#     a = 1
#     b = 1
#     c = a/b
#     print(c)


#Sittuation4

try:
    a = eval(input('Enter a number 1st:-'))
    b = eval(input('Enter a number 2nd:-'))
    c = a/b
    print(c)

except (ZeroDivisionError,ValueError,NameError):
    print('Ok error handel Zero')

except Exception as msg:
    print(msg)


