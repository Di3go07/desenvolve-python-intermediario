import labirinto
import player
import menus
from rich.console import Console
console = Console()
import argparse

#MENU
def menu():
    """
    menu() cria o menu inicial e analise qual atitude tomar após a escolha do player
    """
    labirinto.limparTabuleiro()
    menus.cabecalho()
    menus.opcoes()
    escolha = menus.escolha()

    #JOGO
    if escolha == 1:
        player1 = player.Player()
        inimigo = player.Inimigo()
        inimigo.position()
        player1.position() 

        labirinto.criarBordas()

        while True:
            with player.keyboard.Listener(
                    on_press=player.on_press) as listener:
                listener.join()
            
            inimigo.moverInimigo()
        listener.start()

    #HISTORIA
    if escolha == 2:
        labirinto.limparTabuleiro()
        menus.historia()
        voltar = input("Voltar ao menu(Y/[n]): ")
        if voltar == "Y":
            menu()
        elif voltar == "[n]":
            quit()
        else:
            console.print("Opção invalida", style="red")

    #TUTORIAL
    if escolha == 3:
        labirinto.limparTabuleiro()
        menus.tutorial()
        voltar = input("Voltar ao menu(Y/[n]): ")
        if voltar == "Y":
            menu()
        elif voltar == "[n]":
            quit()
        else:
            console.print("Opção invalida", style="red")

menu()