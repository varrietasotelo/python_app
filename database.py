from pymongo import MongoClient
import certifi

MONGO_URL = 'mongodb+srv://root:admin@cluster0.3snpphc.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try: 
        client = MongoClient.connect(MONGO_URL, tlsCAFILE=ca)
        db = client["COVID_DB"]
    except ConnectionError:
        print('Error de conexion')
    return db 