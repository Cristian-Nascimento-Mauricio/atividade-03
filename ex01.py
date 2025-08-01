"""
    1- Classificador de Idade

    Crie um programa que solicite a idade do usuário e classifique-o 
    em uma das seguintes categorias: 

    *Criança (0-12 anos), 
    *Adolescente (13-17 anos), 
    *Adulto (18-59 anos) ou 
    *Idoso (60 anos ou mais).
"""

try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Você é Criança.")
    elif idade <= 17:
        print("Você é Adolescente.")
    elif idade <= 59:
        print("Você é Adulto.")
    else:
        print("Você é Idoso.")
except ValueError:
        print("Por favor, digite um número inteiro válido.")
        