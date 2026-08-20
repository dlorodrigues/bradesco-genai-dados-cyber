# 03.5-manipulando-strings.py

# 1. Métodos Úteis da Classe String
curso = "  pYtHon  "
print(curso.upper())      # "  PYTHON  "
print(curso.lower())      # "  python  "
print(curso.title())      # "  Python  "
print(curso.strip())      # "pYtHon"
print(curso.center(20, "#")) # "#####  pYtHon  #####"
print(".".join(["P", "y", "t", "h", "o", "n"])) # "P.y.t.h.o.n"

# 2. Interpolação de Variáveis
nome = "Douglas"
idade = 25
profissao = "Desenvolvedor"

print(f"Nome: {nome} | Idade: {idade} | Profissão: {profissao}")

# 3. Fatiamento de Strings [start:stop:step]
texto = "Douglas Luiz"

print(texto[0])         # Primeiro caractere: 'D'
print(texto[:7])        # Do início até o índice 6: 'Douglas'
print(texto[8:12])      # Do índice 8 ao 11: 'Luiz'
print(texto[::2])       # Passo de 2 em 2
print(texto[::-1])      # String invertida

# 4. String de Múltiplas Linhas (Triple Quotes)
mensagem_menu = f"""
================ MENU ===============
1 - Sacar
2 - Depositar
3 - Sair
=====================================
Usuário logado: {nome}
"""
print(mensagem_menu)