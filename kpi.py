# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

input_name = input ("Digite seu nome: ")
input_salary = float(input("Digite o valor do seu salário: "))
input_bonus = float(input("Digite o seu bônus: "))
fixo_bonus = 1000
final_salary = fixo_bonus + input_salary * input_bonus
print(f'O valor do salário do {input_name} é de {final_salary}')