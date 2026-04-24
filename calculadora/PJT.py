import json
import os


ARQUIVO = "historico.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar(hist):
    with open(ARQUIVO, "w") as f:
        json.dump(hist, f, indent=4)


def calcular(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b


def main():
    historico = carregar()

    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Calcular")
        print("2 - Ver histórico")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            a = float(input("Número 1: "))
            operador = input("Operador (+ - * /): ")
            b = float(input("Número 2: "))

            resultado = calcular(a, operador, b)

            conta = f"{a} {operador} {b} = {resultado}"
            historico.append(conta)
            salvar(historico)

            print("Resultado:", resultado)

        elif op == "2":
            print("\nHistórico:")
            for h in historico:
                print(h)

        elif op == "0":
            break


if __name__ == "__main__":
    main()