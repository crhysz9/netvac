from netvac.backend.database.db_connection import connect_to_db, close_connection
import psycopg2

class Appointment:
    def __init__(self, id, date, time, customer_id, service_id, status):
        self.id = id
        self.date = date
        self.time = time
        self.customer_id = customer_id
        self.service_id = service_id
        self.status = status

    def create(self):
        conn = connect_to_db()
        cur = conn.cursor()
        query = """INSERT INTO appointments (date, time, customer_id, service_id, status)
                   VALUES (%s, %s, %s, %s, %s) RETURNING id;"""
        try:
            cur.execute(query, (self.date, self.time, self.customer_id, self.service_id, self.status))
            self.id = cur.fetchone()[0]
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error creating appointment: {e}")
            conn.rollback()
        finally:
            cur.close()
            close_connection(conn)

    @classmethod
    def get_by_id(cls, id):
        conn = connect_to_db()
        cur = conn.cursor()
        query = """SELECT id, date, time, customer_id, service_id, status
                   FROM appointments WHERE id = %s;"""
        try:
            cur.execute(query, (id,))
            row = cur.fetchone()
            if row:
                return cls(*row)
            else:
                return None
        except psycopg2.Error as e:
            print(f"Error getting appointment by ID: {e}")
            return None
        finally:
            cur.close()
            close_connection(conn)

    @classmethod
    def get_all(cls):
        conn = connect_to_db()
        cur = conn.cursor()
        query = """SELECT id, date, time, customer_id, service_id, status
                   FROM appointments;"""
        appointments = []
        try:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                appointments.append(cls(*row))
            return appointments
        except psycopg2.Error as e:
            print(f"Error getting all appointments: {e}")
            return None
        finally:
            cur.close()
            close_connection(conn)