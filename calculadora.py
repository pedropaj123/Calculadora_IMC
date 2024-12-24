# Pegando dados de entrada
peso = float(input('Informe seu peso(kg)? ')) # Pegando número de peso
altura = float(input('Informe sua altura(exemplo: 1.75)? ')) # Pegando número de sua altura

# Calculo do IMC
def calcular_imc(peso, altura): 
    return peso / (altura ** 2)

# Indicando variável do calculo
imc = calcular_imc(peso, altura)

# Indicando a classificação do IMC
if imc <= 18.5:
    classificacao = "Abaixo do normal"
elif imc > 18.5 and imc <= 24.9:
    classificacao = "Normal"
elif imc > 24.9 and imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc > 29.9 and imc <= 34.9:
    classificacao = "Obesidade grau 1"
elif imc > 34.9 and imc <= 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

# Indicando Resultado
print (f"IMC:{imc:.2f}, Classificação:{classificacao}")