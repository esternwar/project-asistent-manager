from app.queries import bd_connect, close_connect_cursor


class Priority:
    def __init__(self, id=123, title='New title', order=1):
        self.__id = id
        self.__title = title
        self.__order = order

    def create(self):
        try:
            conn = bd_connect()
            cursor = conn.cursore()
            cursor.execute(f"""INSERT INTO public."Priorities" (id, title, order)
                            VALUES ({self.__id}, '{self.__title}', {self.__order})""")
            conn.commit()
            close_connect_cursor(conn, cursor)
            return True
        except:
            return None

    def update(self):
        try:
            conn = bd_connect()
            cursor = conn.cursore()
            cursor.execute(f"""UPDATE public."Priorities" 
                            SET title='{self.title}', order={self.order} 
                            WHERE id={self.id}""")
            conn.commit()
            close_connect_cursor(conn, cursor)
            return True
        except:
            return None

    def remove(self):
        try:
            conn = bd_connect()
            cursor = conn.cursore()
            cursor.execute(f"""DELETE FROM public."Priorities" 
                            WHERE id={self.id}""")
            conn.commit()
            close_connect_cursor(conn, cursor)
            return True
        except:
            return None


def getProperty():
    conn = bd_connect()
    cursor = conn.cursore()
    cursor.execute('SELECT * FROM public."Priorities"')
    dict_like_arr = []
    for row in cursor.fetchall():
        if row != []:
            dict_like_arr.append({'id': row[0], 'title': row[1], 'order': row[2]})
    close_connect_cursor(conn, cursor)

    return dict_like_arr


def createProperty(title, order):
    id = 123
    prop = Priority(id, title, order)
    return prop.create()


def updateProperty(id, title, order):
    prop = Priority(id, title, order)
    return prop.update()


def removeProperty(id):
    prop = Priority(id)
    return prop.remove()
