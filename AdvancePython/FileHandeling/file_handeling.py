# # two type
# #text file (.txt,.word,.excel,.csv)
# #binary file (.png,.jpg,.mp4)
#
#
# # How to open a file
# # open()
#
# '''
# var = open('completed_path/location','mode')
#
# mode :- read(r),write(w),append(a)
# '''
#
# # file_1 = open('D:\\TREENETRA\\Treenetra_class_notes\\TREENETRA_AT-5\\class_3_reserved_words.txt','r')
# # data1 = file_1.readline()
# # print(data1)
# #
# # data2 = file_1.readline()
# # print(data2)
#
# #readlines()
# # data = file_1.readlines()
# # # print(data)
# #
# # for i in data:
# #     print(i)
#
# #read
# '''
# read()
# read(n)
# readline()
# readlines()
# '''
#
#
# #in python symbol role.special char
# #\n :- new line
# #\t :- tab
# #\b :- back space
# #\v
# # print('subham\vkumar')
#
# '''
# write()
# writelines()
# '''
#
# # file1 = open('D:\\TREENETRA\\Treenetra_class_notes\\TREENETRA_AT-5\\gogo.txt','w')
# # text = ['Hi , how are you? \n yes am fine gogo','ghioechwei\n','jchenweocdhi\n','dce\n']
# # file1.writelines(text)
# #
# # file1 = open('D:\\TREENETRA\\Treenetra_class_notes\\TREENETRA_AT-5\\gogo.txt','a')
# # text= 'Good people is always back Good'
# # file1.write(text)
#
#
# # how to handel binary
# # how to csv file and excel
# # how to do zip and unzip
#
# import csv
#
# # var = open('D:\\TREENETRA\\Treenetra_class_notes\\at_6_file_handeling.csv','w')
# # var.close()
# #
# # print(var.closed)
#
# #csv data write
# # import csv
# # with open('D:\\TREENETRA\\Treenetra_class_notes\\at_6_file_handeling.csv','w',newline='') as var:
# #     w = csv.writer(var)
# #     w.writerow(['E_no','E_name','E_salary'])
# #     number_of_emp_data = int(input('Number of employee:-'))
# #
# #     for i in range(number_of_emp_data):
# #         e_no = int(input('Enter your employee number'))
# #         e_name = input('Enter your employee name:-')
# #         e_salary = int(input('Enter emp slary:-'))
# #
# #         w.writerow([e_no,e_name,e_salary])
#
#
# # import csv
# # with open('D:\\TREENETRA\\Treenetra_class_notes\\at_6_file_handeling.csv','r') as var:
# #     data = csv.reader(var)
# #     for i in data:
# #         print(i)
#
#
# #Binary
#
# with open('D:\\TREENETRA\\Treenetra_class_notes\\Capture.PNG','rb') as var:
#     data = var.read()
#     # print(data)
#
# with open('D:\\TREENETRA\\Treenetra_class_notes\\cs_nayak.jpg','wb') as var1:
#     var1.write(data)
#
#
# ----------------------------

# --------------------ZIP and Unzip---------------------
# import zipfile

#zip
# var = zipfile.ZipFile('D:\\batch_6_find_handeling_notes.zip','w',zipfile.ZIP_DEFLATED) # zip a file with name
# # var.write('D:\\TREENETRA\\Treenetra_class_notes\\cs_nayak.jpg')
# var.write('C:\\Users\\chand\\PycharmProjects\\PythonAutomationAllBatch\\TREENETRA_AT_6\\AdvancePython\\FileHandeling\\file_handeling.py')


#unzip

# import zipfile
#
# file_name = 'new_zip_6.zip'
#
# var = zipfile.ZipFile(file_name,'r')
# print(var.printdir())
# var.extractall()
# print('Done')


#exception
#oops



