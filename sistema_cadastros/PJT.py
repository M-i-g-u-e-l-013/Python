def lin():
    print("-=-" * 16)


print("==== CADASTROS EM PYTHON ====")

pessoas = []
pessoa = {}

while True:
    pessoa["nome"] = input("Digite seu nome: ").strip()

    while True:
        try:
            idade = int(input("Digite a sua idade: ").strip())
            if idade >= 0:
                pessoa["idade"] = idade
                break
            else:
                print("Digite uma idade válida!")
        except ValueError:
            lin()
            print("Erro! Digite apenas números.")
            lin()

    while True:
        pessoa["sexo"] = input("Digite seu sexo [M/F]: ").strip().upper()[0]
        if pessoa["sexo"] in ("M", "F"):
            break
        lin()
        print("Ops! Digite um sexo válido")
        lin()

    pessoas.append(pessoa.copy())
    pessoa.clear()

    lin()
    print("Cadastro concluído com sucesso")
    lin()

    while True:
        resp = input("Deseja continuar [S/N]: ").strip().upper()[0]
        if resp in ("S", "N"):
            break
        print("Opção inválida! Digite S ou N")
        lin()

    if resp == "N":
        break

# ================= RESULTADOS =================

print("==== HOMENS CADASTRADOS ====")
for p in pessoas:
    if p["sexo"] == "M":
        print(f"{p['nome']} - {p['idade']} anos")

print("==== MULHERES CADASTRADAS ====")
for p in pessoas:
    if p["sexo"] == "F":
        print(f"{p['nome']} - {p['idade']} anos")

print("==== HOMENS MENORES DE IDADE ====")
for p in pessoas:
    if p["sexo"] == "M" and p["idade"] < 18:
        print(f"{p['nome']} - {p['idade']} anos")

print("==== MULHERES MENORES DE IDADE ====")
for p in pessoas:
    if p["sexo"] == "F" and p["idade"] < 18:
        print(f"{p['nome']} - {p['idade']} anos")

print("==== MÉDIA DE IDADE DOS CADASTRADOS ====")

if len(pessoas) > 0:
    soma_idade = sum(p["idade"] for p in pessoas)
    media = soma_idade / len(pessoas)
else:
    media = 0

print(f"Quantidade de pessoas cadastradas: {len(pessoas)}")
print(f"Média de idade: {media:.2f}")