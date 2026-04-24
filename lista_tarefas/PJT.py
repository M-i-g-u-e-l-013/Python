import json
import os


ARQUIVO = "tarefas.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)


def listar(tarefas, filtro=None):
    print("\n=== TAREFAS ===")

    for t in tarefas:
        if filtro == "pendente" and t["concluida"]:
            continue
        if filtro == "concluida" and not t["concluida"]:
            continue

        status = "✔" if t["concluida"] else "✗"
        print(f"{t['id']} - {t['titulo']} [{status}]")


def adicionar(tarefas):
    titulo = input("Nova tarefa: ")
    tarefas.append({
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False
    })


def editar(tarefas):
    id_ = int(input("ID da tarefa: "))
    for t in tarefas:
        if t["id"] == id_:
            t["titulo"] = input("Novo título: ")
            return


def concluir(tarefas):
    id_ = int(input("ID da tarefa: "))
    for t in tarefas:
        if t["id"] == id_:
            t["concluida"] = True
            return


def main():
    tarefas = carregar()

    while True:
        print("\n=== TO-DO LIST ===")
        print("1 - Adicionar")
        print("2 - Listar todas")
        print("3 - Listar pendentes")
        print("4 - Listar concluídas")
        print("5 - Editar")
        print("6 - Concluir")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar(tarefas)
        elif op == "2":
            listar(tarefas)
        elif op == "3":
            listar(tarefas, "pendente")
        elif op == "4":
            listar(tarefas, "concluida")
        elif op == "5":
            editar(tarefas)
        elif op == "6":
            concluir(tarefas)
        elif op == "0":
            break

        salvar(tarefas)


if __name__ == "__main__":
    main()