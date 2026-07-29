#parcelas de um financiamanto
valorTotal = 2354
parcelas = 12

#calcula o valor de cada parcela
valorParcela = valorTotal / parcelas

#percorrer todas as parcelas
for parcela in range(1, parcelas + 1):
    #verifica se chegou na ultima parcela
    if parcela == parcelas:
        print(f"Parcela {parcela}: ultima parcela - R${valorParcela: .2F}")
    else:
        print(f"parcela {parcela}: R$ {valorParcela: .2F}")