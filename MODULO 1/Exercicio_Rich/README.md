# Modulo 1 - Exercicio Rich
Modulos para costumizar a saida no terminal da impressão de um texto

## 🖥️​ Ambiente virtual
Como criar o ambiente virtual Python desse programa
1. Abra no terminal a pasta do projeto
   
2. Se ainda não tiver instalado, instale a ferramenta `virtualenv`:
   ```
   pip install virtualenv
   ```

   
3. Crie um ambiente virtual na pasta do seu projeto:
   ```
   virtualenv nome_do_ambiente
   ```
   ou
   ```
   python3 -m venv nome_do_ambiente
   ```

   
4. Ative o ambiente virtual:
   - No Windows:
     ```
     .\nome_do_ambiente\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source nome_do_ambiente/bin/activate
     ```


5. Agora você está no ambiente virtual. Você pode instalar as dependências específicas do programa usando o `pip` e acessando o arquivo 'requirements'. Por exemplo:
   ```
   python3 -m pip install -r requirements.txt
   ```
   
Lembre-se de que, ao terminar o desenvolvimento, você pode desativar o ambiente virtual digitando `deactivate` no terminal.

O ambiente virtual ajuda a isolar as dependências do seu projeto, facilitando o gerenciamento e evitando conflitos entre diferentes projetos Python.

## 👨‍💻​ Linhas de comando
Como acessar os módulos pelo terminal

1. Abra o terminal na pasta 'Scripts' de 'Exercicio_Rich'
2. Execute esse comando para verificar os argumentos disponíveis:
   ```
   python3 main.py
   ```
3. Execute esse comando para conhcer cada argumento:
   ```
   python3 main.py -h
   ```
5. Selecione o argumento desejado e insira o texto a ser impresso, por exemplo:
   ```
   python3 main.py -a -c blue ./texto.txt
   ```
      ```
   python3 main.py -c blue "Numa toca no chão vivia um hobbit"
   ```
Lembre-se de que o argumento -a sempre deve ser informado caso o texto fornecido pelo usuário seja o caminho para um arquivo


## 📃​ Argumentos
Função de cada argumento do programa

**Argumento obrigátorio**
   - text -> digite um texto ou o caminho para um diretório

**Argumento opcionais**
   - -h => mostra uma mensagem de ajuda
   - -a => argumento que deve ser passado sempre que o texto for o caminho de um diretório
   - -c COLOR => argumento que muda a cor do texto na impressão e necessita de um valor
   - -hlw HIGHLIGHTWORD => deixa em destaque uma palavra do texto na impressão e necessita de um valor
   - -t TITULO => cria um titulo ao texto impresso e necessita de um valor
   - -st SUBTITULO SUBTITULO => cria um titulo e subtitulo para o texto impresso, necessita de dois valores
   - -lt => imprime cada paragrafo do documento ou do texto inserido pelo usuário
   - -pt => imprime todo o texto e apresenta uma barra de progresso em relação ao processo de leitura feito pelo computador

Detalhe: com exceção do argumento -a, o usuario só pode passsar um argumento de cada vez


Para mais detalhe acerca das funções dos argumentos, consulte os arquivos html na pasta 'docs'
