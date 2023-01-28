"""
#Movimentando a turtle para frente 
t.forward(100)
#Rotacionar em x graus para a direita
t.right(90)
t.forward(100)
#Rotacionar em X graus para a esquerda
t.left(90)
t.forward(100)
#Movimentar a turtle para trás 
t.backward(200)
input()
"""

"""Criando um jogo utilizando Turtle e laços de repetição"""

from turtle import Turtle
#Inicializando uma Turtle
t = Turtle()
#Definindo a velocidade 
t.speed(1)
while True:
    distancia = int(input("Distancia a percorrer "))
    t.forward(distancia)
    rotacao_direita = int(input("Rotação para a direita ? "))
    t.right(rotacao_direita)
    voltando = int(input("Qual a distancia a ser retornada"))
    t.backward(voltando)
    rotacao_esquerda = int(input("Qual o valor de rotação esquerda"))
    t.left(rotacao_esquerda)
    encerra_programa = input("Digite S para encerrar o programa ")
    if encerra_programa == "S":
        break
    else:
        pass
   
