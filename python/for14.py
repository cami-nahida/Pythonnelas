#simulando um elevador
andarDestino = int(input("Qual andar? "))
for andar in range(1, andarDestino + 1):
    #verificar se chegou no destino
    if andar == andarDestino:
        print(f"chegou ao andar {andar}")
    else:
        print(andar)