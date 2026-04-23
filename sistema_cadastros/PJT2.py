import json
import os

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade
        }


class SistemaCadastro:
    def __init__(self, arquivo="usuarios.json"):
        self.arquivo = arquivo
        self.usuarios = self.carregar()

    def carregar(self):
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.usuarios, f, indent=4)

    def cadastrar_usuario(self, nome, email, idade):
        if any(u["email"] == email for u in self.usuarios):
            print("Email já cadastrado!")
            return

        usuario = Usuario(nome, email, idade)
        self.usuarios.append(usuario.to_dict())
        self.salvar()
        print("Usuário cadastrado com sucesso!")

    def listar_usuarios(self):
        for u in self.usuarios:
            print(f"{u['nome']} - {u['email']} - {u['idade']} anos")

    def buscar_usuario(self, email):
        for u in self.usuarios:
            if u["email"] == email:
                return u
        return None

    def remover_usuario(self, email):
        self.usuarios = [u for u in self.usuarios if u["email"] != email]
        self.salvar()
        print("Usuário removido!")


# Interface simples (terminal)
def menu():
    sistema = SistemaCadastro()

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Remover")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            sistema.cadastrar_usuario(nome, email, idade)

        elif op == "2":
            sistema.listar_usuarios()

        elif op == "3":
            email = input("Email: ")
            usuario = sistema.buscar_usuario(email)
            print(usuario if usuario else "Não encontrado")

        elif op == "4":
            email = input("Email: ")
            sistema.remover_usuario(email)

        elif op == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()