import psycopg2

class DBManager:
    def __init__(self, db_name = 'postgres', db_user = 'postgres', db_password = '0833', db_port = '5432', db_host = 'localhost'):
        self.conn = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            port = db_port,
            host = db_host
        )

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def execute(self, query, params=None, fetch="none"):
        cursor = self.conn.cursor()
        cursor.execute(query, params)

        if fetch == "one":
            result = cursor.fetchone()
        elif fetch == "all":
            result = cursor.fetchall()
        else:
            result = None

        self.conn.commit()
        cursor.close()
        return result

    def close(self):
        self.conn.close()

def get_vlogs():
    db = DBManager()
    rows = db.execute(
            "SELECT id, title, description, created_at FROM vlogs ORDER BY created_at DESC",
            fetch="all"
        )
    db.close()
    return rows

def add_vlog(title, description):
        db = DBManager()
        db.execute(
            "INSERT INTO vlogs (title, description) VALUES (%s, %s)",
            (title, description)
        )
        db.close()

def delete_vlog(vlog_id):
    db = DBManager()
    db.execute("DELETE FROM vlogs WHERE id = %s", (vlog_id,))
    print(vlog_id)
    print("deleted")
    db.close()

def update_vlog(vlog_id, title, description):
    db = DBManager()
    db.execute("UPDATE vlogs SET title = %s, description = %s WHERE id = %s",(title, description, vlog_id))
    print(vlog_id)
    print("updated")
    db.close()

def get_vlog_by_id(vlog_id):
    db = DBManager()
    vlog =  db.execute("SELECT id, title, description, created_at FROM vlogs WHERE id = %s", (vlog_id,),fetch = "one",)

    db.close()
    return vlog
