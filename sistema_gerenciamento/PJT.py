import json
import os


# ================= UTIL =================
def carregar(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)


def entrada_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido!")


# ================= CLIENTES =================
def cadastrar_cliente(clientes):
    nome = input("Nome: ")
    email = input("Email: ")

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "email": email
    }

    clientes.append(cliente)
    print("Cliente cadastrado!")


def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for c in clientes:
        print(c)


def atualizar_cliente(clientes):
    id_ = entrada_int("ID do cliente: ")
    for c in clientes:
        if c["id"] == id_:
            c["nome"] = input("Novo nome: ")
            c["email"] = input("Novo email: ")
            print("Atualizado!")
            return
    print("Cliente não encontrado.")


def deletar_cliente(clientes):
    id_ = entrada_int("ID do cliente: ")
    for c in clientes:
        if c["id"] == id_:
            clientes.remove(c)
            print("Removido!")
            return
    print("Cliente não encontrado.")


# ================= PRODUTOS =================
def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = entrada_int("Quantidade em estoque: ")

    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    print("Produto cadastrado!")


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto.")
        return
    for p in produtos:
        print(p)


def atualizar_produto(produtos):
    id_ = entrada_int("ID do produto: ")
    for p in produtos:
        if p["id"] == id_:
            p["nome"] = input("Novo nome: ")
            p["preco"] = float(input("Novo preço: "))
            p["estoque"] = entrada_int("Novo estoque: ")
            print("Atualizado!")
            return
    print("Produto não encontrado.")


def deletar_produto(produtos):
    id_ = entrada_int("ID do produto: ")
    for p in produtos:
        if p["id"] == id_:
            produtos.remove(p)
            print("Removido!")
            return
    print("Produto não encontrado.")


# ================= MENU =================
def menu():
    print("\n=== SISTEMA DE GERENCIAMENTO ===")
    print("1 - Clientes")
    print("2 - Produtos")
    print("0 - Sair")
    return entrada_int("Escolha: ")


def menu_crud(tipo):
    print(f"\n--- {tipo.upper()} ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Voltar")
    return entrada_int("Escolha: ")


# ================= MAIN =================
def main():
    clientes = carregar("clientes.json")
    produtos = carregar("produtos.json")

    while True:
        op = menu()

        if op == 1:
            while True:
                op2 = menu_crud("clientes")

                if op2 == 1:
                    cadastrar_cliente(clientes)
                elif op2 == 2:
                    listar_clientes(clientes)
                elif op2 == 3:
                    atualizar_cliente(clientes)
                elif op2 == 4:
                    deletar_cliente(clientes)
                elif op2 == 0:
                    break

                salvar("clientes.json", clientes)

        elif op == 2:
            while True:
                op2 = menu_crud("produtos")

                if op2 == 1:
                    cadastrar_produto(produtos)
                elif op2 == 2:
                    listar_produtos(produtos)
                elif op2 == 3:
                    atualizar_produto(produtos)
                elif op2 == 4:
                    deletar_produto(produtos)
                elif op2 == 0:
                    break

                salvar("produtos.json", produtos)

        elif op == 0:
            print("Saindo...")
            break


if __name__ == "__main__":
    main()