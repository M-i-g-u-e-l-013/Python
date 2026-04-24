import random
import time

def lin():
    print ("-=-" * 16)
    
FORCA = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

PALAVRAS = ["python", "computador", "programacao", "desenvolvedor", "algoritmo"]


def escolher_palavra():
    return random.choice(PALAVRAS)


def mostrar_palavra(palavra, letras_corretas):
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra])


def jogar():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 0
    max_tentativas = len(FORCA) - 1

    print("=== JOGO DA FORCA ===")

    while tentativas < max_tentativas:
        print(FORCA[tentativas])
        print("Palavra:", mostrar_palavra(palavra, letras_corretas))
        print("Erradas:", " ".join(letras_erradas))

        tentativa = input("Digite uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Digite apenas UMA letra válida!")
            continue

        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra!")
            continue

        if tentativa in palavra:
            letras_corretas.add(tentativa)
        else:
            letras_erradas.add(tentativa)
            tentativas += 1

        if all(letra in letras_corretas for letra in palavra):
            print("\n🎉 Você venceu!")
            print("Palavra:", palavra)
            return

    print(FORCA[tentativas])
    print("\n💀 Você perdeu!")
    print("A palavra era:", palavra)


def main():
    while True:
        jogar()

        op = input("\nJogar novamente? (s/n): ").lower()
        if op != "s":
            print("Encerrando...")
            break


if __name__ == "__main__":
    main()