"""Pruebas unitarias de la calculadora."""
import pytest

from calculadora import dividir, multiplicar, restar, sumar


def test_sumar():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(1, 0)




def test_potencia():
    assert potencia(2, 3) == 8