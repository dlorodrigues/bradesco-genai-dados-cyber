# 03.2_conhecendo_a_linguagem.py

# Constantes (convenção em letras maiúsculas)
TAXA_CONVERSAO_USD = 5.20

# Entradas de dados e conversão de tipos
nome = input("Digite o nome do usuário: ")
idade = int(input("Digite sua idade: "))
saldo_reais = float(input("Digite o saldo em Reais (R$): "))

# Processamento
saldo_dolares = saldo_reais / TAXA_CONVERSAO_USD
maior_de_idade = idade >= 18

# Saída de dados formatada
print("-" * 30)
print("RESUMO DO CADASTRO", end="\n\n")
print(f"Usuário: {nome}", f"Maior de idade: {maior_de_idade}", sep=" | ")
print(f"Saldo em R$: R$ {saldo_reais:.2f}")
print(f"Saldo em USD: $ {saldo_dolares:.2f}")
print("-" * 30)