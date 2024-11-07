"""Painel é um módulo baseado na biblioteca rich com objetivo de criar um título de destaque à impressão no console"""
from rich import print
import rich
from rich.panel import Panel
from rich.console import Console
console = Console()

def definirTitulo (texto, titulo, isArquivo):
    """
    definirTitulo() imprime o texto como um painel com um título

    A função recebe três argumentos obrigatórios, sendo eles o texto, que pode ser tanto uma string quanto o caminho para um arquivo, o texto que o usuário deseja que seja o título e um valor booleano que diz ao programa se a entrada texto é o caminho para um arquivo ou não.
    """
    if isArquivo == False:
            print(Panel(texto, title=titulo))
    if isArquivo == True:
            arquivo = open(texto, 'r')
            print(Panel(arquivo.read(), title= titulo))

#definirTitulo("/home/PDITA274/Documentos/teste.txt", "Dom Casmurro", True)

def comSubtitulo(texto, titulo, subtitulo, isArquivo):
    """
    comSubtitulo() imprime o texto como um painel com um título

    A função recebe quatro argumentos obrigatórios, sendo eles o texto, que pode ser tanto uma string quanto o caminho para um arquivo, o texto que o usuário deseja que seja o título, outro que será o subtitulo e um valor booleano que diz ao programa se a entrada texto é o caminho para um arquivo ou não.
    """
    if isArquivo == False:
            print(Panel(texto, title=titulo, subtitle= subtitulo))
    if isArquivo == True:
            arquivo = open(texto, 'r')
            print(Panel(arquivo.read(), title= titulo, subtitle=subtitulo))

#comSubtitulo("/home/PDITA274/Documentos/teste.txt", "Dom Casmurro", "Fim", True)