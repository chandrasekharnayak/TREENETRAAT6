#Interative statement  :- for and while

# li =  [10,20,30,40,50]

# for var in con:
#     statement
#
# for i in li:
#     print(i+5)

# di = {'Name':'A','Age':20,'Place':'BBSR'}
#
# for k,v in di.items():
#     print(v)


# li = [
#     [9,19,29,39],
#     [7,17,27,37],
#     [8,18,28,38]
# ]

# for i in li:
#     for j in i:
#         print(j)


# school = [['A','B','C'],['AA','BB','CC'],['AAA','BBB','CCC']]
#
# for i in school:
#     for j in i:
#         print(j)


li = [
    {'SECTION':'A','Class Teacher':'Mohanty Sir','Students':['A','B','C']},
    {'SECTION':'B','Class Teacher':'Tripathy Sir','Students':['AA','BB','CC']},
    {'SECTION':'C','Class Teacher':'Sahoo Sir','Students':['AAA','BBB','CCC']}
]

# for i in li:
#     if i.get('SECTION') =='A':
#         print(i.get('Class Teacher'))

# for i in li:
#     if i.get('SECTION')=='C':
#         for s in i.get('Students'):
#             print(s)

# s = set()
# for i in li:
#     for k,v in i.items():
#         if i.get("SECTION")=='C':
#             for j in i.get('Students'):
#                 s.add(j)
#
# print(s)

s ='ABBABDCDC'

# op = 2A3B2C2D
# di = {}
# for i in s:
#     di.update({i:s.count(i)})
# print(di)
# st = ''
# for k,v in di.items():
#     st =st+str(v)+k
# print(st)

#formkeys

# v = 20
#
# st = ('A','B','C')
# di = dict.fromkeys(st,v)
# print(di)
# range(start,end+1,step)
# li = []
# for i in range(1,11):
#     li.append(i)
# li.reverse()
# print(li)

#
# for i in range (11,2):
#     print(i)