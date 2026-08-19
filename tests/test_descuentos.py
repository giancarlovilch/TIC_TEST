import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from descuentos import calcular_descuento


def test_descuento_20_porciento():
    assert calcular_descuento(100, 20) == 80


def test_descuento_0_porciento():
    assert calcular_descuento(50, 0) = 50


def test_descuento_precio_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(-10, 20)


def test_descuento_porcentaje_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(100, -5)
