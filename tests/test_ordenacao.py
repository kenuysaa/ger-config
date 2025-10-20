import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from ordenacao.bubbleSort import bubble_sort
from ordenacao.insertionSort import insertion_sort
from ordenacao.mergeSort import merge_sort
from ordenacao.quickSort import quick_sort
from ordenacao.selectionSort import selection_sort

ALGORITMOS = [
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort
]

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_vazia(algoritmo):
    assert algoritmo([]) == []

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_um_elemento(algoritmo):
    assert algoritmo([42]) == [42]

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_ja_ordenada(algoritmo):
    lista = [1, 2, 3, 4, 5]
    assert algoritmo(lista.copy()) == sorted(lista)

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_invertida(algoritmo):
    lista = [5, 4, 3, 2, 1]
    assert algoritmo(lista.copy()) == sorted(lista)

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_com_repetidos(algoritmo):
    lista = [4, 2, 5, 2, 3, 4, 1]
    assert algoritmo(lista.copy()) == sorted(lista)

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_negativos(algoritmo):
    lista = [-3, 0, -1, 5, 2, -2]
    assert algoritmo(lista.copy()) == sorted(lista)

@pytest.mark.parametrize("algoritmo", ALGORITMOS)
def test_lista_strings(algoritmo):
    lista = ["uva", "banana", "maçã", "laranja"]
    assert algoritmo(lista.copy()) == sorted(lista)
