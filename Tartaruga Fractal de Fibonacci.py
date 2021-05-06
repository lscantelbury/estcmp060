import turtle

turtle.speed("fastest")

# Rodando a tartaruga para cima.
turtle.rt(-90)

# Ângulo do "Y" do fractal.
angulo_de_divisão_fractal = 30

# Função para plotar o fractal.
def plotar_fractal(tamanho_fractal, niveis_fractal):

    if niveis_fractal > 0:
        # Definindo esquema de cores para r,g,b.
        turtle.colormode(255)
        # Definindo cor da caneta conforme o nível
        # a ser desenhado no fractal.
        turtle.pencolor(0, 255//niveis_fractal, 0)
        # Desenhando reta inicial e rotacionando 30° 
        # para a direita.
        turtle.fd(tamanho_fractal)
        turtle.rt(angulo_de_divisão_fractal)
        # Plotando outro ramo do braço,
        # mas em menor proporção.
        plotar_fractal(0.8 * tamanho_fractal,
             niveis_fractal-1)
        # Mantendo esquema de cor por níveis e 
        # rotacionando a tartaruga para a esquerda.
        turtle.pencolor(0, 255//niveis_fractal, 0)
        turtle.lt(2 * angulo_de_divisão_fractal)
        # Plotando ramo esquerdo do braço.
        plotar_fractal(0.8 * tamanho_fractal,
             niveis_fractal - 1)
        
        turtle.pencolor(0, 255//niveis_fractal, 0)

        turtle.rt(angulo_de_divisão_fractal)
        turtle.fd(-tamanho_fractal)
        turtle.done()

plotar_fractal(80, 7)