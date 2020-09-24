import app.queries
import psycopg2
import psycopg2.extras

cursor = app.queries.cursor
conn = app.queries.conn


class Priority:
    def __init__(self, id=123, title='New title', order=1):
        self.id = id
        self.title = title


    def create(self):
        try:
            cursor.execute(f"""INSERT INTO public."Priorities" (id, title, order)
                            VALUES ({self.id}, '{self.title}', {self.title})""")
            conn.commit()
            return True
        except:
            return None

    def update(self):
        try:
            cursor.execute(f"""UPDATE public."Priorities" 
                            SET title='{self.title}', order={self.order} 
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
           dict_like_arr.append({'id': row[0], 'title': row[1], 'order': row[2]})

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
