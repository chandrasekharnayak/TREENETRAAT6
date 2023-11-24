# # def test_addition(setup_function):
# #     result = 2+4
# #     assert result == 6
#
#
# class TestMathOperation:
#     def test_multiplication(self,setup_class):
#         result = 6*4
#         assert result == 24
#
#
# def test_module1(setup_module):
#
# def test_module2(setup_module)
# def test_module3(setup_module)

# write some in file
#read this file
#read test
# remove
import pytest

class TestFileOpeartionsClass:
    def test_read_file_claas(self,file_data):
        with open(file_data,'r') as file:
            data = file.read()
        print(data)
        assert "hello,world" in data

@pytest.mark.skip
def test_1():
    pass

@pytest.mark.skipif(reason='No Required')
def test_2():
    pass

@pytest.mark.xfail
def test_3():
    pass

#bus program:- oops - 173 - 212
#student 316 - 363






