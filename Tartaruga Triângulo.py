import turtle

# Input do tipo de triângulo que o usuário deseja.
tipo_de_triangulo = str(input('''Que tipo de triângulo você deseja:\
Equilatero, isoceles ou retangulo?'''))
# Formatação da resposta do usuário.
tipo_de_triangulo = tipo_de_triangulo.lower()

# Criando uma tela de desenho
tela = turtle.Screen()

# Criando caneta para desenhar.
caneta = turtle.Turtle()


# Criando função para desenhar triângulos.
def triangulo(x, y):

    # Levanta a caneta do papel
    caneta.up()

    # Leva caneta ao ponto (x,y)
    caneta.goto(x, y)

    # Encosta caneta no "papel"
    caneta.down()
    # Condicional e loop para a opção "equilatero".
    if tipo_de_triangulo == "equilatero":
        for i in range(3):
            caneta.forward(100)
            caneta.lt(120)
            caneta.forward(100)
    # Condicional e diretrizes para a opção "isoceles".
    if tipo_de_triangulo == "isoceles":
        caneta.forward(75)
        caneta.lt(100)
        caneta.forward(400)
        caneta.rt(200)
        caneta.forward(400)
        caneta.lt(100)
        caneta.forward(75)
    # Condicional e diretrizes para a opção "retangulo".
    if tipo_de_triangulo == "retangulo":
        caneta.forward(100)
        caneta.lt(135)
        caneta.forward(200 * 1.414213562)
        caneta.lt(135)
        caneta.forward(200)
        caneta.lt(90)
        caneta.forward(100)


# Método que inicia o traçado no local
# onde o usuário clicar com o mouse.
turtle.onscreenclick(triangulo, 1)
# Receber inputs dos módulos do turtle.
turtle.listen()
# Método para manter a tela, como mainloop.
turtle.done()
