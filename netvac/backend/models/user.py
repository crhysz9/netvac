from netvac.backend.database.db_connection import connect_to_db, close_connection
import psycopg2

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        close_connection(conn)
        if user_data:
            return cls(*user_data)
        return None

    @classmethod
    def create(cls, username, email, password):
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id"
        try:
            cursor.execute(query, (username, email, password))
            conn.commit()
            user_id = cursor.fetchone()[0]
            user = cls(user_id, username, email, password)
            close_connection(conn)
            return user
        except psycopg2.Error as e:
            print(f"Error creating user: {e}")
            conn.rollback()
            close_connection(conn)
            return None

    def __repr__(self):
        return f"<User {self.username}>"