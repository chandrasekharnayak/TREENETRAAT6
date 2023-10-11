# li =[10,20,304,404,505,50]  -- iteration ----
# print(li)

#for   --- general iteration ---- container -- list,tuple,set.dict,range,string
#while  --- conditional iteration ---- condition

#for :- it is a loop, using while we are iteration a container object and it's fetch the element one by one.

# li = [1,2,3,4,5]

'''
for var in container:
    statement
'''
#
# for var in li:
#     print(var)

# li_1= [12,90,67,56]
#
# for var in li_1:
#     print(var)

# li = [10,20,13,15,17,19,24,42,16,18]
# even_list = []
# for var in li:#var = 10
#     if var%2==0:
#         even_list.append(var)
#
# print(even_list)

# s = 'Treenetra'

# if 'e' in s:
#     a = s.replace('e','E')
#     print(a)

# for subham in s:
#     if subham == 'e':
#         s = s.replace('e','E')
# print(s)

# 29 aug 23
#string,list,tuple,set,dict

# li = [10,20,67.90,890.80,'dfghj','fgh',[67,89]]
# str_li = []
#
# for var in li:
#     if type(var)==str:
#         str_li.append(var)
# print(str_li)


# check in a list if any duplicate char is there, then add him a another list.

# li = [1,2,3,4,5,2,2,3,10,11,12,12]
# dup_li = []
# for var in li:
#     if li.count(var)>1:
#         dup_li.append(var)
# print(dup_li)


# s = ['Subhakanta','Sujit','Subhrajit','Suvendu']
#
# li = []
#
# for var in s:
#     if var[-3:]=='jit':
#         li.append(var)
# print(li)


# s = 'My name is gupta'
#
# # op:- 'atpug si eman yM'
# print(s[::-1])


# dictionary

# di = {'name':'krishna','age':26,'city':'bbsr'}
#
# for k,v in di.items():
#     print(k,v)

# di = {'name':'a','age':78,'awards':['Nation','State','Dict']}
#
# for k,v in di.items():
#     if k == 'awards':
#         for i in v:
#             print(i)

# di = {'name':'a','age':78,'awards':['Nation','State','Dict']}
#
# for k,v in di.items():
#     if k == 'awards':
#         v.append('village')
# print(di)


# 1. it's a list = [10,89,67,23,21,45,90,12,32] accesending list with out using inbuit a method(soramwt,reverse not use)range
#2. {'Name':'Krishna,'Salary':'200k',Lang:['Jython','C++','Golang']} -- lang :- Jython -- Python
#3l = [
#         {'Name':'A','Salary':50000,'org':'Citrix'},
#         {'Name':'B','Salary':70000,'org':'KPMG'},
#         {'Name':'C','Salary':43000,'org':'EverSana'},
#        {'Name':'D','Salary':32000,'org':'Infosys'},
#         {'Name':'E','Salary':80000,'org':'Calsoft'},
#         {'Name':'F','Salary':20010,'org':'Citi'},
#  ]

#those name are above 50k fetch those name?

# di = {'Name':'Krishna','Salary':'200k','Lang':['Jython','C++','Golang']}

# for k,v in di.items():
#     if k =='Lang':
#         v[v.index('Jython')] = 'Python'
#
# print(di)

# for k,v in di.items():
#     if k == "Lang":
#         for i in v:
#             if i == "Jython":
#                 s = i.replace('Jython','Python')
#
# print(di)


# l = [
#         {'Name':'A','Salary':50000,'org':'Citrix'},
#         {'Name':'B','Salary':70000,'org':'KPMG'},
#         {'Name':'C','Salary':43000,'org':'EverSana'},
#        {'Name':'D','Salary':32000,'org':'Infosys'},
#         {'Name':'E','Salary':80000,'org':'Calsoft'},
#         {'Name':'F','Salary':20010,'org':'Citi'},
#  ]

# for i in l:
#     for k,v in i.items():
#         if k == 'Salary':
#             if v>50000:
#                 print(i)


# for i in l:
#     if i.get('Salary')>50000:
#         print(i)

#range:- genearating the sequence of number

#syntax:- range(start_number,end+1number,step)

# a = range(6)
# for i in a:
#     print(i)

# list = [10,89,67,23,21,45,90,12,32]
#
# length_of_list = len(list) #9
# # print(length_of_list)
# for i in range(length_of_list): #i = 0,1,2,3,4,5,6,7,8
#     for j in range(0,length_of_list-i-1): #0,9 (80,)
#         if list[j] < list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]

# print(list)

# a = 10
# b = 20
#
# a,b = b,a
# print(a)
# print(b)

# *
# *
# *
# *
# *

#*****
# for i in range(5):
#     print('*',end = ' ')

# li = [10,20,30]
# for i in li:
#     print(i,end=' ')

# *
# **
# ***
# ****
# *****
# n = 6
# for i in range(1,6):
#     for j in range(1,6+1-5):1,6 1,5 1,4 1,3 1,2
#         print('*'*i)


# 1. it's a list = [10,89,67,23,21,45,90,12,32] accesending list with out using inbuit a method(soramwt,reverse not use)range
#2. {'Name':'Krishna,'Salary':'200k',Lang:['Jython','C++','Golang']} -- lang :- Jython -- Python
#3l = [
#         {'Name':'A','Salary':50000,'org':'Citrix'},
#         {'Name':'B','Salary':70000,'org':'KPMG'},
#         {'Name':'C','Salary':43000,'org':'EverSana'},
#        {'Name':'D','Salary':32000,'org':'Infosys'},
#         {'Name':'E','Salary':80000,'org':'Calsoft'},
#         {'Name':'F','Salary':20010,'org':'Citi'},
#  ]

#those name are above 50k fetch those name?

# di = {'Name':'Krishna','Salary':'200k','Lang':['Jython','C++','Golang']}

# for k,v in di.items():
#     if k =='Lang':
#         v[v.index('Jython')] = 'Python'
#
# print(di)

# for k,v in di.items():
#     if k == "Lang":
#         for i in v:
#             if i == "Jython":
#                 s = i.replace('Jython','Python')
#
# print(di)


# l = [
#         {'Name':'A','Salary':50000,'org':'Citrix'},
#         {'Name':'B','Salary':70000,'org':'KPMG'},
#         {'Name':'C','Salary':43000,'org':'EverSana'},
#        {'Name':'D','Salary':32000,'org':'Infosys'},
#         {'Name':'E','Salary':80000,'org':'Calsoft'},
#         {'Name':'F','Salary':20010,'org':'Citi'},
#  ]

# for i in l:
#     for k,v in i.items():
#         if k == 'Salary':
#             if v>50000:
#                 print(i)


# for i in l:
#     if i.get('Salary')>50000:
#         print(i)

#range:- genearating the sequence of number

#syntax:- range(start_number,end+1number,step)

# a = range(6)
# for i in a:
#     print(i)

# list = [10,89,67,23,21,45,90,12,32]
#
# length_of_list = len(list) #9
# # print(length_of_list)
# for i in range(length_of_list): #i = 0,1,2,3,4,5,6,7,8
#     for j in range(0,length_of_list-i-1): #0,9 (80,)
#         if list[j] < list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]

# print(list)

# a = 10
# b = 20
#
# a,b = b,a
# print(a)
# print(b)

# *
# *
# *
# *
# *

#*****
# for i in range(5):
#     print('*',end = ' ')

# li = [10,20,30]
# for i in li:
#     print(i,end=' ')

# *
# **
# ***
# ****
# *****
# n = 6
# for i in range(1,6):
#     for j in range(1,6+1-5):1,6 1,5 1,4 1,3 1,2
#         print('*'*i)


# ******
# ****
# ***
# **
# *


#while lopp

'''
while condition:
    statement

'''

#1 to 10

# n = 1
# while n<=10:
#     print(n)
#     n = n + 1

# n= 6
# count = 1
# while n%2==0 and n<(n*11):
#     result = n*count
#     print(result)
#     count = count+1


# n = 6
# count = 1
# while n%2==0 and count<=10:
#     result = count*n
#     print(result)
#     count = count+1


# write a program print fact using while --

# n=4
# fact=1
# while n>=1:
#     fact = fact*n
#     print(fact)
#     n=n-1

# num =  4
# n = 1
# fact = 1
#
# while fact<=num:
#     n = n*fact
#     fact = fact+1
# print(n)

# for loop
# 1.Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# 2.Write a program to print multiplication table of a given number
# 3. Count the total number of digits in a number with out string conversion
# 4. Write a program to display all prime numbers within a range 10 to 80.
# 5. Display Fibonacci series up to 10 terms


# #while
#
# 1.Write program print 10 even numbers using while loop?
# 2.Write a program to display the first 7 multiples of 7.
# 3.Write a program that appends the square of each number to a new list.





