import pytest

"""Prueba Ejercicio 1"""
from TP5 import valid_dni

def test_valid_dni():
    assert valid_dni("12345678") == True
    assert valid_dni("1234567") == True
    assert valid_dni("123456") == False



"""Prueba Ejercicio 2"""
from TP5 import word_length

def test_word_length():
    assert word_length("hola buenas tardes") == 6



"""Prueba Ejercicio 3""" #MAL
from TP5 import identificador

def test_identificador():
    assert identificador("Uriel", "Osmar", "Vera", "12345678") == "Uriel4123"
    assert identificador("Uriel", "", "Vera", "12345678")     == "Uriel4123"



"""Ejercicio 4"""
from TP5 import is_multiple

def test_is_multiple():
    assert is_multiple(2, 4) == True
    assert is_multiple(3, 4) == False



"""Ejercicio 5""" #MAL
from TP5 import average_temp

def test_average_temp():
    assert average_temp(20, 10) == 15
    assert average_temp(3, 12)  == 7.5



"""Ejercicio 6"""
from TP5 import spacing

def test_spacing():
    assert spacing("hola que tal")   == "h o l a   q u e   t a l"
    assert spacing("buenos dias")      == "b u e n o s   d i a s"



"""Ejercicio 7"""
from TP5 import max_min

def test_max_min():
    assert max_min([1, 2, 3, 4, 5, None]) == (1, 5)
    assert max_min([4, 232, 53, 47, 5, None]) == (4, 232)
    assert max_min([None, None, None]) is None



"""Ejercicio 8"""
from TP5 import area_perimeter

def test_area_perimeter():
    assert area_perimeter(1) == (3.14, 6.28)
    assert area_perimeter(2) == (12.57, 12.57)



"""Ejercicio 9"""
from TP5 import login

@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("usuario1", "asdasd", True),
        ("user1", "asdasd", True),
        ("usuario", "wasdwasd", False),
        ("usuario1", "asdasd", True),
    ]
)
def test_login(username, password, expected):
    assert login(username, password) == expected



"""Ejercicio 10"""
from TP5 import discount 

@pytest.mark.parametrize(
    "cart, expected_result",
    [
        (
            {
                "Memory RAM": {"price": 20.800, "discount": 5},
                "Processor": {"price": 90.500, "discount": 10},
                "Motherboard": {"price": 120.200, "discount": 15},
            },
            205.73,
        ),
    ]
)
def test_apply_discount(cart, expected_result):
    assert discount(cart) == expected_result



"""Ejercicio 11"""
from TP5 import modify_list

@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        (["Hola", "buenas", "tardes"], ["Hola@buenas@tardes"]),
    ]
)
def test_modify_list(input_list, expected_list):
    assert modify_list(input_list) == expected_list



"""Ejercicio 12"""
from TP5 import show_sentence

def test_show_sentence():
    result = show_sentence("hola que tal")
    assert result == {'hola': 4, 'que': 3, 'tal': 3}

    result = show_sentence("tenga un buen dia")
    assert result == {'tenga': 5, 'un': 2, 'buen': 4, 'dia': 3}



"""Ejercicio 14"""
from TP5 import is_prime

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True



"""Ejercicio 15"""   
from TP5 import factorial

def test_factorial():
    assert factorial(-1) == -1 
    assert factorial(0) == 1
    assert factorial(3) == 6



"""Ejercicio 16"""
from TP5 import frequency

def test_frequency():
    assert frequency(37617, 7) == 2
    assert frequency(61523, 6) == 1



"""Ejercicio 17"""
from TP5 import is_prime, sum_digits, frequency

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False

def test_sum_digits():
    assert sum_digits(123) == 6
    assert sum_digits(9876) == 30

def test_frequency():
    assert frequency(1122334, 3) == 3
    assert frequency(567876, 9) == 0