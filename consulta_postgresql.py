import psycopg2
from psycopg2 import sql

# Configuración de la conexión a la base de datos
dbname = "biblioteca"
user = "admin"
password = "admin"
host = "192.168.1.156"
port = "5432"  # Puerto por defecto de PostgreSQL

# Conectar a la base de datos
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print("Conexión exitosa")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    exit()

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Consulta para obtener información de la tabla "libros"
consulta = sql.SQL("SELECT * FROM libros LIMIT 5")

# Ejecutar la consulta
try:
    cursor.execute(consulta)
    filas = cursor.fetchall()
    print("Información de la tabla libros:")
    for fila in filas:
        print(fila)
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
