import time
import random


def lin():
    print("-=-" * 16)


def msg(texto):
    lin()
    print(texto)
    lin()


def entrada_int(mensagem, opcoes=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if opcoes and valor not in opcoes:
                print("Opção inválida!")
            else:
                return valor
        except ValueError:
            print("Erro! Digite apenas números!")


def menu():
    msg("==== JOGO DA ADIVINHAÇÃO ====")
    print("[ 1 ] - Jogar")
    print("[ 2 ] - Sair")
    return entrada_int("Sua opção: ", [1, 2])


def jogar():
    vitorias = 0
    derrotas = 0

    for rodada in range(1, 11):
        msg(f"Rodada {rodada}/10")

        numero = random.randint(1, 10)

        print("Estou pensando em um número de 1 a 10")
        palpite = entrada_int("Seu palpite: ")

        print("1...")
        time.sleep(0.5)
        print("2...")
        time.sleep(0.5)
        print("3...")
        time.sleep(0.5)

        if palpite == numero:
            msg(f"Você acertou! Número: {numero}")
            vitorias += 1
        else:
            msg(f"Você errou! Número era: {numero}")
            derrotas += 1

        print(f"Placar: {vitorias} Vitórias / {derrotas} Derrotas")

    msg("Limite de rodadas atingido!")

    print("Deseja continuar?")
    print("[ 1 ] - Sim")
    print("[ 2 ] - Não")

    return entrada_int("Sua opção: ", [1, 2])


def main():
    while True:
        escolha = menu()

        if escolha == 2:
            print("Encerrando...")
            time.sleep(1)
            break

        while True:
            continuar = jogar()

            if continuar == 2:
                print("Encerrando...")
                time.sleep(1)
                return


if __name__ == "__main__":
    main()