from pymongo import MongoClient

# Configuración de la conexión a MongoDB
host = "192.168.1.157"
port = 27017  # Puerto por defecto de MongoDB
base_de_datos = "biblioteca"
coleccion = "autores"

# Conectar a MongoDB
try:
    client = MongoClient(host, port)
    db = client[base_de_datos]
    print("Conexión exitosa a MongoDB")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")
    exit()

# Seleccionar la colección
collection = db[coleccion]

# Mostrar información de la colección
documentos = collection.find().limit(5)  # Obtener las primeras 5 filas
print("Información de la colección:")
for documento in documentos:
    print(documento)

# Cerrar la conexión
client.close()