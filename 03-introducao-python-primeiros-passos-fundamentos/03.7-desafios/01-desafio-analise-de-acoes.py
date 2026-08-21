# desafio-analise-de-acoes.py

# Leitura e parsing dos dados
entrada = input("Digite o preço de abertura e fechamento (ex: 10 15): ")
abertura_str, fechamento_str = entrada.split()

abertura = int(abertura_str)
fechamento = int(fechamento_str)

# Regra de negócio
if fechamento > abertura:
    resultado = "ALTA"
elif fechamento < abertura:
    resultado = "BAIXA"
else:
    resultado = "ESTAVEL"

print(resultado)