import random
import string


def gerar_senha(tamanho=12, usar_simbolos=True):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    caracteres = letras + numeros
    if usar_simbolos:
        caracteres += simbolos

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    print("=== GERADOR DE SENHAS ===")

    tamanho = int(input("Tamanho da senha: "))
    usar = input("Incluir símbolos? (s/n): ").lower() == "s"

    senha = gerar_senha(tamanho, usar)

    print(f"\nSenha gerada: {senha}")


if __name__ == "__main__":
    main()