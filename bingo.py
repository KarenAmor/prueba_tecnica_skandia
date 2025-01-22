# A. Escriba un algoritmo que imprima los números del 1 al 100, pero con las siguientes consideraciones:
# Si el número es divisible por 3 y 5, imprime "bingo".
# Si el número es solo divisible por 3, imprime "Bin".
# Si el número es solo divisible por 5, imprime "Go".
# Si no es divisible ni por 3 ni por 5, imprime el número.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("bingo")
    elif i % 3 == 0:
        print("Bin")
    elif i % 5 == 0:
        print("Go")
    else:
        print(i)