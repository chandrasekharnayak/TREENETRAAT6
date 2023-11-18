#open a file write something
#then read the data and test data is string or not
#failed
#close

from TREENETRA_AT_6.PytestProject.Fixture.conftest import file_opeartion

def test_file_content_is_string(file_opeartion):
    file_path = file_opeartion

    with open(file_path,'r') as file:
        data = file.read()

    assert isinstance(data,str)
