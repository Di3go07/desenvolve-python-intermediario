from classes import EventoUnico
from classes import EventoRecorrente
from datetime import datetime

evento1 = EventoUnico('Reunião','Sala 302, prédio da esquina', '05/10/2025 16:30')
evento2 = EventoRecorrente('Monitoria', 'Sala 302, prédio da esquina', '28/01/2024 16:30', '28/03/2024 16:30', 5)
evento3 = EventoUnico('Apresentação','Sala 302, prédio da esquina', '05/01/2026 16:30')
evento4 = EventoRecorrente('Seminario', 'Sala 302, prédio da esquina', '28/01/2025 14:15', '28/11/2025 14:15', 30)
evento5 = EventoUnico('Prova','Sala 302, prédio da esquina', '25/06/2024 08:30')

eventos = [evento1, evento2, evento3, evento4, evento5]

for evento in eventos:
    print(evento)
    print('=' * 150)