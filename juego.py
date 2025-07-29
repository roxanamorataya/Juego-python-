import os
import readchar 
from mapa import cargar_mapa
estado_juego =True
def game():
    #iniciar juego 
    tecla  = readchar.readchar()

    if tecla == "W":
        cargar_mapa(tecla)
    elif tecla == "S":
        cargar_mapa(tecla)
    elif tecla == "A":
        cargar_mapa(tecla)
    elif tecla == "D":
        cargar_mapa(tecla)
    elif tecla == "Q":
        estado_juego = False

game()

while estado_juego:
    game() 