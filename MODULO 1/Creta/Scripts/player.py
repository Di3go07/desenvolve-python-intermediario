import os
import rich
from rich.console import Console
from rich.theme import Theme
from rich.style import Style
console = Console()
import time
from time import sleep
from pynput import keyboard
import pandas as pd
import random
import threading
import labirinto
import itens

#criando o personagem
class Player:
    char = "@"
    xPos = 16
    yPos = 21 
    itens = 3
    dead = False
    #status do personagem
    def position(self):
        labirinto.board[self.yPos][self.xPos] = self.char
    def pegouItens(self):
        self.itens += 1
        if self.itens == 4:
            labirinto.board[32][14] = " "
            labirinto.limparTabuleiro()
            labirinto.imprimirTabuleiro()
            console.print('Saída liberada!')
            sleep(1)
    def vitoria(self):
        labirinto.board[32][14] = " "
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
        console.print("ESCAPED!!!", style='bold green')
        sleep(1)
        quit()

    def isDead(self):
            labirinto.board[self.xPos][self.yPos] = " "
            labirinto.limparTabuleiro()
            labirinto.imprimirTabuleiro()
            self.dead = True
            console.print("YOU DIED!!!", style='bold red')
            sleep(2)
            quit()

#movimentos do personagem
def moverCima():
    if labirinto.board[Player.yPos - 1][Player.xPos] == "o":
        Player.pegouItens(Player)
        labirinto.board[Player.yPos - 1][Player.xPos] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.yPos = Player.yPos - 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
    elif labirinto.board[Player.yPos - 1][Player.xPos] != " ":
        print('Bateu!')
    else:
        labirinto.board[Player.yPos - 1][Player.xPos] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.yPos = Player.yPos - 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()


def moverBaixo():
    if Player.xPos == 14 and Player.yPos + 1 == 32: #verifica se o player está no final
        labirinto.board[Player.yPos + 1][Player.xPos] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
        Player.vitoria(Player)
    if labirinto.board[Player.yPos + 1][Player.xPos] == "o": 
        Player.pegouItens(Player)
        labirinto.board[Player.yPos + 1][Player.xPos] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.yPos = Player.yPos + 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
    elif labirinto.board[Player.yPos + 1][Player.xPos] != " ":
        print('Bateu!')
    else:
        labirinto.board[Player.yPos + 1][Player.xPos] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.yPos = Player.yPos + 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()


def moverEsquerda():
    if labirinto.board[Player.yPos][Player.xPos - 1] == "o":
        Player.pegouItens(Player)
        labirinto.board[Player.yPos][Player.xPos - 1] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.xPos = Player.xPos - 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
    elif labirinto.board[Player.yPos][Player.xPos - 1] != " ":
        print('Bateu!')
    else:
        labirinto.board[Player.yPos][Player.xPos - 1] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.xPos = Player.xPos - 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()

def moverDireita():
    if labirinto.board[Player.yPos][Player.xPos + 1] == "o":
        Player.pegouItens(Player)
        labirinto.board[Player.yPos][Player.xPos + 1] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.xPos = Player.xPos + 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
    elif labirinto.board[Player.yPos][Player.xPos + 1] != " ":
        print('Bateu!')
    else:
        labirinto.board[Player.yPos][Player.xPos + 1] = Player.char
        labirinto.board[Player.yPos][Player.xPos] = " "
        Player.xPos = Player.xPos + 1
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()

#respondendo o teclado
def on_press(key):
    """
    on_press() le a tecla pressionada no teclado

    A função utiliza a biblioteca keyboard para ler qual tecla o usuário apertou no teclado e tomar decisões a partir disso
    """
    try:
            if key.char=='w':
                moverCima()
            if key.char=='s':
                moverBaixo()
            if key.char=='a':
                moverEsquerda()
            if key.char=='d':
                moverDireita()
            if key.char=='q':
               exit()

    except AttributeError:
            print('special key {0} pressed'.format(key))
    return False


#criando o inimigo
class Inimigo:
    char = "V"
    xPos = 16
    yPos = 16
    last_position = (yPos,xPos)
    #status do inimigo
    def position(self):
        labirinto.board[16][16] = self.char
    #movimento do inimigo
    def moverInimigo(self):
        decisao = random.randrange(1, 5)
        print(decisao)
        match decisao:
            case 1:
                if labirinto.board[Inimigo.yPos - 1][Inimigo.xPos] ==  "@":
                    labirinto.board[Inimigo.yPos - 1][Inimigo.xPos] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    Player.isDead(Player)
                elif labirinto.board[Inimigo.yPos - 1][Inimigo.xPos] == " ":
                    labirinto.board[Inimigo.yPos - 1][Inimigo.xPos] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    self.last_position = (Inimigo.yPos, Inimigo.xPos)
                    Inimigo.yPos = Inimigo.yPos - 1
                    labirinto.limparTabuleiro()
                    labirinto.imprimirTabuleiro()  
                else:
                    self.moverInimigo()
            case 2:
                if labirinto.board[Inimigo.yPos + 1][Inimigo.xPos] ==  "@":
                    labirinto.board[Inimigo.yPos + 1][Inimigo.xPos] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    Player.isDead(Player)
                elif labirinto.board[Inimigo.yPos + 1][Inimigo.xPos] == " ":
                    labirinto.board[Inimigo.yPos + 1][Inimigo.xPos] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    self.last_position = (Inimigo.yPos, Inimigo.xPos)
                    Inimigo.yPos = Inimigo.yPos + 1
                    labirinto.limparTabuleiro()
                    labirinto.imprimirTabuleiro()  
                else:
                    self.moverInimigo()
            case 3:
                if labirinto.board[Inimigo.yPos][Inimigo.xPos - 1] ==  "@":
                    labirinto.board[Inimigo.yPos][Inimigo.xPos - 1] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    Player.isDead(Player)
                elif labirinto.board[Inimigo.yPos][Inimigo.xPos - 1] == " ":
                    labirinto.board[Inimigo.yPos][Inimigo.xPos - 1] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    self.last_position = (Inimigo.yPos, Inimigo.xPos)
                    Inimigo.xPos = Inimigo.xPos - 1
                    labirinto.limparTabuleiro()
                    labirinto.imprimirTabuleiro() 
                else:
                    self.moverInimigo()
            case 4:
                if labirinto.board[Inimigo.yPos][Inimigo.xPos + 1] ==  "@":
                    labirinto.board[Inimigo.yPos][Inimigo.xPos + 1] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    Player.isDead(Player)
                elif labirinto.board[Inimigo.yPos][Inimigo.xPos + 1] == " ":
                    labirinto.board[Inimigo.yPos][Inimigo.xPos + 1] = Inimigo.char
                    labirinto.board[Inimigo.yPos][Inimigo.xPos] = " "
                    self.last_position = (Inimigo.yPos, Inimigo.xPos)
                    Inimigo.xPos = Inimigo.xPos + 1
                    labirinto.limparTabuleiro()
                    labirinto.imprimirTabuleiro()   
                else:
                    self.moverInimigo()
