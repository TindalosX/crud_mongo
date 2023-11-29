#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Invocamos la entidad que hemos creado ****nEw
from db.models.user import Tracks, Pasajero, Pais
#Importamos la instancia que devolvera al usuario en formato user ***new
from db.schemas.user import *
#Importamos nuestro cliente para poder agregar usuarios a la db****nEw
from db.Client_9 import db_client, clientTi, clientPais

from bson import ObjectId

#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

@router.get("/track/{id}")
async def track(id: str):
    #print("_id", ObjectId(id))
    return search_user("_id", ObjectId(id))

@router.get("/tracks", response_model=list[Tracks])
async def tracks():
    return allTracks_schema(db_client.tracks.find())

@router.delete("/{id}")
async def track(id: str):
    
    found = db_client.tracks.find_one_and_delete({"_id": ObjectId(id)})
    if found:
        return {"Eliminación": "Se ha eliminado el track"}

    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontro el track")
    
@router.post("/addtrack", response_model=Tracks, status_code=status.HTTP_201_CREATED)
async def track(tracks:Tracks):
    
    track_dict= dict(tracks)
    del track_dict["id"]

    id = db_client.tracks.insert_one(track_dict).inserted_id

    new_track= tracks_schema(db_client.tracks.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return Tracks(**new_track)


@router.put("/", response_model=Tracks, status_code=status.HTTP_202_ACCEPTED)
async def track( track:Tracks):

    track_dict= dict(track)
    del track_dict["id"]

    found = db_client.tracks.find_one({"_id": ObjectId(track.id)})
    print(found)
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ERROR: Track no encontrado")

    db_client.tracks.update_one({"_id": ObjectId(track.id)}, {"$set": track_dict})

    return search_user("_id", ObjectId(track.id))


def search_user(field: str, key):
    try:
        track = db_client.tracks.find_one({field: key})
        return Tracks(**tracks_schema(track))
    except:
        return {"error": "No se ha encontrado el track(id incorrecto o no registrado)"}



@router.get("/pasajeros", response_model=list[Pasajero])
async def pasajero():
    return allPasajeros_schema(clientTi.pasajeros.find())


@router.get("/pasajero/{id}")
async def pasajero(id: str):
    #print("_id", ObjectId(id))
    return search_pasajero("_id", ObjectId(id))

@router.post("/addpasajero", response_model=Pasajero, status_code=status.HTTP_201_CREATED)
async def pasajero(pasajero:Pasajero):
    
    pasajero_dict= dict(pasajero)
    del pasajero_dict["id"]

    id = clientTi.pasajeros.insert_one(pasajero_dict).inserted_id

    new_pasajero = pasajero_schema(clientTi.pasajeros.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return Pasajero(**new_pasajero)

@router.put("/updatepasajero", response_model=Pasajero, status_code=status.HTTP_202_ACCEPTED)
async def pasajero( pasajero:Pasajero):

    pasajero_dict= dict(pasajero)

    found = clientTi.pasajeros.find_one({"_id": ObjectId(pasajero_dict["id"])})

    if found is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pasajero no encontrado")

    clientTi.pasajeros.update_one({"_id": ObjectId(pasajero_dict["id"])}, {"$set": pasajero_dict})

    return search_pasajero("_id", ObjectId(pasajero.id))

@router.delete("/delpasajero/{id}")
async def pasajero(id: str):
    
    found = clientTi.pasajeros.find_one_and_delete({"_id": ObjectId(id)})
    if found:
        return {"Eliminación": "Se ha eliminado el registro del pasajero"}

    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontro al pasajero")


def search_pasajero(field: str, key):
    try:
        pasajero = clientTi.pasajeros.find_one({field: key})
        return Pasajero(**pasajero_schema(pasajero))
    except:
        return {"error": "No se ha encontrado el pasajero(id incorrecto o no registrado)"}
    

@router.get("/paises", response_model=list[Pais])
async def paises():
    return allPaises_schema(clientPais.paises.find())

@router.get("/pais/{id}")
async def pais(id: str):
    #print("_id", ObjectId(id))
    return search_pais("_id", ObjectId(id))

@router.post("/addpais", response_model=Pais, status_code=status.HTTP_201_CREATED)
async def apis(pais:Pais):
    
    pais_dict= dict(pais)
    del pais_dict["id"]

    id = clientPais.paises.insert_one(pais_dict).inserted_id

    new_pais= pais_schema(clientPais.paises.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return Pais(**new_pais)

@router.put("/updatepais", response_model=Pais, status_code=status.HTTP_202_ACCEPTED)
async def pais(pais:Pais):

    pais_dict= dict(pais)

    found = clientPais.paises.find_one({"_id": ObjectId(pais.id)})

    if found is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pais no encontrado")

    clientPais.paises.update_one({"_id": ObjectId(pais.id)}, {"$set": pais_dict})

    return search_pais("_id", ObjectId(pais.id))

@router.delete("/delpais/{id}")
async def pasajero(id: str):
    
    found = clientPais.paises.find_one_and_delete({"_id": ObjectId(id)})
    if found:
        return {"Eliminación": "Se ha eliminado el registro del pais"}

    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontro al pais")


def search_pais(field: str, key):
    try:
        pais = clientPais.paises.find_one({field: key})
        return Pais(**pais_schema(pais))
    except:
        return {"error": "No se ha encontrado el pais(id incorrecto o no registrado)"}


#tracks_schema, allTracks_schema, pasajero_schema, allPasajeros_schema

#source /home/tindalos/Code/env-py/mdw/bin/activate