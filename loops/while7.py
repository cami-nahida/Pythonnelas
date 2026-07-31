#Encontrando o maior divisor comum
a = 84
b = 36

#enquanto o menor numero for diferente de zero
while b!= 0:
    #calcula o resto da divisão de a por b
    resto = a % b
    
    a = b
    b = resto
    
print(f"MDC {a}")