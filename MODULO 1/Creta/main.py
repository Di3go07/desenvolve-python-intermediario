from creta_pkg import labirinto
from creta_pkg  import player
from creta_pkg  import menus
from rich.console import Console
console = Console()
import threading
from time import sleep
import playsound
from playsound import playsound
import argparse

#ARGUMNETOS
parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store_true', help='acionado caso deseja tirar a musica')
parser.add_argument('user', type=str, help='Digite um nome de usuário')

args = parser.parse_args() #interpreta o comando
#MUSICA
if not args.s:
    def loopSound():
        while True:
            playsound('./docs/musica.mp3', block=True)

    loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
    loopThread.daemon = True #desativa a música apenas após sua execução finalizar
    loopThread.start()

#MENU
def menu():
    """
    menu() cria o menu inicial e analise qual atitude tomar após a escolha do player
    """
    labirinto.limparTabuleiro()
    menus.cabecalho()
    menus.apresentacao(args.user)
    menus.opcoes()
    escolha = menus.escolha()

    #JOGO
    match escolha:
        case 1:
            player1 = player.Player()
            inimigo = player.Inimigo()
            inimigo.position()
            player1.position() 

            labirinto.criarBordas()
            sleep(1)
            labirinto.cutscene()

            while True:
                #verifca sempre se o player está morto
                if player1.dead == True:
                    if not args.s:
                        playsound('./docs/death.mp3', block=False)
                    player1.isDead(args.user)
                    sleep(2)
                    quit()
                with player.keyboard.Listener(
                        on_press=player.on_press) as listener:
                    listener.join()
                
                inimigo.moverInimigo()
            listener.start()

        #HISTORIA
        case 2:
            labirinto.limparTabuleiro()
            menus.historia(args.user)
            voltar = input("Voltar ao menu(Y/[n]): ")
            if voltar == "Y":
                menu()
            elif voltar == "[n]":
                quit()
            else:
                console.print("Opção invalida", style="red")

        #TUTORIAL
        case 3:
            labirinto.limparTabuleiro()
            menus.tutorial()
            voltar = input("Voltar ao menu(Y/[n]): ")
            if voltar == "Y":
                menu()
            elif voltar == "[n]":
                quit()

menu()