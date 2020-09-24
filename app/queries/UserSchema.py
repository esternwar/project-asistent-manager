from app.queries import conn, cursor

class User:
    def __init__(self, id):
        self.id = id