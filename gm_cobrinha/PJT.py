import pygame
import random

# Inicializar
pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 200, 0)
vermelho = (200, 0, 0)

# Tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()
velocidade = 15

# Tamanho da cobra
tamanho_bloco = 10

font = pygame.font.SysFont(None, 30)


def mostrar_pontuacao(pontos):
    texto = font.render(f"Pontos: {pontos}", True, branco)
    tela.blit(texto, [10, 10])


def desenhar_cobra(lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])


def jogo():
    game_over = False
    game_close = False

    x = largura / 2
    y = altura / 2

    x_vel = 0
    y_vel = 0

    cobra = []
    comprimento = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not game_over:

        while game_close:
            tela.fill(preto)
            msg = font.render("Você perdeu! Pressione C para jogar novamente ou Q para sair", True, vermelho)
            tela.blit(msg, [50, altura / 2])
            mostrar_pontuacao(comprimento - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_vel = -tamanho_bloco
                    y_vel = 0
                elif evento.key == pygame.K_RIGHT:
                    x_vel = tamanho_bloco
                    y_vel = 0
                elif evento.key == pygame.K_UP:
                    y_vel = -tamanho_bloco
                    x_vel = 0
                elif evento.key == pygame.K_DOWN:
                    y_vel = tamanho_bloco
                    x_vel = 0

        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        x += x_vel
        y += y_vel
        tela.fill(preto)

        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        cobra.append(cabeca)

        if len(cobra) > comprimento:
            del cobra[0]

        for bloco in cobra[:-1]:
            if bloco == cabeca:
                game_close = True

        desenhar_cobra(cobra)
        mostrar_pontuacao(comprimento - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()


jogo()