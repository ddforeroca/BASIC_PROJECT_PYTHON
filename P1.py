#IDENTIFICADOR DE NUMEROS PARES E IMPARES
numero = int(input(" Ingrese el numero: "))

while numero < 100:
    numero = numero+1
    if numero%2 == 0:
        print(str(numero)+" "+" Es un numero par")
    else:
        print(str(numero)+" "+" Es un numero impar")
