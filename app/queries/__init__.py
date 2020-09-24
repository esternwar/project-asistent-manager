import psycopg2
from app.constants import dbname, user, password, host, port

conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host, port=port)
cursor = conn.cursor()


# cursor.execute("""INSERT INTO public."Priorities" (id, title)
#                VALUES (1, 'low')""")
# conn.commit()

# cursor.execute('SELECT * FROM public."Priorities"')
# records = cursor.fetchall()



#conn.close()
