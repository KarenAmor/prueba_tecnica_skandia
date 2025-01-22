# B. Escriba un algoritmo para calcular e imprimir los primeros 50 números primos. 

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Contador para los primeros 50 números primos
contador = 0
numero = 2

while contador < 50:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1