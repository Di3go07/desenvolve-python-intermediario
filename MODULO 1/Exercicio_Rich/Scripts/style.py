"""Style é um módulo baseado na biblioteca rich com objetivo de alterar atributos na impressão de um texto"""
import rich
from rich.console import Console
from rich.style import Style
console = Console()


def changeColor (texto, cor, isArquivo):
    """
    changeColor() altera a cor do texto proveniente de uma string ou de um arquvio

    A função recebe três argumentos obrigatŕoios para sua execução, sendo eles o texto, que pode ser tanto uma string quanto o caminho para um arquivo, a cor 
    que deseja aplicar e um valor booleano que diz ao programa se a entrada texto é o caminho para um arquivo ou não.
    Ao passar o argumento da cor lembre-se que ela aceita o formato das 256 Standard Colors - como "blue", "yellow" "violet" -, o CSS-like syntax que especifica 
    a cor com "#" e a forma RGB, por exemplo, "rgb(175,0,255)".
     """
    if isArquivo == False:
        console.print(texto, style=cor)
    if isArquivo == True:
        arquivo = open(texto, 'r')
        console.print(arquivo.read(), style=cor)


def highlightWord (texto, chave, isArquivo):
    """
    highlightWord() coloca negrito para destacar a palavra que o usário deseja buscar

    A função recebe três argumentos obrigatórios, sendo eles o texto, que pode ser tanto uma string quanto o caminho para um arquivo,  uma palavra que
    o usuário deseja encontrar e um valor booleano que diz ao programa se a entrada texto é o caminho para um arquivo ou não.
    Alguns detalhes são importantes de serem reforçados: a grafia errada da palavra pode causar respostas inesperadas ou indesejadas do programa, bem como
    o usuário deve estar ciente que ponto final(.), virgula(,) ou outros caracteres especiais mudam a palavra. Por exemplo: "hobbit" != "Hobbit" != "hobbit."
    """
    if isArquivo == True:
            palavras = []
            palavras_alteradas = []
            with open( texto, 'r' ) as arq:
                # acessa cada linha    
                for line in arq:
                    # acessa cada palavra      
                    for word in line.split():
                        # armazena as palavras em uma lista         
                        palavras.append(word)

            #buscando a palavra desejada
            if chave in palavras:
                for palavra in palavras:
                    if palavra == chave:
                        palavras_alteradas.append(f"[bold]  {palavra} [/bold]")
                    else:
                        palavras_alteradas.append(palavra)
                #juntando as palavras
                frase = " ".join(palavras_alteradas)
                console.print(frase)
            else:
                console.print('Palavra não encontrada')
            
    if isArquivo == False:
        frase = texto.split(" ")
        palavras_alteradas  = []
        if chave in frase:
            for palavra in frase:
                if palavra == chave:
                    palavras_alteradas.append(f"[bold]{palavra}[/bold]")
                else:
                    palavras_alteradas.append(palavra)
            
            nova_frase = " ".join(palavras_alteradas)
            console.print(nova_frase)
        else:
            console.print('Palavra não encontrada')



#changeColor("/home/PDITA274/Documentos/teste.txt", "violet", True)
#highlightWord("/home/PDITA274/Documentos/teste.txt", "livro", True)