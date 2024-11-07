"""Progresso é um módulo baseado na biblioteca rich com objetivo de imprimir o progresso do computar na leitura de textos"""
from time import sleep
from rich.console import Console
console = Console()
from rich.progress import track
from rich.progress import Progress  
import os


texto = "/home/PDITA274/Documentos/teste.txt"

def lerTexto(texto, isArquivo):
    """
    lerTexto() imprime cada paragrafo de um texto no console

    A função recebe dois argumentos obrigatórios, sendo eles o texto, que pode ser tanto uma string quanto o caminho para um arquivo,    e um valor booleano que diz ao programa se a entrada texto é o caminho para um arquivo ou não. A impressão do texto conta com uma barra de progresso que mostra ao usuário o avanço da leitura de cada paragrafo do texto no arquivo pelo computador até sua impressão.
    """
    
    i = 1
    if isArquivo == True:
        with open(texto, 'r' ) as arq:
                for paragrafo in arq:
                    for line in track(paragrafo.split("."), description=f"Lendo {i}° paragráfo..."):
                        if (line != "\n"):
                            print(line, end=".")
                            sleep(1)
                        else:
                            print(line)
                            sleep(1)
                    i += 1

    elif isArquivo == False:
        for palavra in track(texto.split(" "), description="Lendo string..."):
                print(palavra, end=" ")
                sleep(1)
                

def imprimirTexto(texto, isArquivo):
        """
        imprimirTexto() imprime o texto após ler o tamanho de seu arquivo ou número de caracteres

        A função recebe dois argumentos obrigatórios, sendo eles o texto, que pode ser tanto uma string quanto o caminho para um arquivo, e um valor booleano que diz ao programa se a entrada texto é o caminho para um arquivo ou não. A impressão do texto ocorre após o programa completar o progresso da barra de leitura do arquivo ou string, sendo que a primeira leva como base o tamanho em bytes e a segunda o tamanho da string.
        """  

        if isArquivo == True:
            with Progress() as progress:
                size_bytes = os.path.getsize(texto)
                task = progress.add_task("[green]Lendo...", total=size_bytes)

                while not progress.finished:
                    progress.update(task, advance=0.5)
                    sleep(0.02)

            print(f'Leitura do arquivo de {size_bytes} bytes: ')
            arquivo = open(texto, 'r')
            print(arquivo.read())

        elif isArquivo == False:
            with Progress() as progress:
                size = len(texto)
                task = progress.add_task("[green]Lendo...", total= size)

                while not progress.finished:
                    progress.update(task, advance=0.5)
                    sleep(0.02)

            print(f'Leitura de string com {size} caracteres: ')
            print(texto)


#lerTexto(texto, True)
