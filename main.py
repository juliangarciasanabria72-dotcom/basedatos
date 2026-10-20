from fastapi import FastAPI, HTTPException #FastAPI = freomwork
from database import leer_base_datos, obtener_producto

appiRest = FastAPI(
    title="API inventarios SENA",
    description="Mi primera API asincrona",
    version="1.0.0"
)

#end points= direccion donde se recibe las peticiones+
#Peticiones= solicitar el procesamiento de un metodo
#metodo=get,POST,Put,Delete

@appiRest.get("/") # Decorador -> Funcion que recibe como parametro otra funcion
async def ruta_principal():
    return{"mensaje":"Bienvenido a mi primera API Rest"}

@appiRest.get("/estado")
async def estado_servidor():
    return{"status":"En linea","Servicios":"operativos Sin ningun inconveniente"}

@appiRest.get("/suma")
async def valor_suma(num1:int,num2:int):
    resultado = num1+num2
    return{"suma": resultado}


@appiRest.get("/prodocutos")
async def listar_productos():
    datos = await leer_base_datos()
    return{"cantidad":len(datos), "productos":datos}

@appiRest.get("/productos/{codigo_producto}")
async def buscar_un_producto(codigo_producto:str):
    try:
        producto = await obtener_producto(codigo_producto)
        return producto
    except KeyError:
        raise HTTPException(status_code=404, detail="El producto solicitao no esxiste en la BD")


