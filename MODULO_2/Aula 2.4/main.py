from classes import Evento
from datetime import datetime
import time

Evento.num_eventos()

print('=============================================================================')

time.sleep(2)

#erro ao criar evento
evento1 = Evento('jogar', '11/12/2024', 'aaaaaaaaa')

print('=============================================================================')

time.sleep(2)

#verifica os dados no evento
Evento.valida_evento('jogar', '10/12/2024 20:30', 25)
print(' ')
time.sleep(2)
Evento.valida_evento('jogar', '10/12/2024 20:30', 'aaaaaaaaaa')

print('=============================================================================')

time.sleep(2)

#criar eventos
evento1 = Evento('jogar', '10/12/2024 20:30', 'aaaaaaaaaa')
evento2 = Evento('basquete', '11/03/2025 15:45', 'aaaaaaaaa')
evento3 = Evento('cinema', '09/12/2024 21:00', 'aaaaaaaaaaa')
evento1.isConcluido()
evento2.isConcluido()
evento3.isConcluido()

#imprimir seus dados
print(evento1)
print(evento2)
print(evento3)
Evento.num_eventos()

print('=============================================================================')

time.sleep(2)

#comparando horario dos eventos
print(evento2 == evento1)
print(evento1 == '10/12/2024 20:30')
print(evento2 < datetime.now())
print(evento2 > datetime.now())
