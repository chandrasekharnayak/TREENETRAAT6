from TREENETRA_AT_6.PytestProject.Fixture.FixtureScope.math_operation import add,multiply,divide

import pytest

@pytest.mark.smoke
def test_add():
    assert add(2,3) == 5
    assert add(0,0) == 0
    assert add(2,-2) == 0
    assert add(-2,-2) == -4
    assert add(-3,2) == -1
    # assert add(8,9) == 18

@pytest.mark.skip
def test_divide():
    assert divide(3,3)==1.0

@pytest.mark.skipif(reason='due no work of this function, want to skip')
def test_function():
    pass

@pytest.mark.xfail
def test_function1():
    assert True == False

@pytest.mark.smoke
def test_divide_zero_division():
    try:
        divide(5,0)
    except ZeroDivisionError as e:
        assert str(e)== 'Cannot divide'

#pip install pytest pytest-xdist

# pytest  -n number --dist=loadscope --tx=auto