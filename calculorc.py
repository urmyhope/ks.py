def retangulo(tipoR, largura, altura):
    r =0
    if tipoR == "area":
        r = largura * altura
    elif tipoR == "perimetro":
        r=2*(largura + altura)
    return r


def circulo(tipoC,raio):
    c = 0
    if tipoC == "area":
        c = 3.14 + (raio ** 2)
    elif tipoC == "perimero":
        c = 2 * 3.14 * (raio)
    return c

ra = retangulo("area", 15, 4.5)
print(f'area:{ra}')

ca = circulo("area", 5)
print(f'area: {ca}')
