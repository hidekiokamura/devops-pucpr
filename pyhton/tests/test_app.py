import pytest
from main import soma, subtrai, divide, multiplica

# Teste 1: Função Soma (Positivo)
def test_soma_valores_corretos():
    resultado = soma(5, 5)
    assert resultado == 10

# Teste 2: Função Subtração (Positivo)
def test_subtrai_valores_corretos():
    resultado = subtrai(10, 4)
    assert resultado == 6

# Teste 3: Função Multiplicação (Positivo)
def test_multiplica_valores_corretos():
    resultado = multiplica(3, 4)
    assert resultado == 12

# Teste 4: Função Divisão (Positivo)
def test_divide_valores_corretos():
    resultado = divide(10, 2)
    assert resultado == 5

# Teste 5: Função Divisão por Zero (Tratamento de Exceção)
def test_divide_por_zero():
    # O pytest espera que um erro seja gerado quando tentamos dividir por zero
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)