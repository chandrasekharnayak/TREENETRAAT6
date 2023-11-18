import os
import pytest

@pytest.fixture
def file_opeartion(request):
    '''setup (precondition):- Open the file in writre mode'''
    file_path = 'test_file.txt'
    with open(file_path,'w') as file:
        file.write('Hi, Treenetra AT-6')

    yield file_path

    #Teardown(postcondition) :- Close the file after the test

    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass


    # if request.node.rep_call.failed:
    #     print('\n Teardown:- Test Failed , keep the file for insepction')
    # else:
    #     print('\Teardown:- Test Passed, removing the file ')
    #     # Remove the file after successfull test



#open flipkart.in
