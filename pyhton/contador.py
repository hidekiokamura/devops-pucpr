class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

    def decrementar(self):
        self.valor -= 1

    def mostrar(self):
        return self.valor