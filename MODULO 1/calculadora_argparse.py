import argparse

#salvando o interpretador de argumentos
parser = argparse.ArgumentParser()

#ARGUMENTOS
parser.add_argument('número', nargs = 2, type=int, help="passe dois números como parametros")
#parâmetro nargs exige dois argumentos

parser.add_argument('-a','--adicao', action='store_true', help='realiza uma adição')

parser.add_argument('-s','--subtracao', action='store_true', help='realiza uma subtração')

parser.add_argument('-m','--multiplicacao', action='store_true', help='realiza uma multiplicação')

parser.add_argument('-d','--divisao', action='store_true', help='realiza uma divisão')


#PROCESSAMENTO 
args = parser.parse_args() #interpreta o comando

if args.adicao == True:
    print(args.número[0] + args.número[1])
elif args.subtracao == True:
    print(args.número[0] - args.número[1])
elif args.multiplicacao == True:
    print(args.número[0] * args.número[1])
elif args.divisao == True:
    print(args.número[0] / args.número[1])
else:
    problema = input('Precisa de ajuda?[Y/n] ')
    if problema == 'Y':
            parser.print_help()
    else:
        print('beleza')
