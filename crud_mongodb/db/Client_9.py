#Este fichero será encargado de gestionar la conexión de nuestra base de datos con Mongo DB

from pymongo import MongoClient

#Levantamos el server Uvicorn
#-uvicorn main:app --reload-

#Instancia de tipo MongoClient (si no se le asignan argumentos se conecta al localhost por default)
#Base de datos local
#db_client= MongoClient()


#Base de datos remota
#db_client= MongoClient("mongodb+srv://test1:test1@mdw.coahofk.mongodb.net/?retryWrites=true&w=majority").test1

db_client= MongoClient("mongodb+srv://victormrz0101:tindalosdb@mdw.jtzqdgx.mongodb.net/?retryWrites=true&w=majority").DB_Tracks

clientTi= MongoClient("mongodb+srv://victormrz0101:tindalosdb@mdw.jtzqdgx.mongodb.net/?retryWrites=true&w=majority").Titanic

clientPais= MongoClient("mongodb+srv://victormrz0101:tindalosdb@mdw.jtzqdgx.mongodb.net/?retryWrites=true&w=majority").Paises