# Modulo 1 - Exercicio Rich
Modulos para costumizar a saida no terminal da impressão de um texto

## Ambiente virtual
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

## Linhas de comando
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


##Argumentos
