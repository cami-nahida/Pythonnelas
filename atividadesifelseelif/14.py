valor = float(input("colocar valor"))
desconto20 = 20
desconto10 = 10

descoProduto = (valor * desconto20)/100
descoProduto = (valor * desconto10)/100

final = valor - desconto10
final2 = valor - desconto20

if final >= 500:
    print("ganhou 10%, o valor final será de ", final , "R$")


elif final2 >= 200:
    print("ganhou 20%, o valor final será de ", final2 , "R$")

else:
    print("Infelizmente, não teve desconto", valor, "R$")
