import os
WIDHT_MAPA = 50
HEIGHT_MAPA = 20
espacio_invisible = "   "
espacio_visible = "[ ]"
coordenada_personaje = [10,25]
personaje = "➤"
coordenada_personaje = [10,25]
personaje = "➤"

def cargar_mapa(Movimiento_personaje):
    

    os.system("cls")
    if Movimiento_personaje == "W":
        coordenada_personaje[0] -= 1
        personaje = "🡱"
    elif Movimiento_personaje == "S":
        coordenada_personaje[0] += 1
        personaje = "🡳"
    elif Movimiento_personaje == "A":
        coordenada_personaje[1] -= 1
        personaje = "🡰"
    elif Movimiento_personaje == "D":
        coordenada_personaje[1] += 1
        personaje = "🡲"

    print("+","-"* 149 + "+")
    for cada_fila in range(HEIGHT_MAPA):
        print("|",end="")
        for cada_item in range(WIDHT_MAPA):
            
            if(coordenada_personaje[0]==cada_fila and coordenada_personaje[1]== cada_item):
                print(f" {personaje} ", end="")
            else:
                print(espacio_invisible, end="")

        print("|")
    print("+","-"* 149 + "+")