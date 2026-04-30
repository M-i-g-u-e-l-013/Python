import pyautogui
import time
import os
from datetime import datetime

# ======================================================
# BOT DE AUTOMAÇÃO DE TAREFAS EM PYTHON
# ======================================================
# Funções do bot:
# 1. Abrir programas
# 2. Digitar automaticamente
# 3. Clicar automaticamente
# 4. Criar relatório TXT
# 5. Automatizar tarefas simples
# ======================================================

TEMPO_ESPERA = 3

def abrir_bloco_notas():
    print("Abrindo bloco de notas...")

    os.system("notepad")

    time.sleep(2)



def escrever_texto(texto):
    print("Escrevendo texto automaticamente...")

    pyautogui.write(texto, interval=0.05)


def pressionar_enter():
    pyautogui.press("enter")



def criar_relatorio():
    print("Criando relatório...")

    agora = datetime.now()

    relatorio = f"""
==============================
RELATÓRIO DE EXECUÇÃO DO BOT
==============================

Data: {agora.strftime('%d/%m/%Y')}
Hora: {agora.strftime('%H:%M:%S')}

Status: BOT EXECUTADO COM SUCESSO

==============================
"""

    with open("relatorio_bot.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)

    print("Relatório salvo com sucesso!")



def contagem_regressiva(segundos):
    print("\nPrepare a janela para automação...")

    for i in range(segundos, 0, -1):
        print(f"Iniciando em {i}...")
        time.sleep(1)



def executar_bot():

    print("=" * 50)
    print("BOT DE AUTOMAÇÃO PYTHON")
    print("=" * 50)

    contagem_regressiva(TEMPO_ESPERA)

    abrir_bloco_notas()

    escrever_texto("Olá! Este texto foi escrito automaticamente por um BOT em Python.")

    pressionar_enter()

    escrever_texto("Python é excelente para automação de tarefas.")

    pressionar_enter()

    escrever_texto("Este projeto utiliza PyAutoGUI.")

    pressionar_enter()

    escrever_texto("Automação concluída com sucesso!")

    # Criar relatório
    criar_relatorio()

    print("\nBOT FINALIZADO!")


# -------------------------------
# EXECUÇÃO
# -------------------------------
if __name__ == "__main__":
    executar_bot()
