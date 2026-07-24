nota1 = float(input("digite a nota"))
nota2 = float(input("digite a nota"))
nota3 = float(input("digite a nota"))

media = (nota1 + nota2 + nota3)/ 3

if media >= 7:
    print("APROVADOO!")
elif media >= 5:
    print("RECUPERAÇÃOO!")
else: 
    print("REPROVADO!")