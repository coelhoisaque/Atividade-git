# Programa simples para calcular IMC

print("--- Calculadora de IMC ---")

# Recebendo os dados do usuário
# Usamos float() porque peso e altura geralmente têm casas decimais
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibindo o resultado com duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Estrutura de decisão para classificar o resultado
      if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
