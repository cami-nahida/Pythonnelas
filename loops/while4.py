#listas de nomes
nomes = ["Cami"," Mile","Cammie","Nahida", "Waguri"," joana"]
#Cami =0, Mile = 1, Cammie = 2, Nahida= 3 e Waguri= 4 
#variável contador
contador = 0
#indice inicial
indice = 0
#Enquanto existir item na lista, len() conta quantas palavras tem
while indice < len(nomes):
    contador += 1
    indice += 1

print(f"Quantidade de nomes:  {contador}")
    