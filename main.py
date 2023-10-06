from Figura import QuadradoRetangulo, Triangulo, Circulo, Semicirculo, obter_coordenadas, animacao,um_quarto_circulo

apresentacao = (
    "Bem-vindo à Calculadora de Engenharia Estrutural!\n"
    "Essa calculadora determinará a área, o momento estático, o centro de gravidade e o momento de inércia de várias figuras!\n"
)

animacao(apresentacao)
print(
    "\nDessa forma, vamos calcular a área, o momento estático, o centro de gravidade e o momento de inércia de várias figuras!")

figuras = []


while True:
    area_total = 0
    momento_estatico_total_x = 0
    momento_estatico_total_y = 0
    momento_inercia_x = 0
    momento_inercia_y = 0

    figuras.clear()  # Limpa a lista de figuras para começar de novo.

    figuras_count = int(input("Quantas figuras você deseja calcular?\n"))

    for i in range(figuras_count):
        tipo_figura = int(input(f"Qual o tipo de figura está sendo adicionada? (Figura {i + 1})\n"
                                "1- quadrado ou retângulo\n"
                                "2- triângulo\n"
                                "3- círculo\n"
                                "4- semicírculo\n"
                                "5- 1/4 de círculo\n"))
        if tipo_figura == 1:
            base = obter_coordenadas("Quais as coordenadas em X da base? (separar por vírgula)\n")
            altura = obter_coordenadas("Quais as coordenadas em Y da altura? (separar por vírgula)\n")
            figura = QuadradoRetangulo(base[1] - base[0], altura[1] - altura[0])
        elif tipo_figura == 2:
            base = obter_coordenadas("Quais as coordenadas em X da base? (separar por vírgula)\n")
            altura = obter_coordenadas("Quais as coordenadas em Y da altura? (separar por vírgula)\n")
            figura = Triangulo(base[1] - base[0], altura[1] - altura[0])
        elif tipo_figura == 3:
            raio = float(input("Qual o raio do círculo?\n"))
            figura = Circulo(raio)
        elif tipo_figura == 4:
            raio = float(input("Qual o raio do semicírculo?\n"))
            direcao = int(input("Para qual direção está o semicírculo?\n"
                                "1 - esquerda\n"
                                "2 - baixo\n"
                                "3 - direita\n"
                                "4 - cima\n"))
            figura = Semicirculo(raio, direcao)
        elif tipo_figura == 5:
            raio = float(input("Qual o raio do 1/4 de círculo?\n"))
            direcao = int(input("Para qual direção está o 1/4 de círculo?\n"
                                "1 - superior esquerdo\n"
                                "2 - inferior esquerdo\n"
                                "3 - superior direito\n"
                                "4 - inferior direito\n"))
            figura = um_quarto_circulo(raio, direcao)

        figura.calcular_area()
        figura.calcular_centro_gravidade()
        figura.calcular_momento_inercia()

        figuras.append(figura)

        area_total += figura.area
        momento_estatico_total_x += figura.centro_gx * figura.area
        momento_estatico_total_y += figura.centro_gy * figura.area
        momento_inercia_x += figura.momento_inercia_x
        momento_inercia_y += figura.momento_inercia_y

    print(f"Área Total: {area_total}")
    print(f"Centro de Gravidade (Eixo X): {momento_estatico_total_x / area_total}")
    print(f"Centro de Gravidade (Eixo Y): {momento_estatico_total_y / area_total}")
    print(f"Momento de Inércia (Eixo X): {momento_inercia_x}")
    print(f"Momento de Inércia (Eixo Y): {momento_inercia_y}")

    sair = input("Digite 'SAIR' para parar ou pressione ENTER↵ para continuar: ")

    if sair == 'SAIR':
        break
