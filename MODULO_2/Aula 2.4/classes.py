from datetime import datetime

class Evento:
    ### ATRIBUTOS/DADOS ###

    #atributo da classe
    total_eventos = 0

    #atributo constructor
    def __init__(self, titulo, data, descricao):
        """
        Função construtora que cria uma instância nova para a classe
        """
        try: 
            self.data = datetime.strptime(data, "%d/%m/%Y %H:%M")    
            self.titulo = titulo
            self.descricao = descricao
            self.is_concluido = False
            Evento.total_eventos += 1 #acrescenta um a variável da classe sempre que uma nova instância for criada

        except ValueError:
            print("Algo deu errado. Use a função 'valida_eventos' para verificar se os dados inseridos são válidos")


    #metodos mágicos
    def __str__(self):
        """
        Retorna uma representação humanamente legivel ao objeto, voltada aos usuários finais do projeto
        """
        return f'Evento: {self.titulo}, Data: {self.data}, Descrição: {self.descricao}, Concluido: {self.is_concluido}'
    
    def __eq__(self, other):
        """
        Permite definir o que ira acontecer quando comparar uma instância dessa classe com outro elemento
        """
        if isinstance(other, Evento):
            return self.data == other.data
        elif isinstance(other, datetime): #compara se é igual ao horario atual do computador
            return self.data == other
        elif isinstance(other, str):
            #compara se a data da instância é igual à fornecida
            try: 
                return self.data == datetime.strptime(other, "%d/%m/%Y %H:%M")
            except ValueError:
                return "Algo deu errado. Use a função 'valida_eventos' para verificar se os dados inseridos são válidos"
                #resposta executada caso a data não esteja na formatação certa

    def __lt__(self, other):
        """
        Permite definir o que ira acontecer quando comparar uma instância dessa classe com outro elemento
        """
        if isinstance(other, Evento):
            return self.data < other.data
        elif isinstance(other, datetime): #compara se é menor que o horario atual do computador
            return self.data < other
        elif isinstance(other, str):
            #compara se a data da instância é igual à fornecida
            try: 
                return self.data < datetime.strptime(other, "%d/%m/%Y %H:%M")
            except ValueError:
                return "Algo deu errado. Use a função 'valida_eventos' para verificar se os dados inseridos são válidos"
                #resposta executada caso a data não esteja na formatação certa

    def __gt__(self, other):
        """
        Permite definir o que ira acontecer quando comparar uma instância dessa classe com outro elemento
        """
        if isinstance(other, Evento):
            return self.data > other.data
        elif isinstance(other, datetime): #compara se é menor que o horario atual do computador
            return self.data > other
        elif isinstance(other, str):
            #compara se a data da instância é igual à fornecida
            try: 
                return self.data > datetime.strptime(other, "%d/%m/%Y %H:%M")
            except ValueError:
                return "Algo deu errado. Use a função 'valida_eventos' para verificar se os dados inseridos são válidos"
                #resposta executada caso a data não esteja na formatação certa

    #metodo da instância
    def isConcluido(self):
        """
        Quando chamado, atualiza o estado da instância caso o horario do computador ultrapasse o do evento
        """
        if self.data <= datetime.now():
            self.is_concluido = True


    #metodo de classe
    @classmethod 
    def num_eventos(cls):
        """
        Retorna a quantidade de eventos instanciados
        """
        print(f'Total de eventos: {cls.total_eventos}')

    #static method
    @staticmethod
    def valida_evento(titulo, data, descricao):
        """
        Verifica se os dados estão corretos
        """
        teste_titulo = isinstance(titulo, str)
        try: #verifica se a data está no formato correto
            datetime.strptime(data, '%d/%m/%Y %H:%M')
            teste_data = True
        except ValueError:
            print('Data invalida! Insira dessa forma: "01/03/2018 12:30"')
            return
        teste_descricao = isinstance(descricao, str)

        if teste_titulo == True and teste_data == True and teste_descricao == True:
            print('Os dados estão corretos!')
        else:
            print('Ops, algo deu errado...')

