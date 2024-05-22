def Forca(Tentativa):
    f1 = "  +------------+ "
    f2 = "  |            | "
    f3 = "  |            O "
    f4 = "  |           /|\ "
    f5 = "  |            |  "
    f6 = "  |           / \ "
    f7 = "__|_______              "


def Continua():
    while True:
        print("-" * 20)
        novamente = input("Quer Jogar de S/N:").upper()
        if novamente == "S":
            Acabou = True
            break
        elif novamente == "N":
            Acabou = False
            break
        else:
            print("Digite S ou N: ")
    return Acabou
Jogar = True
while Jogar:
    Jogar = Continua()
