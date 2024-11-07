import style
import painel
import progresso
import argparse


#salvando o interpretador de argumentos
parser = argparse.ArgumentParser()

#Informações principais
parser.add_argument('texto', type=str, help='Digite um texto ou um caminho de diretório')
parser.add_argument('-a', action='store_true', help="informa se o texto inserido é um caminho para um diretório")

#COMANDOS STYLE
parser.add_argument('-c', '--color', type=str, help='Digite uma cor')
parser.add_argument('-hlW', '--highlightWord', type=str, help='Digite uma palavra para ser destacada')

#COMANDOS PAINEL
parser.add_argument('-t', '--titulo', type=str, help='digite um titulo para a mensagem exibida')
parser.add_argument('-st', '--subtitulo', nargs=2, type=str, help='digite um título e um subtítulo para a mensagem exibida')

#COMANDOS PROGRESSO
parser.add_argument('-lt', '--lerTexto', action='store_true', help='imprime cada paragrafo do documento ou o texto inserido pelo usuário')
parser.add_argument('-pt', '--printTexto', action='store_true', help='imprime todo o texto e apresenta uma barra de progresso em relação ao processo de leitura feito pelo computador')

#PROCESSAMENTO 
args = parser.parse_args() #interpreta o comando

###É UM DIRETORIO
if args.a == True:
    if args.color:
        style.changeColor(args.texto, args.color, True)
    if args.highlightWord:
        style.highlightWord(args.texto,args.highlightWord, True)
    if args.titulo:
        painel.definirTitulo(args.texto,args.titulo, True)
    if args.subtitulo:
        painel.comSubtitulo(args.texto,args.subtitulo[0], args.subtitulo[1], True)
    if args.lerTexto:
        progresso.lerTexto(args.texto, True)
    if args.printTexto:
        progresso.imprimirTexto(args.texto, True)
###NÃO É UM DIRETORIO
else:
    if args.color:
        style.changeColor(args.texto, args.color, False)
    if args.highlightWord:
        style.highlightWord(args.texto,args.highlightWord, False)
    if args.titulo:
        painel.definirTitulo(args.texto,args.titulo, False)
    if args.subtitulo:
        painel.comSubtitulo(args.texto,args.subtitulo[0], args.subtitulo[1], False)
    if args.lerTexto:
        progresso.lerTexto(args.texto, False)
    if args.printTexto:
        progresso.imprimirTexto(args.texto, False)