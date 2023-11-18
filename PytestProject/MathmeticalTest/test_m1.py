import pytest

def add(a,b):
    return a+b

@pytest.mark.parametrize('input_a,input_b,excepted_result',
                         [(1,2,3),
                          (0,0,0),
                          (-1,-2,-3),
                          (-1,1,0),
                          (-1,-10,11)]
                         )
def test_add(input_a,input_b,excepted_result):
    acutal_result = add(input_a,input_b)
    assert acutal_result == excepted_result





# Test Data