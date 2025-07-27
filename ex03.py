"""
    3- Conversor de Temperatura
    Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
    O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

try:
    valor = float(input("Digite o valor da temperatura: "))
    origem = input("Unidade de origem (C, F ou K): ").strip().upper()
    destino = input("Unidade de destino (C, F ou K): ").strip().upper()

    # converte tudo primeiro para Celsius
    if origem == "C":
        c = valor
    elif origem == "F":
        c = (valor - 32) * 5/9
    elif origem == "K":
        c = valor - 273.15
    else:
        print("Unidade de origem inválida.")
        exit()

    # de Celsius para unidade de destino
    if destino == "C":
        resultado = c
    elif destino == "F":
        resultado = c * 9/5 + 32
    elif destino == "K":
        resultado = c + 273.15
    else:
        print("Unidade de destino inválida.")
        exit()

    print(f"{valor:.2f}°{origem} equivalem a {resultado:.2f}°{destino}")

except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número para a temperatura.")


