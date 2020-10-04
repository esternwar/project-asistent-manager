from app.queries import bd_connect, close_connect_cursor


class Card:
    def __init__(self, __id):
        self.__id = id
        self.__title = ''
        self.__priority = 0
        self.__status = 0
        self.__type = 0
        self.__description = ''
        self.__assignee = 0
        self.__reporter = 0
        self.__workLog = 0
        self.__comments = ''

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_priority(self, priority):
        self.__priority = priority

    def get_priority(self):
        return self.__priority

    def set_description(self, desc):
        self.__description = desc

    def get_description(self):
        return self.__description

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_type(self, card_type):
        self.__type = card_type

    def get_type(self):
        return self.__type

    def set_assignee(self, assignee):
        self.__assignee = assignee

    def get_assignee(self):
        return self.__assignee

    def set_reporter(self, reporter):
        self.__reporter = reporter

    def get_reporter(self):
        return self.__reporter

    def set_workLog(self, workLog):
        self.__workLog = workLog

    def get_workLog(self):
        return self.__workLog

    def set_comments(self, comments):
        self.__comments = comments

    def get_comments(self):
        return self.__comments

    def create(self):
        try:
            conn = bd_connect()
            cursor = conn.cursore()
            cursor.execute(f"""INSERT INTO public."Card" (id, title, description, status, type, priority, assignee, reporter, workLog, comments) 
                            VALUES ({self.__id}, '{self.__title}', '{self.__description}'
                            {self.__status}, {self.__type}, {self.__priority}, {self.__assignee}
                            {self.__reporter}, {self.__workLog}, {self.__comments})""")
            conn.commit()
            close_connect_cursor(conn, cursor)
            return True
        except:
            return None

    def update(self):
        try:
            conn = bd_connect()
            cursor = conn.cursore()
            cursor.execute(f"""UPDATE public."Card" 
                            SET title='{self.__title}', description='{self.__description}', 
                            status={self.__status}, type={self.__type}, 
                            priority={self.__priority}, assignee={self.__assignee}, 
                            reporter={self.__reporter}, workLog={self.__workLog}, 
                            comments={self.__comments}
                            WHERE id={self.__id}""")
            conn.commit()
            close_connect_cursor(conn, cursor)
            return True
        except:
            return None

    def remove(self):
        try:
            conn = bd_connect()
            cursor = conn.cursore()
            cursor.execute(f"""DELETE FROM public."Card" 
                            WHERE id={self.__id}""")
            conn.commit()
            close_connect_cursor(conn, cursor)
            return True
        except:
            return None


def getCards(filters, order):
    conn = bd_connect()
    cursor = conn.cursore()
    if filters == '' & order == '':
        cursor.execute('SELECT id, title, description, status, type, priority, assignee, reporter, workLog, comments FROM public."Card"')
        dict_like_arr = []
        for row in cursor.fetchall():
            if row != []:
                new_dict = {'id': row[0], 'title': row[1], 'description': row[2], 'type': row[3], 'priority': row[4],
                            'assignee': row[5], 'reporter': row[6], 'workLog': row[7], 'comments': row[8]}
                dict_like_arr.append(new_dict)

        close_connect_cursor(conn, cursor)
        return dict_like_arr


def createCard(creation_fields):
    conn = bd_connect()
    cursor = conn.cursore()
    id = 123
    card = Card(id)
    cursor.execute('''SELECT id FROM public."Statuses"'
                   WHEN id=1''')
    origin_status = cursor.fetch()
    card.set_status(origin_status[0])
    card.set_title(creation_fields['title'])
    card.set_type(creation_fields['type'])
    card.set_assignee(creation_fields['assignee'])
    card.set_reporter(creation_fields['reporter'])
    card.set_description(creation_fields['description'])
    card.set_priority(creation_fields['priority'])

    close_connect_cursor(conn, cursor)
    return card.create()


def updateCard(fields):
    card = Card(fields['id'])
    card.set_title(fields['title'])
    card.set_type(fields['type'])
    card.set_status(fields['status'])
    card.set_assignee(fields['assignee'])
    card.set_reporter(fields['reporter'])
    card.set_comments(fields['comments'])
    card.set_description(fields['description'])
    card.set_priority(fields['priority'])
    card.set_workLog(fields['workLog'])
    return card.update()


def removeCard(id):
    prop = Card(id)
    return prop.remove()