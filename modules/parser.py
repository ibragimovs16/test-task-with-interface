# -*- coding: UTF-8 -*-

from threading import Thread
import requests
from bs4 import BeautifulSoup


class Parser:
    __exams = None
    __directions = None
    __info = None

    def __init__(self):
        print('Класс инициализирован.')

    def load(self):
        self.__set_exams()
        self.__exams = self.get_exams()
        self.__directions = self.get_directions(self.__exams[0])
        self.__info = self.get_info(self.__directions[0])

    def get_exams(self):
        return self.__exams

    def get_directions(self, exam=None):
        if exam is not None:
            self.__set_direction(exam)

        return self.__directions

    def get_info(self, direction=None):
        if direction is not None:
            self.__set_info(direction)

        return self.__info

    def __set_exams(self):
        """
        Функция для получения списка вступительных экзаменов.
        :return: Возвращает список вступительных экзаменов
        """

        url = 'https://uni-dubna.ru/Entrance/Navigator'
        page_source = requests.get(url).text

        soup = BeautifulSoup(page_source, 'lxml')
        exams = soup.find('div', class_='wrapper') \
            .find('select', id='exam') \
            .find_all('option')

        for i in range(len(exams)):
            exams[i] = exams[i].text

        self.__exams = exams

    def __set_direction(self, exam):
        """
        Функция для получения направлений подготовки по указаному вступительному экзамену.
        :param exam: Название экзамена.
        :return: Возвращает список направлений подготовки.
        """
        url = 'https://uni-dubna.ru/Entrance/GetGuidelines'

        data = {
            'limit': 25,
            'classification': 'Бакалавриат',
            'form': 'Очная',
            'exam': exam
        }

        res = requests.post(url, data).text

        directions = []

        soup = BeautifulSoup(res, 'lxml')
        tmp = soup.find_all('div', class_='panel')

        def get_current_direction(index):
            """
            Вспомогательная функция для реализации многопоточной обработки информации.
            """
            bs4 = BeautifulSoup(str(tmp[index]), 'lxml')
            info = bs4.find('a')
            index = info['id'][6:]
            name = info.text.strip()
            directions.append([index, name])

        for i in range(len(tmp)):
            thread = Thread(target=get_current_direction, args=(i,))
            thread.start()
            thread.join()

        self.__directions = directions

    @staticmethod
    def __get_about(res):
        """
        Функция для получения информации о каждом профиле направления.
        """
        soup = BeautifulSoup(str(res), 'lxml')
        sections = soup.find('div', class_='header').find_all('a')

        about = []

        def get_current_information(i):
            bs4 = BeautifulSoup(str(sections[i]), 'lxml')

            index = bs4.find('a')['href'][6:]
            name = bs4.text.strip()

            url = 'https://uni-dubna.ru/Entrance/GetChair'

            data = {
                'limit': 25,
                'id': index
            }

            response = requests.post(url, data).text

            bs4 = BeautifulSoup(response, 'lxml')
            data = bs4.find_all('div', class_='tab-pane-item')

            result = ''
            final = ''

            for k in [3, 4]:
                bs4 = BeautifulSoup(str(data[k]), 'lxml')
                description = bs4.find('div', 'col-sm-4').text.strip()
                info = bs4.find('div', 'col-sm-8').text.strip()

                result += f'{description}: {info}\n'

            final += f'     {name}\n\n{result}\n'
            about.append(final)

        for j in range(1, len(sections)):
            thread = Thread(target=get_current_information, args=(j,))
            thread.start()
            thread.join()

        return about

    def __set_info(self, direction):
        """
        Функция, возвращающая полную информацию о выбранном направлении.
        :param direction: Название направления.
        """
        url = 'https://uni-dubna.ru/Entrance/GetGuideline'

        data = {
            'limit': 25,
            'id': direction[0]
        }

        res = requests.post(url, data).text
        about = self.__get_about(res)

        soup = BeautifulSoup(res, 'lxml')
        content = soup.find_all('div', class_='tab-pane-item')

        free_places = ''
        paid_places = ''

        if direction[1] == 'ЭКОНОМИКА':
            free_places = f"Количество бюджетных мест (бесплатных): 0"
            soup = BeautifulSoup(str(content[0]), 'lxml')
            value = soup.find('div', class_='col-sm-8').text.strip()
            paid_places = f"Количество платных мест: {value}"
        else:
            for i in [0, 1]:
                soup = BeautifulSoup(str(content[i]), 'lxml')

                value = soup.find('div', class_='col-sm-8').text.strip()
                if i == 0:
                    free_places = f"Количество бюджетных мест (бесплатных): {value}"
                elif i == 1:
                    paid_places = f"Количество платных мест: {value}"

        try:
            soup = BeautifulSoup(str(content[5]), 'lxml')
        except Exception:
            soup = BeautifulSoup(str(content[4]), 'lxml')

        value = soup.find('div', class_='col-sm-8').text.strip()
        passing_score = f"Проходной балл прошлого года: {value}"

        soup = BeautifulSoup(res, 'lxml')
        data = soup.find_all('script')
        if direction[1] == 'ЯДЕРНЫЕ ФИЗИКА И ТЕХНОЛОГИИ':
            cost = data[3]
        else:
            try:
                cost = data[2]
            except Exception:
                cost = data[1]

        cost = f"Стоимость обучения: {str(cost).split()[4][:-1]}"
        result = f'{direction[1]}:\n\n{free_places}\n{paid_places}\n{cost}р\n{passing_score}'
        result += '\n\nПрофили:\n\n'
        for item in about:
            result += item

        self.__info = result
