from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://enanobrillante:ZE2ambNujhsaOwAA@cluster0.z8fcv4g.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
