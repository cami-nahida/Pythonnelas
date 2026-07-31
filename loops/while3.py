numero = int(input("Digite um numero: "))

contador = 1

#Enquanto o contador for menor ou igual a10
while contador <= 10:
    #calcular a multiplicação
    resultado = numero * contador
    #exibir o resultado
    print(f"{numero} X {contador}= {resultado}")
    contador += 1