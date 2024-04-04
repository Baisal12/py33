import pytest

from main import add_one, division, is_palindrom


def test_answer():
    # оператор assert - встроенный оператор пайтон позволяющий отслеживать код.  Этот оператор пайтон принемайт условия и необезательное сообщения которая выходит при исключении AssertionError. исключениу выходит Folse, но если он встретит true то нечего не произайдет
    assert add_one(5) == 5 


def test_division():
    assert division(10, 5) == 2



@pytest.mark.parametrize(
    'a, b, res',
    [(10, 5, 2), (12, 6, 2), (9, 3, 3)]
)
def test_division2(a, b, res):
    assert division(a, b) == res 














































































