import turtle
import math


def plotar_fibonacci(n):
    a = 0
    b = 1
    quadrado_a = a
    quadrado_b = b

    tartaruga.shape("turtle")
    tartaruga.pencolor("green")
    tartaruga.pensize(3)

    tartaruga.forward(b * fator)
    tartaruga.left(90)
    tartaruga.forward(b * fator)
    tartaruga.left(90)
    tartaruga.forward(b * fator)
    tartaruga.left(90)
    tartaruga.forward(b * fator)

    temp = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = temp

    for i in range(1, n):
        tartaruga.backward(quadrado_a * fator)
        tartaruga.right(90)
        tartaruga.forward(quadrado_b * fator)
        tartaruga.left(90)
        tartaruga.forward(quadrado_b * fator)
        tartaruga.left(90)
        tartaruga.forward(quadrado_b * fator)

        temp = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = temp
    tartaruga.up()
    tartaruga.setposition(fator, 0)
    tartaruga.seth(0)
    tartaruga.down()

    tartaruga.pencolor("red")
    tartaruga.pensize(1)

    tartaruga.left(90)
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


fator = 5


quantidade_de_algarismos = int(input("Digite o número de algarismos \
    na sua sequência de Fibonacci:"))

if quantidade_de_algarismos > 0:
    print("Espiral de Fibonacci para", quantidade_de_algarismos, "algarismos:")
    tartaruga = turtle.Turtle()
    tartaruga.speed(250)
    plotar_fibonacci(quantidade_de_algarismos)
    turtle.done()

else:
    print("Digite um número maior que 0:")
