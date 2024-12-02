from PySide6.QtWidgets import QApplication, QPushButton
import pygame
from pygame.locals import *
from random import randint
pygame.init()

#Definir classes 
class objeto:
    def __init__(self,posicao_x,posicao_y,cor_obj,largura_obj,altura_obj):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.cor_obj = cor_obj
        self.largura_obj = largura_obj
        self.altura_obj = altura_obj
        

#Definir jogador e a frutinha
Jogador = objeto(0,0,(255,0,0),20,20)
Frutinha = objeto(l)


#Define os locais que estao os sons
Local_musica = "Python projects//jogo_da_cobrinha/virtual//sons//doom.mp3"
Local_son_pegou_frutinha = "Python projects//jogo_da_cobrinha/virtual//sons//pegou.mp3"
pygame.mixer.music.play(-1)

