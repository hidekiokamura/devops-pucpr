from contador import Contador

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
        print("0Opção inválida")