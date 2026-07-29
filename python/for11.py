#caixa em um depósito
#Um laço que percorre as caixas de 1 a 10
for caixa in range(1, 11):
    #verificar se é a últma caixa
    if caixa == 10:
        print(f"Caixa {caixa}: última caixa conferida")
    else:
     print(f"Conferindo a caixa {caixa}")