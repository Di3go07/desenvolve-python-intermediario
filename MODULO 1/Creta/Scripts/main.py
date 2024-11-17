import labirinto
import player
import argparse

#JOGO
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