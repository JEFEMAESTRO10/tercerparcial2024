import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autocnocimiento creada")
    conn.commit()   
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()

def insertRow(experience_id, experience_type, start_date, end_date, budget=None, status="scheduled"):
    conn = sql.connect("autoconocimientoKevin.db")
    cursor = conn.cursor()
    query = """
    INSERT INTO experience_planning (experience_id, experience_type, start_date, end_date, budget, status)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    try:
        cursor.execute(query, (experience_id, experience_type, start_date, end_date, budget, status))
        conn.commit()
        print("Datos insertados correctamente")
    except sql.Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        conn.close()

def readRow():
    try:
        conn = sql.connect("autoconocimientoKevin.db")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM experience_planning;
        """)
        rows = cursor.fetchall()
        if rows:
            print("Registros en la tabla experience_planning:")
            for row in rows:
                print(row)
        else:
            print("No hay registros en la tabla experience_planning.")
    except sql.Error as e:
        print(f"Error al leer los registros: {e}")
    
    finally:
        conn.close()


if __name__ == "__main__":
    createDB()
    createTable()
