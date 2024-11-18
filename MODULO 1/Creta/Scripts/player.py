import os
import rich
from rich.console import Console
console = Console()
from rich.theme import Theme
from rich.style import Style
import time
from time import sleep
from pynput import keyboard
import pandas as pd
import random
import threading
import labirinto

#criando o personagem
class Player:
    char = "@"
    xPos = 16
    yPos = 21 
    itens = 0
    dead = False
    #status do personagem
    def position(self):
        labirinto.board[self.yPos][self.xPos] = self.char
    def pegouItens(self):
        """
        pegouItens() função da classe acionada quando o player pega um item

        Quando o player está na mesma posição que um item, a função pegouItens() é chamada e adiciona 1 ao valor de itens resgatados pelo player. Além disso, verifica se a quantidade dos itens é igual a 4, caso sejam iguais, a saída é liberada
        """
        self.itens += 1
        if self.itens == 4:
            labirinto.board[32][14] = " "
            labirinto.limparTabuleiro()
            labirinto.imprimirTabuleiro()
            console.print('Saída liberada!')
            sleep(1)
    def vitoria(self):
        """
        vitoria() função da classe acionada quando o player chega ao final

        Quando o player se encontra na posição do final, a função vitoria() é ativada e encerra o jogo com uma mensagem de vitória
        """
        labirinto.board[32][14] = " "
        labirinto.limparTabuleiro()
        labirinto.imprimirTabuleiro()
        console.print("ESCAPED!!!", style='bold green')
        sleep(1)
        quit()

    def isDead(self):
            """
            isDead() função da classe acionada quando o player morre

            Quando o inimigo está na mesma posição do labirinto que o player, a função isDead() é ativada e encerra o jogo com uma mensagem final de morte
            """
            labirinto.board[self.xPos][self.yPos] = " "
            labirinto.limparTabuleiro()
            labirinto.imprimirTabuleiro()
            self.dead = True
            console.print("YOU DIED!!!", style='bold red')
            sleep(2)
            quit()

#movimentos do personagem
"""
funções de movimento

As funções de movimento do player foram dividas para cada movimento que ele possa tomar, sendo eles: para cima(w), para baixo(s), para esquerda(a) e para direita(d). Além disso, elas também possuem o papel de verificar se o caminho está liberado ou se o item pode ser resgatado pelo player
"""
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
        """
        moverInimigo() função responsável por movimentar o inimigo

        A função pretende criar uma pequena Inteligência Artificial no inimigo do jogo. Para isso, o inimigo consegue tomar decisões do caminho que ele deseja tomar ao escolher de forma aleatória um número de 1 a 4. Caso não tenha barreiras no caminho, o inimgo prossegue para a direção que ele escolheu, mas se apresentar barreiras ele toma outra decisão. Lembre-se: o inimigo se movimento na mesma medida que o player
        """
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
