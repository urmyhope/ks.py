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
    elif tipoC == "perimetro":
        c = 2 * 3.14 * (raio)
    return c

def verifica_resultado(altura, largura, raio):
    print(f'retangulo area:{retangulo("area", largura, altura)}')
    print(f'retangulo perimetro: {retangulo("perimetro", largura, altura)}')
    print(f'circulo perimetro:{circulo("perimetro", raio )}')



ra = retangulo("area", 8, 12)
print(f'area:{ra}')

ca = circulo("area", 5)
print(f'area: {ca}')

verifica_resultado(8,12,5)

