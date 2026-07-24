peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))

imc= peso / (altura * altura)
if imc < 18.5:
    print("Indice Abaixo")
elif imc < 25:
    print("Indice Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")