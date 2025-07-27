"""
    4- Verificador de Ano Bissexto

    Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
    Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

try:
    ano = int(input("Digite um ano (ex: 2024): "))
    
    # Verifica ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido como número inteiro.")