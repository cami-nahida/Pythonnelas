#solicita uma palavra
palavra = input("Digite uma palavra: ")

#indice
indice = 0
#contador de letras
contador = 0

#Enquanto existir letra na pavra
while indice < len(palavra):
    #soma 1 contador 
    contador += 1
    
    #proxima letra
    indice += 1
print(f"quantidade de letras da palavra {palavra} é: {contador}")
