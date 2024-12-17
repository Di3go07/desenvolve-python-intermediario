from abc import ABC, abstractmethod
from datetime import datetime

# CLASSE ABSTRATA 
class EventoABC(ABC):
    def __init__(self, titulo, descricao):
        self._titulo = titulo
        self.descricao = descricao
        self.is_concluido = False

    def isConcluido(self):
        """
        Quando chamado, atualiza o estado da instância caso o horário atual ultrapasse o do evento.
        """
        pass


# CLASSE AUXILIAR
class DataHora:

    @staticmethod
    def FormataData(data):
        """
        Converte uma string no formato 'dd/mm/yyyy HH:MM' em um objeto datetime.
        """
        try:
            return datetime.strptime(data, "%d/%m/%Y %H:%M")
        except ValueError:
            raise ValueError('Data inválida! Use o formato: "dd/mm/aaaa hh:mm"')

    def __init__(self, data):
        self._data_hora = self.FormataData(data)

    def __str__(self):
        dia = self._data_hora.strftime("%d/%m/%Y %H:%M")
        return dia

    def isPassado(self):
        """
        verifica se a data do evento já passou
        """ 
        return self._data_hora < datetime.now()

    def somaDias(self, num):
         if isinstance(num, int):
            try: 
                dia_atual = int(self._data_hora.strftime("%d"))
                if dia_atual + num <= 30: #caso a data continue no mesmo mês
                    dia = dia_atual + num
                    mes = int(self._data_hora.strftime("%m"))
                    ano = self._data_hora.strftime("%Y")                    
                    hora = self._data_hora.strftime("%H:%M")
                    nova_data = f'{dia:02}/{mes:02}/{ano} {hora}'
                    return nova_data

                else: #caso a proxima data seja em outro mês
                    quantidade_mes = num // 30
                    if quantidade_mes <= 1: #lidando caso a data seja proxima ao fim do mes e o num muito baixo
                        quantidade_mes = 1

                    dia = (dia_atual + num) - (30 * quantidade_mes)
                    if dia >= 30: #lidando caso a data seja proxima ao fim do mes e o num muito alto
                        dia = dia - 30
                        quantidade_mes += 1

                    mes = int(self._data_hora.strftime("%m")) + quantidade_mes 
                    ano = self._data_hora.strftime("%Y")
                    hora = self._data_hora.strftime("%H:%M")
                    nova_data = f'{dia:02}/{mes:02}/{ano} {hora}'
                    return nova_data
            except ValueError:
                raise ValueError("Pensando demais no futuro. Não é possivel adiar tanto assim o evento")
                #erro lançado caso o evento se adie até o ano seguinte

    @property
    def data_hora(self):
        return self._data_hora

    @data_hora.setter
    def data_hora(self, valor):
        self._data_hora = self.FormataData(valor)


# CLASSE PRINCIPAL 
class EventoUnico(EventoABC):
    def __init__(self, titulo, descricao, date):
        super().__init__(titulo, descricao)
        self._data = DataHora(date)

    def isConcluido(self):
        """
        Atualiza a propriedade `is_concluido` se a data já passou.
        """
        return self._data.isPassado()
         

    def __str__(self):
        return f'Evento: {self._titulo}; Data: {self._data}; Descrição: {self.descricao}; Concluído: {self.isConcluido()}'

    @property
    def editar_data_hora(self):
        """
        Acessa a data e hora do evento.
        """
        return self._data.dataEhora

    @editar_data_hora.setter
    def editar_data_hora(self, valor):
        """
        Modifica a data e hora do evento.
        """
        self._data.dataEhora = valor

class EventoRecorrente(EventoABC):
    _lista_eventos = []

    def __init__(self, titulo, descricao, data_inicio, data_final, intervalo):
        super().__init__(titulo, descricao)
        self._data_hora_inicial = DataHora(data_inicio)
        self._data_hora_final = DataHora(data_final)
        self.intervalo_dias = intervalo
        self.preencherEventos()

    def isConcluido(self):
        """
        Atualiza a propriedade `is_concluido` se a data já passou.
        """
        return self._data_hora_inicial.isPassado()

    def __str__(self):
        for data in self._lista_eventos:
            print(f'Evento: {self._titulo}; Data: {data}; Descrição: {self.descricao}; Concluído: {self.isConcluido()}')
        return 'Eventos recorrentes'

    def preencherEventos(self):
        i = 1
        while True:
            num = self.intervalo_dias * i
            dia = DataHora.somaDias(self._data_hora_inicial, num)
            self._lista_eventos.append(dia)

            if dia == str(self._data_hora_final):
                break
            
            i += 1




