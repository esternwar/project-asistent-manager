import app.queries
import psycopg2
import psycopg2.extras

cursor = app.queries.cursor
conn = app.queries.conn


class Priority:
    def __init__(self, id=123, title='New title'):
        self.id = id
        self.title = title


    def create(self):
        try:
            cursor.execute(f"""INSERT INTO public."Priorities" (id, title)
                            VALUES ({self.id}, '{self.title}')""")
            conn.commit()
            return True
        except:
            return None

    def update(self):
        try:
            cursor.execute(f"""UPDATE public."Priorities" 
                            SET title='{self.title}' 
                            WHERE id={self.id}""")
            conn.commit()
            return True
        except:
            return None

    def remove(self):
        try:
            cursor.execute(f"""DELETE FROM public."Priorities" 
                            WHERE id={self.id}""")
            conn.commit()
            return True
        except:
            return None


def getProperty():
    cursor.execute('SELECT * FROM public."Priorities"')
    dict_like_arr = []
    for row in cursor.fetchall():
        if row != []:
           dict_like_arr.append({'id': row[0], 'title': row[1]})

    return dict_like_arr


def createProperty(title):
    id = 123
    prop = Priority(id, title)
    return prop.create()


def updateProperty(id, title):
    prop = Priority(id, title)
    return prop.update()


def removeProperty(id):
    prop = Priority(id)
    return prop.remove()
