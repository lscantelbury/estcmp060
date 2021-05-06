import turtle

turtle.speed("fastest")

turtle.rt(-90)

angulo_de_divisão_fractal = 30

def plotar_fractal(tamanho_fractal, niveis_fractal):

    if niveis_fractal > 0:
        turtle.colormode(255)

        turtle.pencolor(0, 255//niveis_fractal, 0)

        turtle.fd(tamanho_fractal)
        turtle.rt(angulo_de_divisão_fractal)

        plotar_fractal(0.8 * tamanho_fractal,
             niveis_fractal-1)

        turtle.pencolor(0, 255//niveis_fractal, 0)

        turtle.lt(2 * angulo_de_divisão_fractal)

        plotar_fractal(0.8 * tamanho_fractal,
             niveis_fractal - 1)
        
        turtle.pencolor(0, 255//niveis_fractal, 0)

        turtle.rt(angulo_de_divisão_fractal)
        turtle.fd(-tamanho_fractal)

plotar_fractal(70, 7)
