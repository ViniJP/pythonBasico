# Básico de Python

# Comentário em uma linha
"""
Comentários em
mais de uma
linha!
"""

""" Módulos
Um módulo é um arquivo contendo definições
e instruções Python que podem ser importados para
utilização de seus recursos
https://docs.python.org/pt-br/3/tutorial/modules.html
"""
#import operacoes
#from operacoes import somar, subtrair, nome_empresa
from exemplo_modulo import subtrair, nome_empresa

#print(operacoes.subtrair(10, 2))
#print(somar(1, 3))
#print(subtrair(1, 3))
print(nome_empresa)
#print(__name__)

"""
Módulos padrão:
Um módulo é um arquivo contendo definições
e instruções Python que podem ser importados para
utilização de seus recursos
Permitem expandir as funcionalidades
da linguagem além dos recursos padrões
1) É possível utilizar módulos padrões do Python
2) É possível intalar módulos
https://docs.python.org/pt-br/3/py-modindex.html
"""
#import random
#from random import randint
#print(random.randint(1, 10))
#print(randint(1, 10))

#from functools import reduce

# from datetime import datetime as date
# print(date.now())

# from math import sqrt
# print(sqrt(64))

"""
PIP
pip é um sistema de gerenciamento de pacotes em Python
"""
#pip3 install --upgrade pip
#import pymysql

# Try catch
lista = [0,1]
try:
    print(lista[2])
except Exception as erro:
    print('Não existe item na lista')
else:
    print('não deu erro')
finally:
    print("sempre executa")


# Função que define um erro
def dividir(n1, n2):
    try:
        print(f'resultado: {n1 / n2}' )
    except ZeroDivisionError as erro:
        raise  # lança uma exceção

## For:
# Lista de Postagens utilizadas
postagens = [
    "Postagem 1",
    "Postagem 2",
    "Postagem 3",
    "Postagem 4"
]

# Para cada postagem dentro da lista de postagens, executa o print
for postagem in postagens:
    print(postagem + '\n')  # Quebra de linha: \n

# 2 Variaveis em uma unica linha
nome, nome2 = "Vini", "Vinicius"

# For com o índice
for indice, postagem in enumerate(postagens):
    print(f'{indice} - {postagem}')

# Faz um for ate o indice 11
for indice in range(0, 11):  # (11), (postagens)
    print(indice)


# Função - usa-se a palavra def:
# O Python usa os espaços para identificar um bloco de código como no exemplo abaixo
# A linha que está identada com espaço, está dentro da função print
def print_hello():
    print("Hello World")
    return "ok"


retorno = print_hello()
print(retorno)


# Função com parâmetros variáveis (Packing) (usa o formato tuple)
def somar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    print(f'total somar: {total}')


somar(10, 20, 5, 10)


# Função com parametros em lista (Unpacking)
def calcular_media(nota1, nota2, ponto_extra=0):  # Ultimo valor é opcional
    media = (nota1 + nota2) / 2 + ponto_extra
    print(f'Média: {media}')


notas = [10, 8]
calcular_media(*notas, ponto_extra=1)  # Ultimo valor é nomeado


# Funções com outra função como parametro
carrinho_compras = [
    {'produto': 'Fone de Ouvido', "preco": 500},
    {'produto': 'Controle Xbox', "preco": 400},
    {'produto': 'Celular', "preco": 800}
]


def calcular_somado(lista, funcao):
    print(" função calcular_somado")
    for produto in lista:
        item_somado = funcao(produto['preco'], 10)
        print(item_somado)


calcular_somado(carrinho_compras, somar)


# Função lambda - anônima
sub = lambda a, b: a - b # Função Lambda atribuida à variavel
print(sub(1, 3))


# Função Map - percorre a lista e para cada elemento da lista utiliza a função lambda
lista_numero = [10, 20, 30]
nova_lista = map(lambda n: n * 2, lista_numero)
print("\n" + "função map")
print(list(nova_lista))


# Função Filter - filtra dados de acordo com uma condição True ou False
nova_lista_filter = filter(lambda n: n <= 20, lista_numero)
print("\n" + "função filter")
print(list(nova_lista_filter))


# Função reduce - acumula e reduz uma lista em um único valor (deve ser importada)
from functools import reduce
funcao = lambda acumulador, item: acumulador + item
resultado = reduce(funcao, lista_numero, 5)
print("\n" + "função reduce")
print(resultado)


# Função list comprehension
lista_comprehension = [item for item in lista_numero if item >= 20]
# Lê-se o código acima como [item (onde se coloca a variavel) for
# item na lista_numero (percorre a lista_numero) se o item for
# maior ou = a 20
print("\n" + "função list comprehension")
print(lista_comprehension)

