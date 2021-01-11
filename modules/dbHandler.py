from os import path, mkdir
import sqlite3

from modules.parser import Parser


class DataBaseHandler:
    __db = None
    __cursor = None

    def __init__(self):
        self.__parser = Parser()
        self.__prepare_db()

    def __processing_db(self):
        self.__db = sqlite3.connect('db/mainDB.db')
        self.__cursor = self.__db.cursor()

        self.__create_tables()
        self.__fill()
        self.__db.close()

    def __prepare_db(self):
        if not path.exists('db/'):
            mkdir('db/')

            self.__processing_db()
        else:
            if not path.exists('db/mainDB.db'):
                self.__processing_db()

    def __create_tables(self):
        self.__db = sqlite3.connect('db/mainDB.db')
        self.__cursor = self.__db.cursor()

        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS exams (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text
            )
        """)

        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS directions (
                id integer PRIMARY KEY AUTOINCREMENT,
                exam_name text,
                direction_id text,
                name text,
                info text
            )
        """)

        self.__db.commit()
        self.__db.close()

    def __fill(self):
        self.__parser.load()

        exams = self.__parser.get_exams()

        self.__db = sqlite3.connect('db/mainDB.db')
        self.__cursor = self.__db.cursor()

        for exam in exams:
            self.__cursor.execute(f"""
                INSERT INTO exams (name) VALUES ('{exam}')          
            """)

        exams = exams[1:]  # Отсекается первый элемент списка, т.к. далее уже будет не нужен

        for i in range(len(exams)):
            directions = self.__parser.get_directions(exams[i])

            for direction in directions:
                info = self.__parser.get_info(direction)

                self.__cursor.execute(f"""
                    INSERT INTO directions (exam_name, direction_id, name, info)
                    VALUES ('{exams[i]}', '{direction[0]}', '{direction[1]}', '{info}')
                """)

        self.__db.commit()
        self.__db.close()

    @staticmethod
    def decode_data(data):
        result = []

        for item in data:
            result.append(item[0])

        return result

    @staticmethod
    def execute(request):
        db = sqlite3.connect('db/mainDB.db')
        cursor = db.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        db.close()
        return data

    def repair(self):
        self.__create_tables()

        self.execute('DELETE FROM exams')
        self.execute('DELETE FROM directions')

        self.__fill()

    def get_exams(self):
        data = self.execute("""
            SELECT name FROM exams
        """)

        return self.decode_data(data)

    def get_directions(self, exam):
        if exam == 'Все':
            data = self.execute(f"""
                SELECT name FROM directions
            """)
        else:
            data = self.execute(f"""
                SELECT name FROM directions WHERE exam_name = '{exam}'
            """)

        return self.decode_data(data)

    def get_info(self, direction):
        data = self.execute(f"""
            SELECT info FROM directions WHERE name = '{direction}'
        """)

        return self.decode_data(data)
