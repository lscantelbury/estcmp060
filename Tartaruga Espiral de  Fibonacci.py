import turtle
import math

# Função para desenhar os quadrados fibonacci
def plotar_fibonacci(n):
    a = 0
    b = 1
    quadrado_a = a
    quadrado_b = b
    # Características da tartaruga.
    tartaruga.shape("turtle")
    tartaruga.pencolor("green")
    tartaruga.pensize(3)
    # Diretrizes para a tartaruga desenhar
    # os quadrados conforme a escala/fator
    # definidos.
    tartaruga.forward(b * fator)
    tartaruga.left(90)
    tartaruga.forward(b * fator)
    tartaruga.left(90)
    tartaruga.forward(b * fator)
    tartaruga.left(90)
    tartaruga.forward(b * fator)
    # Transformando o próximo quadrado a ser
    # desenhado na soma dos quadrados anteriores,
    # iniciando a sequência de fibonacci.
    temp = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = temp
    # Loop para desenhar os quadrados conforme
    # o input do usuário.
    for i in range(1, n):
        tartaruga.backward(quadrado_a * fator)
        tartaruga.right(90)
        tartaruga.forward(quadrado_b * fator)
        tartaruga.left(90)
        tartaruga.forward(quadrado_b * fator)
        tartaruga.left(90)
        tartaruga.forward(quadrado_b * fator)
        # Transformando o próximo quadrado a ser
        # desenhado na soma dos quadrados anteriores
        # continuando a sequência de fibonacci.
        temp = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = temp
    # Retornando a tartaruga para o ponto
    # inicial parar dar início ao desenho
    # da espiral.
    tartaruga.up()
    tartaruga.setposition(fator, 0)
    tartaruga.seth(0)
    tartaruga.down()
    # Cor e tamanho do traço.
    tartaruga.pencolor("red")
    tartaruga.pensize(1)

    tartaruga.left(90)
    # Loop para desenho da espiral.
    for i in range(n):
        print(b)
        x = math.pi * b * fator / 2
        x /= 90
        for j in range(90):
            tartaruga.forward(x)
            tartaruga.left(1)
        temp = a
        a = b
        b = temp + b

# Escala de tamanho que achei mais apropriada. 
fator = 5

while True:

    #Input de algarismos desejados pelo usuário.
    quantidade_de_algarismos = int(input('Digite o número de algarismos '\
        'na sua sequência de Fibonacci:'))

    if quantidade_de_algarismos > 0:
        print("Espiral de Fibonacci para", quantidade_de_algarismos, "algarismos:")
        tartaruga = turtle.Turtle()
        tartaruga.speed(250)
        plotar_fibonacci(quantidade_de_algarismos)
        turtle.done()

    else:
        print("Digite um número maior que 0!")
        continue

