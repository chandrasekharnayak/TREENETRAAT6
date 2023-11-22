# #in fixture scope is 4 type :- function(default),session, module, and class
#
# import pytest
#
# # function level fixture
# @pytest.fixture
# def setup_function():
#     print('\Setting up for function')
#     yield
#     print('\n Teardown after function')
#
#
# #class level fixture
#
# @pytest.fixture(scope='class')
# def setup_class():
#     print('\Setting up for function')
#     yield
#     print('\n Teardown after function')
#
# @pytest.fixture(scope='module')
# def setup_module():
#     print('\Setting up for function')
#     yield
#     print('\n Teardown after function')


#----------------------

import pytest
import os

@pytest.fixture(scope='class')
def file_data():

    file_path='file_data.txt'
    with open(file_path,'w') as f:
        f.write("hello,world")
    print('setup working')
    yield file_path

    try:
        pass
        # os.remove(file_path)
    except FileNotFoundError as msg:
        print(msg)
    finally:
        print('tear down working')






