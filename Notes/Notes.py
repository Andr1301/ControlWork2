import csv
from datetime import datetime
import os
import uuid
import pandas as pd

"""Для решения задачи решено было использовать pandas, поскольку он позволяет удобно редактировать 
содержимое любой ячейки. Идентификаторы заметок генерируются при помощи uuid, 
дата проставляется в момент создания заметки, сортировка по дате создания происходит автоматически"""

title_id = 'Id'
title_name = 'Name'
title_date = 'Date'
title_text = 'Text'

def input_title():
    """Функция отвечает за ввод заголовка и его проверку на уникальность"""
    df = pd.read_csv('Notes.csv', delimiter = ';')
    print('Введите заголовок заметки: ')
    namecheck = False
    while namecheck == False:
        name = input()
        if name in df['Name'].values:
            print('Заметка с таким названием уже существует! Введите другое название!')
        else: namecheck = True
    return name

def input_text():
    """Функция отвечает за ввод текста заметки"""
    return input("Введите текст заметки: ")

def create_note():
    """Функция, создающая новую заметку. Перед созданием заметки проверяется наличие заголовков датафрейма в файле"""
    with open('Notes.csv', 'a', encoding = 'utf-8') as file:
        if os.stat('Notes.csv').st_size == 0:
            data = {'Id': [], 'Name': [], 'Date': [], 'Text': []}
            df = pd.DataFrame(data, columns=['Id', 'Name', 'Date', 'Text'])
            df.to_csv('Notes.csv', header=True, index=False, sep=';')
        name = input_title()
        text = input_text()
        date = datetime.now()
        id = uuid.uuid4()
        new_row = {'Id': id, 'Name': name, 'Date': date, 'Text': text}
        data = pd.DataFrame([new_row])
        data.to_csv(file, index=False, sep=';', header = False)
    file.close()

def show_notes():
    """Функция, выводящая на экран список заметок (только заголовок и дату) и выбранную заметку (только текст заметки)"""
    if os.stat('Notes.csv').st_size == 0:
        print('--------------------')
        print('Заметки отстутствуют!')
        print('--------------------')
    else:
        df = pd.read_csv('Notes.csv', delimiter = ';')
        print(df.iloc[:,[1, 2]])
        num = int(input('Выберите номер заметки: '))
        if num>0 and num<=df.shape[0]:
            print('--------------------')
            print(df.iloc[[num],[3]])
            print('--------------------')
        else:
            print('Выбран неверный номер заметки!')

def redact_note():
    """Функция, отвечающая за редактирование заметки"""
    if os.stat('Notes.csv').st_size == 0:
        print('--------------------')
        print('Заметки отстутствуют!')
        print('--------------------')
    else:
        df = pd.read_csv('Notes.csv', delimiter = ';')
        print(df.iloc[:,[1, 2]])
        num = int(input('Выберите номер заметки: '))
        if num>0 and num<=df.shape[0]:
            print('--------------------')
            print(df.iloc[[num],[3]])
            df = pd.read_csv('Notes.csv', delimiter = ';')
            print('--------------------')
            print('Введите новый текст заметки: ')       
            df.iloc[num, 3] = input_text()
            df.to_csv('Notes.csv', index = False, sep = ';')
        else:
            print('Выбран неверный номер заметки!')

def delete_note():
    """Функция, отвечающая за удаление заметки"""
    if os.stat('Notes.csv').st_size == 0:
        print('--------------------')
        print('Заметки отстутствуют!')
        print('--------------------')
    else:
        df = pd.read_csv('Notes.csv', delimiter = ';')
        print(df.iloc[:,[1, 2]])
        num = int(input('Выберите номер удаляемой заметки: '))
        if num>=0 and num<=df.shape[0]:
            df = df.drop(labels = [num])
            df.to_csv('Notes.csv', index = False, sep = ';')
            print('Заметка удалена!')
        else:
            print('Выбран неверный номер заметки!')

def date_notes():
    """Функция, осуществляющая поиск заметок по вводимой пользователем дате"""
    if os.stat('Notes.csv').st_size == 0:
        print('--------------------')
        print('Заметки отстутствуют!')
        print('--------------------')
    else:
        df = pd.read_csv('Notes.csv', delimiter = ';')
        print('Введите дату в формате "yyyy-mm-dd": ')
        date = input()
        notes_by_date = df.loc[df['Date'].str.contains(date)]
        print(notes_by_date)


def interface():
    with open('Notes.csv', 'a', encoding='utf-8'):
        pass
    """Интерфейс"""
    choice = ''
    while choice != '6':
        print(
            "Варианты действия: \n" \
            "1 - Создать заметку \n" \
            "2 - Вывести заметку на экран список заметок \n" \
            "3 - Редактировать заметку \n" \
            "4 - Удалить заметку \n" \
            "5 - Поиск заметок по дате \n" \
            "6 - Выход"
            )
        print()
        choice = input("Выберите номер действия: ")
        print()
        while choice not in ('1', '2', '3', '4', '5', '6'):
            print("Некорректный ввод данных!")
            choice = input("Выберите номер действия: ")
            print()
        match choice:
            case '1':
                create_note()
            case '2':
                show_notes()
            case '3':
                redact_note()
            case '4':
                delete_note()
            case '5':
                date_notes()
            case '6':
                print('Всего доброго!')              

if __name__ == '__main__':
    interface()