from contador import Contador

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    c = Contador()
    
    while True:
        print("\n+ - Somar")
        print("- - Subtrair")
        print("3 - Mostrar")
        print("0 - Sair")
        
        op = input("\nEscolha: ")
        
        if op == "+":
            c.incrementar()
        elif op == "-":
            c.decrementar()
        elif op == "3":
            print("Valor:", c.mostrar())
        elif op == "0":
            break
        else:
            print("Opção inválida")
