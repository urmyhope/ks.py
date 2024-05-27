def Forca(tentativa):
    f1 = "  +------------+ "
    f2 = "  |              "
    f3 = "  |              "
    f4 = "  |              "
    f5 = "  |              "
    f6 = "  |              "
    f7 = "__|_______              "

    if tentativa >= 1:
        f2= "  |            | "

    if tentativa >= 2:
        f3 = "  |            O " 

    if tentativa >= 3:  
        f4 = "  |            | "

    if tentativa >= 4: 
        f4 = "  |           /| "

    if tentativa >= 5: 
        f4 = "  |           /|\ "

    if tentativa >= 6: 
        f5 = "  |            |  "

    if tentativa >= 7:
        f6 = "  |           /  "

    if tentativa >= 8:
        f6 = "  |           / \ "  

    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)


Forca(0)


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
x=0

while Jogar:
    print(x)
    Forca(x)
    Jogar = Continua()
    x = x + 1
