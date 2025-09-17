from netvac.backend.database.db_connection import connect_to_db, close_connection
import psycopg2

class Inventory:
    def __init__(self, item_id, item_name, quantity, unit_price):
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price

    def add_item(self):
        conn = connect_to_db()
        cur = conn.cursor()
        query = "INSERT INTO inventory (item_id, item_name, quantity, unit_price) VALUES (%s, %s, %s, %s)"
        values = (self.item_id, self.item_name, self.quantity, self.unit_price)
        try:
            cur.execute(query, values)
            conn.commit()
            print("Item added successfully!")
        except psycopg2.Error as e:
            print(f"Error adding item: {e}")
            conn.rollback()
        finally:
            close_connection(conn)


    def update_item(self, new_quantity, new_unit_price):
        conn = connect_to_db()
        cur = conn.cursor()
        query = "UPDATE inventory SET quantity = %s, unit_price = %s WHERE item_id = %s"
        values = (new_quantity, new_unit_price, self.item_id)
        try:
            cur.execute(query, values)
            conn.commit()
            print("Item updated successfully!")
        except psycopg2.Error as e:
            print(f"Error updating item: {e}")
            conn.rollback()
        finally:
            close_connection(conn)

    def delete_item(self):
        conn = connect_to_db()
        cur = conn.cursor()
        query = "DELETE FROM inventory WHERE item_id = %s"
        values = (self.item_id,)
        try:
            cur.execute(query, values)
            conn.commit()
            print("Item deleted successfully!")
        except psycopg2.Error as e:
            print(f"Error deleting item: {e}")
            conn.rollback()
        finally:
            close_connection(conn)

    @classmethod
    def get_item(cls, item_id):
        conn = connect_to_db()
        cur = conn.cursor()
        query = "SELECT * FROM inventory WHERE item_id = %s"
        values = (item_id,)
        try:
            cur.execute(query, values)
            result = cur.fetchone()
            if result:
                return cls(result[0], result[1], result[2], result[3])
            else:
                return None
        except psycopg2.Error as e:
            print(f"Error getting item: {e}")
            return None
        finally:
            close_connection(conn)