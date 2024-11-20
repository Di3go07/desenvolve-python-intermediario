from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
layout = Layout()
from rich.theme import Theme
custom_theme = Theme({
    'indice': 'bold #731F17',
    'opcao': '#F2B66D',
})
console = Console(theme=custom_theme)

#INICIO
def cabecalho():
    """
    cabecalho() cria o cabecalho do menu
    """
    console.print("—" * 42, style="#D98B48")
    console.print("CRETA".center(42), style="bold #D96F32")
    console.print("—" * 42, style="#D98B48")

def apresentacao(user):    
    """
    apresentacao() imprime uma mensagem de bem vindo com o nome do jogador
    """
    console.print(f"[opcao]Bem vindo, {user}[/opcao]")
    print()
    console.print(f"[opcao]Escolha uma das opções: [/opcao]",)
def opcoes():
    """
    opcoes() cria as opções de menu que o player pode escolher
    """
    console.print(" [indice] 1 [/indice]- [opcao]Jogar[/opcao]")
    console.print(" [indice] 2 [/indice]- [opcao]História[/opcao]")
    console.print(" [indice] 3 [/indice]- [opcao]Tutorial[/opcao]")
    console.print("—" * 42, style="#D98B48")

def escolha():
    """
    escolha() adiciona um valor input para o player registrar sua escolha
    """
    console.print("[indice]Opção:[/indice]", end=" ")
    escolha = int(input(''))
    return escolha

#HISTÓRIA
#texto
def historiaTexto(user):
    """
    historiaTexto() armazena o texto da página História e seu layout
    """
    historia_message = Table.grid(padding=1)
    historia_message.add_column(style='#F2B66D', justify="left")
    historia_message.add_column(no_wrap=True)
    historia_message.add_row(
        "   Na Grécia Antiga, uma construção imponente e grandiosa feita pelo brilhante arquiteto Dédalo se destaca na ilha de Creta: um labirinto que guarda um monstro terrível em seu interior. Metade homem e metade touro, o Minotauro foi aprisionado dentro desse labirinto a mando do Rei Minos para livrar seu reino desse mal que ele mesmo liberou, de forma que a criatura nunca consiga achar a saída. Porém, a força e a raiva dele são incontroláveis até mesmo para a arquitetura de Dédalo, então o Rei envia todo ano jovens para serem devorados e alimentar a fera."
    )
    historia_message.add_row(
        f"   A época de alimentar o Minotauro chegou e você foi o escolhido para ser enviado ao labrinto de Creta e fazer esse trabalho sujo. Agora, para sobreviver e não virar a comida do monstro, você precisa achar falhas na estrutura que consigam liberar a saída e, o mais importante, não se perder pelos corredores do labirinto. Boa sorte, {user}, em sua aventura para desvendar a arquitetura complexa de Dédalo e não ser capturado pelo Minotauro."
    )
    return historia_message
#painel
def historia(user):
    """
    historia() imprime a página História
    """
    console.print(Panel(historiaTexto(user), title='[indice]HISTÓRIA[/indice]', style="#D98B48"))

#TUTORIAL
#textos
def header():
    """
    header() cria o texto da header na página Tutorial e a customização dele
    """
    header = Table.grid(expand=True)
    header.add_column(style = "bold #D96F32", justify="center", ratio=1)
    header.add_row("TUTORIAL")
    return header

def comoJogar():
    """
    comoJogar() cria o texto de explicação do jogo na página Tutorial e a customização dele
    """
    comoJogar_message = Table.grid(padding=1)
    comoJogar_message.add_column(style='#F2B66D', justify="left")
    comoJogar_message.add_column(no_wrap=True)
    comoJogar_message.add_row(
        "Como jogar", style="#D96F32"
    )
    comoJogar_message.add_row(
        "O objetivo do jogo é fugir do labirinto sem que o minotauro [indice](V)[/indice] alcance o player [indice](@)[/indice]."
    )
    comoJogar_message.add_row(
        "Para fugir do labirinto, o player precisa obter quatro itens [indice](o)[/indice] espalhados pelo mapa e, assim, liberar o portão principal. Quando o jogo é iniciado, uma pequena cutscene da impressão do tabuleiro e de uma cena de perseguição acontece antes do player estar autorizado a jogar."
    )
    comoJogar_message.add_row(
        "[indice]Lembre-se: [/indice]cada passo seu também é um movimento feito pelo minotauro, então pense bem em como prosseguir pelo labirinto"
    )
    comoJogar_message.add_row(
        "Aproveite o jogo!"
    )
    return comoJogar_message

def controle():
    """
    controle() cria o texto com informações sobre os controles do jogo e a customização dele
    """
    controle_message = Table.grid(padding=1)
    controle_message.add_column(justify="left")
    controle_message.add_column(no_wrap=True)
    controle_message.add_row(
        "Controles", style="#D96F32"
    )
    controle_message.add_row(
        "[opcao]W[/opcao] - [indice]subir[/indice]"
    )    
    controle_message.add_row(
        "[opcao]S[/opcao] - [indice]descer[/indice]"
    )
    controle_message.add_row(
        "[opcao]A[/opcao] - [indice]esquerda[/indice]"
    )
    controle_message.add_row(
        "[opcao]D[/opcao] - [indice]direita[/indice]"
    )
    controle_message.add_row(
        "[opcao]Q[/opcao] - [indice]sair[/indice]"
    )
    return controle_message

#Layout
def tutorial():
    """
    tutorial() cria o layut da página Tutorial e imprime os textos
    """
    layout.split_column(
        Layout(name="header"),
        Layout(name="text")
    )
    layout["header"].size = 3
    layout["header"].update(Panel(header(), style="#D98B48"))
    layout["header"].minimum_size = 1
    layout["text"].size = 15
    layout["text"].split_row(
        Layout(name="sobre"),
        Layout(name="controles"),
    )
    layout["sobre"].update(Panel(comoJogar(), style="#D98B48"))
    layout["controles"].update(Panel(controle(), style="#D98B48"))

    console.print(layout)
