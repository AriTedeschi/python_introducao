from datetime import date, time, datetime, timedelta

# data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
# hora = time(hour=13, minute=14, second=00)
# print('{} às {}'.format(data, hora))

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(type(data_atual))

    print(data_atual.strftime('%d/%m/%Y'))
    print(type(data_atual.strftime('%d/%m/%Y')))

    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=10, second=30)
    print(type(horario))
    print(horario)
    print(horario.strftime('%H:%M:%S'))
    print(horario.strftime('%c'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(type(data_atual))
    print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.weekday)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2020, 5, 6, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2021'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))

    # - 1 ano
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)



if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_date()
    trabalhando_com_datetime()