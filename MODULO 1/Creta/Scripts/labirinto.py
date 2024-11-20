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
import playsound
import random
import threading

import player

#Tabuleiro
board = [[" " for l in range(33)] for c in range(33)]

#Funções

def criarBordas():
    """
    criarBordas() cria as bordas do labirinto

    A função adiciona "-" no topo e na base do tabuleiro e "|" nas laterais para representar as bordas dele
    """
     
    #bordas superiores
    for column in range(33):
        board[0][column] = "-"
        board[32][column] = "¯"
    board[32][14] = "X"

    #bordas laterais
    linha = 1
    while linha < 32:
        board[linha][0] = "|"
        board[linha][32] = "|"
        linha += 1
    spawner()


def spawner():
    """
    spawner() imprime no terminal o spawner

    A função adiciona ao labirinto uma área central onde se enconntra o inimigo do player
    """
    for column in range(14, 19):
        board[14][column] = "-"
        board[18][column] = "¯" 
        board[18][16] = "=" 
    linha = 15
    while linha < 18:
        board[linha][14] = "|"
        board[linha][18] = "|"
        linha += 1
    preencherTabuleiro()


def preencherTabuleiro():
    """
    preencherTabuleiro() adiciona na matriz os obstáculos do labirinto

    A função le um arquivo externo com as informações de posição do caracter a ser adicionado na matriz do labirinto 
    """
    df = pd.read_csv('/home/PDITA274/Documentos/PYTHON/MODULO_1/jogo_labirinto/labirintoInfos.csv')
    for index, row in df.iterrows():
        board[row['eixoY']][row['eixoX']] = row['char'] #le as informações de cada tabela do arquivo para adicionar os elementos na matriz
    board[29][18] = 'o'
    board[13][23] = 'o'
    board[11][5] = 'o'
    board[21][3] = 'o'

    start()


def start():
    """
    start() primeira impressão do labirinto no terminal

    A função tem a mesma proposta da função imprimirTabuleiro(), porém tem elementos diferentes por se tratar da primeira impressão dele
    """
    limparTabuleiro()
    for count in board:
        console.print(" ".join(count), style="#F2B66D")
        sleep(0.5)
    sleep(1)
    board[18][16] = " " 
    limparTabuleiro()
    imprimirTabuleiro()
    console.print('Fera liberada!', style='bold white')


def cutscene():
    """
    cutsecen() adiciona uma cutscene ao jogo

    A função muda os caracteres em diferentes índices da matriz labirinto para criar uma sensação de movimento na tela e produzir uma cena inicial ao jogo
    """
    #movimentos
    for i in range(6):
        #movimento player
        board[player.Player.yPos][player.Player.xPos] = " "
        player.Player.yPos += 1
        board[player.Player.yPos][player.Player.xPos] = "@"
        #movimento inimigo
        board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
        player.Inimigo.yPos += 1
        board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
        #salvar alterações
        limparTabuleiro()
        imprimirTabuleiro()
        sleep(0.5)
    for i in range(5):
        #movimento player
        board[player.Player.yPos][player.Player.xPos] = " "
        player.Player.xPos += 1
        board[player.Player.yPos][player.Player.xPos] = "@"
        #movimento inimigo
        board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
        player.Inimigo.yPos += 1
        board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
        #salvar alterações
        limparTabuleiro()
        imprimirTabuleiro()
        sleep(0.5)
    #movimento player
    board[player.Player.yPos][player.Player.xPos] = " "
    player.Player.xPos += 1
    board[player.Player.yPos][player.Player.xPos] = "@"
    #movimento inimigo
    board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
    player.Inimigo.xPos += 1
    board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
    #salvar alterações
    limparTabuleiro()
    imprimirTabuleiro()
    sleep(0.5)
    for i in range(2):
        #movimento player
        board[player.Player.yPos][player.Player.xPos] = " "
        player.Player.xPos += 1
        board[player.Player.yPos][player.Player.xPos] = "@"
        #movimento inimigo
        board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
        player.Inimigo.xPos += 1
        board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
        #salvar alterações
        limparTabuleiro()
        imprimirTabuleiro()
        sleep(0.5)
    for i in range(4):
        #movimento player
        board[player.Player.yPos][player.Player.xPos] = " "
        player.Player.yPos += 1
        board[player.Player.yPos][player.Player.xPos] = "@"
        #movimento inimigo
        board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
        player.Inimigo.xPos += 1
        board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
        #salvar alterações
        limparTabuleiro()
        imprimirTabuleiro()
        sleep(0.5)
    #movimento player
    board[player.Player.yPos][player.Player.xPos] = " "
    player.Player.xPos += 1
    board[player.Player.yPos][player.Player.xPos] = "@"
    #movimento inimigo
    board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
    player.Inimigo.xPos += 1
    board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
    #salvar alterações
    limparTabuleiro()
    imprimirTabuleiro()
    sleep(0.5)
    #movimento player
    board[player.Player.yPos][player.Player.xPos] = " "
    player.Player.xPos += 1
    board[player.Player.yPos][player.Player.xPos] = "@"
    #movimento inimigo
    board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
    player.Inimigo.yPos += 1
    board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
    #salvar alterações
    limparTabuleiro()
    imprimirTabuleiro()
    sleep(0.5)
    #movimento player
    board[player.Player.yPos][player.Player.xPos] = " "
    player.Player.yPos -= 1
    board[player.Player.yPos][player.Player.xPos] = "@"
    #movimento inimigo
    board[player.Inimigo.yPos][player.Inimigo.xPos] = " "
    player.Inimigo.yPos += 1
    board[player.Inimigo.yPos][player.Inimigo.xPos] = "V"
    board[18][16] = "=" 
    #salvar alterações
    limparTabuleiro()
    imprimirTabuleiro()
    print('colete os itens para liberar a saída e corra do minotauro')
    sleep(0.5)
    print('mova-se com w,a,s,d')
    sleep(1)
    console.print('FUJA DO LABIRINTO!', style='bold red')


def imprimirTabuleiro():
    """
    imprimirTabuleiro() imprime no terminal o labirinto

    A função junta todos os elementos de cada linha da matriz de "board" para formar o visual do labirinto no terminal
    """
    for count in board:
        console.print(" ".join(count), style="#F2B66D")
    


def limparTabuleiro():
    """
    limparTabuleiro() limpa o terminal

    A função fornece ao sistema o comando "clear" e limpa o terminal
    """
    os.system('clear')