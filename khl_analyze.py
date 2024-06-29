import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import warnings

# Подавление предупреждений
warnings.filterwarnings("ignore")

def Season(year):
    global khl, div
    if year == '2018':
        khl = pd.read_csv('khl_2018_19.csv')
        diviz = dict.fromkeys(
            ['СКА', 'Йокерит', 'Динамо М', 'Спартак', 'Динамо Р', 'Северсталь'], 'Боброва')
        diviz.update(dict.fromkeys(
            ['ЦСКА', 'Локомотив', 'ХК Сочи', 'Витязь', 'Динамо Мн', 'Слован'], 'Тарасова'))
        diviz.update(dict.fromkeys(['Автомобилист', 'Металлург Мг',
                                    'Ак Барс', 'Торпедо НН', 'Трактор', 'Нефтехимик'], 'Харламова'))
        diviz.update(dict.fromkeys(['Барыс', 'Авангард', 'Салават Юлаев',
                                    'Сибирь', 'Куньлунь РС', 'Адмирал', 'Амур'], 'Чернышева'))
        div = pd.DataFrame(diviz.items(), columns=['Клуб', 'Д'])
    elif year == '2019':
        khl = pd.read_csv(
            'khl_2019_20.csv')
        diviz = dict.fromkeys(
            ['СКА', 'Йокерит', 'Динамо М', 'Спартак', 'Динамо Р', 'Северсталь'], 'Боброва')
        diviz.update(dict.fromkeys(
            ['ЦСКА', 'Локомотив', 'ХК Сочи', 'Витязь', 'Динамо Мн', 'Торпедо НН'], 'Тарасова'))
        diviz.update(dict.fromkeys(
            ['Автомобилист', 'Ак Барс', 'Сибирь', 'Металлург Мг', 'Нефтехимик', 'Трактор'], 'Харламова'))
        diviz.update(dict.fromkeys(
            ['Барыс', 'Авангард', 'Салават Юлаев', 'Амур', 'Куньлунь РС', 'Адмирал'], 'Чернышева'))
        div = pd.DataFrame(diviz.items(), columns=['Клуб', 'Д'])
    elif year == '2020':
        khl = pd.read_csv(
            'khl_2020_21.csv')
        diviz = dict.fromkeys(
            ['СКА', 'Йокерит', 'Северсталь', 'Спартак', 'Витязь', 'ХК Сочи'], 'Боброва')
        diviz.update(dict.fromkeys(
            ['ЦСКА', 'Динамо М', 'Локомотив', 'Динамо Мн', 'Динамо Р'], 'Тарасова'))
        diviz.update(dict.fromkeys(['Ак Барс', 'Металлург Мг', 'Трактор',
                                    'Автомобилист', 'Торпедо НН', 'Нефтехимик'], 'Харламова'))
        diviz.update(dict.fromkeys(
            ['Авангард', 'Салават Юлаев', 'Барыс', 'Сибирь', 'Амур', 'Куньлунь РС'], 'Чернышева'))
        div = pd.DataFrame(diviz.items(), columns=['Клуб', 'Д'])
    elif year == '2021':
        khl = pd.read_csv(
            'khl_2021_22.csv')
        diviz = dict.fromkeys(
            ['СКА', 'Йокерит', 'Торпедо', 'Спартак', 'Витязь', 'ХК Сочи'], 'Боброва')
        diviz.update(dict.fromkeys(
            ['ЦСКА', 'Динамо М', 'Северсталь', 'Локомотив', 'Динамо Мн', 'Динамо Р'], 'Тарасова'))
        diviz.update(dict.fromkeys(
            ['Куньлунь РС', 'Автомобилист', 'Нефтехимик', 'Ак Барс', 'Трактор', 'Металлург Мг'], 'Харламова'))
        diviz.update(dict.fromkeys(
            ['Адмирал', 'Амур', 'Барыс', 'Сибирь', 'Авангард', 'Салават Юлаев'], 'Чернышева'))
        div = pd.DataFrame(diviz.items(), columns=['Клуб', 'Д'])
    else:
        print('Такого сезона в базе данных нет!!!')
        sys.exit()


def WinLose(data):
    # Забитые шайбы первой команды
    Teams.loc[Teams['Клуб'] == data[1], 'ШЗ'] += (data[8]+data[10]+data[12])
    # Забитые шайбы второй команды
    Teams.loc[Teams['Клуб'] == data[2], 'ШЗ'] += (data[9]+data[11]+data[13])
    # Пропущенные шайбы первой команды
    Teams.loc[Teams['Клуб'] == data[1], 'ШП'] += (data[9]+data[11]+data[13])
    # Пропущенные шайбы второй команды
    Teams.loc[Teams['Клуб'] == data[2], 'ШП'] += (data[8]+data[10]+data[12])
    if data[12] > data[13]:
        Teams.loc[Teams['Клуб'] == data[1], 'ВБ'] += 1  # +1 ВБ для команды_1
        Teams.loc[Teams['Клуб'] == data[2], 'ПБ'] += 1  # +1 ПБ для команды_2
    elif data[12] < data[13]:
        Teams.loc[Teams['Клуб'] == data[2], 'ВБ'] += 1  # +1 ВБ для команды_2
        Teams.loc[Teams['Клуб'] == data[1], 'ПБ'] += 1  # +1 ПБ для команды_1
    elif data[10] > data[11]:
        Teams.loc[Teams['Клуб'] == data[1], 'ВО'] += 1  # +1 ВО для команды_1
        Teams.loc[Teams['Клуб'] == data[2], 'ПО'] += 1  # +1 ПО для команды_2
    elif data[10] < data[11]:
        Teams.loc[Teams['Клуб'] == data[2], 'ВО'] += 1  # +1 ВО для команды_2
        Teams.loc[Teams['Клуб'] == data[1], 'ПО'] += 1  # +1 ПО для команды_1
    elif data[8] > data[9]:
        Teams.loc[Teams['Клуб'] == data[1], 'В'] += 1  # +1 В для команды_1
        Teams.loc[Teams['Клуб'] == data[2], 'П'] += 1  # +1 П для команды_2
    elif data[8] < data[9]:
        Teams.loc[Teams['Клуб'] == data[2], 'В'] += 1  # +1 В для команды_2
        Teams.loc[Teams['Клуб'] == data[1], 'П'] += 1  # +1 П для команды_1


def Trouble(data):
    if data[3] == '+ — -':
        Teams.loc[Teams['Клуб'] == data[1], 'В'] += 1
        Teams.loc[Teams['Клуб'] == data[2], 'П'] += 1
        Teams.loc[Teams['Клуб'] == data[1], 'И'] += 1
        Teams.loc[Teams['Клуб'] == data[2], 'И'] += 1
        data[3] = '0:0'
        data[4] = '0:0'
        data[5] = '0:0'
    elif data[3] == '- — +':
        Teams.loc[Teams['Клуб'] == data[1], 'П'] += 1
        Teams.loc[Teams['Клуб'] == data[2], 'В'] += 1
        Teams.loc[Teams['Клуб'] == data[1], 'И'] += 1
        Teams.loc[Teams['Клуб'] == data[2], 'И'] += 1
        data[3] = '0:0'
        data[4] = '0:0'
        data[5] = '0:0'

Season(input('Введите год начала сезона: '))

# Удаление пустого столбца и стобца "Номер"
khl = khl.drop(['Unnamed: 0', 'Номер'], axis=1)
# Добавление нулей в овертаймы
khl.loc[(khl['Овертайм'] == ':'), 'Овертайм'] = '0:0'
# Добавление нулей в буллиты
khl.loc[(khl['Буллиты'] == ':'), 'Буллиты'] = '0:0'

NameTeams = khl['Команда_1'].unique()  # Все уникальные названия команд
NumTeams = len(NameTeams)             # Количество команд
d = {'Клуб': NameTeams,               # Данные для таблицы
     'И': np.zeros(NumTeams, int),    # Количество проведенных игр
     'В': np.zeros(NumTeams, int),    # Выигрыши в основное время
     'ВО': np.zeros(NumTeams, int),   # Выигрыши в овертайме
     'ВБ': np.zeros(NumTeams, int),   # Выигрыши в послематчевых буллитах
     'ПБ': np.zeros(NumTeams, int),   # Проигрыши в послематчевых буллитах
     'ПО': np.zeros(NumTeams, int),   # Проигрыши в овертайме
     'П': np.zeros(NumTeams, int),    # Проигрыши в основное время
     'Ш': np.zeros(NumTeams, str),    # Шайбы
     'О': np.zeros(NumTeams, int),    # Количество набранных очков
     '%О': np.zeros(NumTeams, float),  # Процент набранных очков
     'ШЗ': np.zeros(NumTeams, int),   # Количество забитых шайб
     'ШП': np.zeros(NumTeams, int),   # Количество полученных шайб
     }
Teams = pd.DataFrame(data=d)  # Создание таблицы

khl.apply(Trouble, axis=1)

khl[['ОВ-1', 'ОВ-2']] = (khl['Период_1'].str.split(':', expand=True).astype(int) + khl['Период_2'].str.split(':', expand=True).astype(int) +
                         khl['Период_3'].str.split(':', expand=True).astype(int))   # Разделение шайб, забитых в основное время
# Разделение шайб, забитых в овертайм
khl[['Овер-1', 'Овер-2']
    ] = khl['Овертайм'].str.split(':', expand=True).astype(int)
# Разделение шайб, забитых в буллиты
khl[['Бул-1', 'Бул-2']
    ] = khl['Буллиты'].str.split(':', expand=True).astype(int)

khl.apply(WinLose, axis=1)                     # Выполнение всех расчетов

# Подсчет количества игр
Teams['И'] = Teams.loc[:, 'В':'П'].sum(axis=1)
# Заполнение столбца "Шайбы"
Teams['Ш'] = Teams['ШЗ'].astype(str)+'-'+Teams['ШП'].astype(str)
# Удаление лишних строк 'ШЗ'и'ШП'
Teams = Teams.drop(['ШЗ', 'ШП'], axis=1)
Teams['О'] = (Teams['В']+Teams['ВО']+Teams['ВБ'])*2 + \
    Teams['ПБ']+Teams['ПО']  # Подсчет очков
# Заполнение столбца "Процент набранных очков"
Teams['%О'] = round(Teams['О']/(Teams['И']*2)*100, 2)
# Сортировка по очкам
Teams = Teams.sort_values(by='О', ascending=False)
# Переставление индексов
Teams = Teams.reset_index(drop=True)
# Объединение для дивизиона
Teams = pd.merge(Teams, div)
# print(Teams)

Bobrov = Teams[Teams['Д'] == 'Боброва']
Bobrov = Bobrov.reset_index(drop=True)
Bobrov.index += 1
Bobrov = Bobrov.drop('Д', axis=1)

Tarasov = Teams[Teams['Д'] == 'Тарасова']
Tarasov = Tarasov.reset_index(drop=True)
Tarasov.index += 1
Tarasov = Tarasov.drop('Д', axis=1)

Harlamov = Teams[Teams['Д'] == 'Харламова']
Harlamov = Harlamov.reset_index(drop=True)
Harlamov.index += 1
Harlamov = Harlamov.drop('Д', axis=1)

Chernisheva = Teams[Teams['Д'] == 'Чернышева']
Chernisheva = Chernisheva.reset_index(drop=True)
Chernisheva.index += 1
Chernisheva = Chernisheva.drop('Д', axis=1)

print('\n Дивизион Боброва \n', Bobrov,
      '\n\n Дивизион Тарасова \n', Tarasov,
      '\n\n Дивизион Харламова', '\n', Harlamov,
      '\n\n Дивизион Чернышева', '\n', Chernisheva)

def histogramOfCommandPoints():
    x = np.array(Teams['Клуб'])  # заполнение осей нужной информацией
    y = np.array(Teams['О'])
    fig, ax = plt.subplots()  # создание полотна
    ax.bar(x, y)  # построение гистограммы
    # поворот меток оси Ох на 270 градусов против часовой стрелки
    plt.xticks(rotation=270)
    ax.set_title('Гистограмма набранных командами очков')
    plt.show()  # показ графика

histogramOfCommandPoints()