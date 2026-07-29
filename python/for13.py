#calculo de juros simples
capital = float(input("Informe o seu capital: "))
juros = 0.310
saldo = capital

# repete o cálculo durante 12 meses
for mes in range(1, 13):
    #soma os juros simples ao saldo
    saldo += capital * juros
    #verifica se é o ultimo mes
    if mes == 12:
        print(f"Mes {mes}: saldo final: R${saldo: .2f}")
    else:
        print(f"Mes {mes}: R$ {saldo: .2f}")