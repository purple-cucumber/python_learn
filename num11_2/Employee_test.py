from Employees import Employee
import pytest
@pytest.fixture
def employee():
    employee_1 = Employee('zining','zhang',3000)
    return employee_1
def test_give_default_raise(employee_1):
    employee_1.give_raise()
    assert employee_1.salary == 8000
def test_give_cusstom_raise(employee_1):
    employee_1.give_raise(3000)
    assert employee_1.salary == 6000
