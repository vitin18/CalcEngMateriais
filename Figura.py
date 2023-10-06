import math
import time


def animacao(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()


class Figura:
    def __init__(self, tipo):
        self.tipo = tipo
        self.area = 0
        self.centro_gx = 0
        self.centro_gy = 0
        self.momento_inercia_x = 0
        self.momento_inercia_y = 0

    def calcular_area(self):
        pass

    def calcular_centro_gravidade(self):
        pass

    def calcular_momento_inercia(self):
        pass


class QuadradoRetangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Quadrado/Retângulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = self.base * self.altura

    def calcular_centro_gravidade(self):
        self.centro_gx = (self.base / 2) * self.area
        self.centro_gy = (self.altura / 2) * self.area

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (self.altura ** 3) * self.base / 12
        self.momento_inercia_y = (self.base ** 3) * self.altura / 12


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triângulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def calcular_centro_gravidade(self):
        self.centro_gx = (self.base / 3) * self.area
        self.centro_gy = (self.altura / 3) * self.area

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (self.altura ** 3) * self.base / 36
        self.momento_inercia_y = (self.base ** 3) * self.altura / 36


class Circulo(Figura):
    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def calcular_area(self):
        self.area = math.pi * (self.raio ** 2)

    def calcular_centro_gravidade(self):
        self.centro_gx = self.raio / 2
        self.centro_gy = self.raio / 2

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (math.pi * self.raio ** 4) / 4
        self.momento_inercia_y = (math.pi * self.raio ** 4) / 4


class um_quarto_circulo(Figura):
    def __init__(self, raio, direcao):
        super().__init__("Um quarto de Círculo")
        self.raio = raio
        self.direcao = direcao

    def calcular_area(self):
        self.area = (math.pi * (self.raio ** 2)) / 4

    def calcular_centro_gravidade(self):
        if self.direcao in [1, 3]:
            self.centro_gx = self.raio / 8
            self.centro_gy = self.raio / 8
        else:
            self.centro_gx = self.raio / 2
            self.centro_gy = self.raio / 2

    def calcular_momento_inercia(self):
        if self.direcao in [1, 3]:
            self.momento_inercia_x = (math.pi * self.raio ** 4) / 32
            self.momento_inercia_y = (math.pi * self.raio ** 4) / 32
        else:
            self.momento_inercia_x = (math.pi * self.raio ** 4) / 8
            self.momento_inercia_y = (math.pi * self.raio ** 4) / 8


def obter_coordenadas(mensagem):
    while True:
        coordenadas = input(mensagem)
        if "," in coordenadas:
            try:
                coordenadas = [float(x) for x in coordenadas.split(",")]
                if len(coordenadas) == 2:
                    return coordenadas
            except ValueError:
                pass
        print("Por favor, digite as coordenadas corretamente (formato: x,y).")


class Semicirculo(Figura):
    def __init__(self, raio, direcao):
        super().__init__("Semicírculo")
        self.raio = raio
        self.direcao = direcao

    def calcular_area(self):
        self.area = (math.pi * (self.raio ** 2)) / 2

    def calcular_centro_gravidade(self):
        if self.direcao in [1, 3]:
            self.centro_gx = self.raio / 4
            self.centro_gy = self.raio / 4
        else:
            self.centro_gx = 0
            self.centro_gy = (4 * self.raio / (3 * math.pi))

    def calcular_momento_inercia(self):
        self.momento_inercia_x = (math.pi * self.raio ** 4) / 8
        self.momento_inercia_y = (math.pi * self.raio ** 4) / 8
