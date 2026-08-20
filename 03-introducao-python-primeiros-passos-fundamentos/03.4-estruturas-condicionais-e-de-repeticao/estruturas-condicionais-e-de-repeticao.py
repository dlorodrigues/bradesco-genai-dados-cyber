# 03.4-estruturas-condicionais-e-de-repeticao.py

# 1. Indentação e Estruturas Condicionais (if / elif / else)
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
opcao = int(input("[1] Sacar\n[2] Extrato\nEscolha uma opção: "))

if opcao == 1:
    if saldo >= saque:
        saldo -= saque
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
    else:
        print("Saldo insuficiente para o saque.")
elif opcao == 2:
    print(f"Seu saldo atual é R$ {saldo:.2f}")
else:
    print("Opção inválida.")

# 2. Operador Ternário
status_saque = "Sucesso" if saldo >= saque else "Falha"
print(f"Status do Processamento: {status_saque}")

# 3. Estruturas de Repetição (for com range)
print("\n--- Exibindo Tabuada do 5 ---")
for numero in range(1, 11):
    print(f"5 x {numero} = {5 * numero}")

# 4. Estrutura de Repetição (while com break e continue)
print("\n--- Menu Interativo (while) ---")
contador = 0
while True:
    contador += 1
    if contador == 2:
        continue  # Pula a execução quando o contador for 2
    
    print(f"Execução número: {contador}")
    if contador >= 4:
        break  # Interrompe o loop