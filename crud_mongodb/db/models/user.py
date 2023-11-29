#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from typing import Optional
    
class Tracks(BaseModel):
    #id: str | None
    id: Optional[str]
    Artista: str
    Cancion: str
    Genero: str
    Year: int
    Rate: int

class Pasajero(BaseModel):
    id: str | None
    Name: str
    Pclass:int
    Survived:int
    Age:str
    Ticket:str

class Pais(BaseModel):
    id: str | None
    Pais: str
    Capital:str
    Idioma: str
