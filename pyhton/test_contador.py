from contador import Contador

def test_incrementar():
    c = Contador()
    c.incrementar()
    assert c.mostrar() == 1

def test_decrementar():
    c = Contador()
    c.decrementar()
    assert c.mostrar() == -1