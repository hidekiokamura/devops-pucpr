from contador import Contador

c = Contador()

while True:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Mostrar")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        c.incrementar()
    elif op == "2":
        c.decrementar()
    elif op == "3":
        print("Valor:", c.mostrar())
    elif op == "0":
        break
    else:
        print("Opção inválida")