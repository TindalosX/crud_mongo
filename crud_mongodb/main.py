#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException, status
#Importamos de la carpeta: "routers" el código o las clases: "routers_5" y "routers2_5"
#from routers import routers_5, routers2_5, router_DB_10

import router_DB_10

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Creamos un router a partir de la clase routers_5
#app.include_router(routers_5.router)
#Creamos un router a partir de la clase routers2_5
#app.include_router(routers2_5.router)
#Creamos un router a partir de la clase router_DB_10
app.include_router(router_DB_10.router)




#source /home/tindalos/Code/env-py/mdw/bin/activate