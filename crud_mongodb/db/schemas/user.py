def tracks_schema(tracks):
    return{
        "id": str(tracks["_id"]),
        "Artista": tracks["Artista"],
        "Cancion": tracks["Cancion"],
        "Genero": tracks["Genero"],
        "Year": tracks["Year"],
        "Rate": tracks["Rate"]
    }

def allTracks_schema(tracks) -> list:
    return [tracks_schema(track) for track in tracks]

    
def pasajero_schema(pasajero):
    return{
        "id": str(pasajero["_id"]),
        "Name": pasajero["Name"],
        "Pclass": pasajero["Pclass"],
        "Survived": pasajero["Survived"],
        "Age": pasajero["Age"],
        "Ticket": pasajero["Ticket"]
    }

def allPasajeros_schema(pasajeros) -> list:
    return [pasajero_schema(pasajero) for pasajero in pasajeros]


def pais_schema(pais):
    return{
        "id": str(pais["_id"]),
        "Pais": pais["Pais"],
        "Capital": pais["Capital"],
        "Idioma": pais["Idioma"],
    }

def allPaises_schema(paises) -> list:
    return [pais_schema(pais) for pais in paises]