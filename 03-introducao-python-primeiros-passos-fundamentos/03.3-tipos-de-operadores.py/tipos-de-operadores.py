# 03.3-tipos-de-operadores.py

# 1. Operadores Aritméticos
saldo = 1000.0
deposito = 200.0
saque = 150.0
rendimento_percentual = 1.05

saldo_atual = (saldo + deposito - saque) * rendimento_percentual
resto = 10 % 3  # Módulo
potencia = 2 ** 3  # Exponenciação

# 2. Operadores de Atribuição
saldo_acumulado = 500
saldo_acumulado += 100  # Equivalente a saldo_acumulado = saldo_acumulado + 100

# 3. Operadores de Comparação & Lógicos
limite_saque = 500
tem_saldo = saldo_atual >= saque
dentro_do_limite = saque <= limite_saque
saque_permitido = tem_saldo and dentro_do_limite

# 4. Operadores de Identidade (is / is not)
opcao_selecionada = None
is_sem_opcao = opcao_selecionada is None

# 5. Operadores de Associação (in / not in)
frutas_permitidas = ["maçã", "banana", "laranja"]
fruta_desejada = "maçã"
tem_fruta = fruta_desejada in frutas_permitidas

# Saída de Resultados
print("=== TESTE DE OPERADORES PYTHON ===")
print(f"Saldo Atualizado: R$ {saldo_atual:.2f}")
print(f"Saque Permitido?: {saque_permitido}")
print(f"Opção é Nula?: {is_sem_opcao}")
print(f"Possui {fruta_desejada} no estoque?: {tem_fruta}")