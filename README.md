# IA Interactive 

- API Rest Desarrollada en FastAPI 
- Un Buen Ejercicio de backend con Python y el Framework FastAPI
- Proyect Academy Magic
- author: Charles Benitez
- email: charlesjbenitez1993@gmail.com


![FastApi](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

**Intrucciones de instalacion**

1. Clonar el repositorio 
    ```
    git clone https://github.com/charlesbenitez16/academy_magic.git
    
    ```

2. Instalar dependecias con virtualenv
    - paso 2.1 crear el entorno virtual
    ```
    python -m virtualenv venv
    ```
    - paso 2.2 activar el entorno virtual
    ```
    source venv/bin/activate
    ```
    
    
    - paso 2.3 actualizar el gestionador de paquetes pip
    ```
    pip install --upgrade pip
    ```
    - paso 2.4 instalar dependecias
    
    ```
    pip install -r requirements.txt
    ```

3. Crear una base de datos y utilizar un .env 
    ```
    mysql+pymysql://<user>:<password>@<host>:<port>/<bd_name>
    ```
    
    **crea un .env para manejar las variables de la BD requeridas**
    user = "charles"
    password = "cjbb1234"
    host = "localhost"
    port = 3306
    bd_name = "academy_magic"


**Ejecucion del proyecto**

1. Activar el servidor local
    ```
    uvicorn main:app --reload
    ```

2. Acceder al swagger u redoc de FastAPI Para probar los endpoints
    - http://127.0.0.1:8000/docs  --> swagger
    - http://127.0.0.1:8000/redoc ---> redoc 


**Endpoints del proyecto**

# 1. /api/solicitud 
    METHOD: POST
    Params: dict -> 
    {  
        "id": "string",
        "first_name": "string",
        "last_name": "string",
        "age": int,
        "magic_affinity": "string"
    }
![swagger FastApi](./docs/create_endpoint.png)

# 2 /api/get_only_user
    METHOD: GET
    Params: id -> string
    id es un identificador para mostrar la informacion de un registro

![swagger FastApi](./docs/get_id.png)

# 3 /api/get_users
    METHOD: GET
    Params: empty
    Muestra todos los registros insertados en la BD

![swagger FastApi](./docs/get_all.png) 


# 4 /api/get_grimorio
    METHOD: GET
    Params: id -> string
    Utiliza el id de un registro para mostrar el grimorio del usuario

![swagger FastApi](./docs/grimorio.png) 

# 5. /api/update
    METHOD: PUT
    params : dict -> 
    {
        "id": "string",
        "first_name": "string",
        "last_name": "string",
        "age": 0,
        "magic_affinity": "string"
    }
    Recibe un diccionario con los campos obligatorios para poder actualizar
![swagger FastApi](./docs/update_register.png) 
![swagger FastApi](./docs/response_update.png)

# 6 /api/status
    METHOD: PUT
    Params: id -> string
    Utiliza el id de un registro para actualizar el status de solicitud

![swagger FastApi](./docs/update_status.png) 


# 6 /api/delete_student
    METHOD: DELETE
    Params: id -> string
    Utiliza el id de un registro para eliminarlo de la BD

![swagger FastApi](./docs/delete.png)


# **Uso de Interfaz web**

- En la siguiente rama puedes tener una version con una interfaz sencilla.
- https://github.com/charlesbenitez16/academy_magic/tree/feature/interfaz-web

Para ser utilizada solo debe descargar y descomprimir el documento

# **Nota:** Repetir los paso 2 y 3 para poder tener todas las dependencias de las instrucciones

**Ejecucion de la interfaz**

1. Activar el servidor local
    ```
    uvicorn main:app --reload
    ```

2. Ir a tu navegador y colocar el siguiente link   

    - http://127.0.0.1:8000/inicio


**Vistas**
1. Inicio
![swagger FastApi](./docs/interfaz.png)

2. Agregar solicitud
![swagger FastApi](./docs/add_solicitud.png)

3. Ver todas las solicitudes
    - en esta vista podemos eliminar un registro o actualizar su status
![swagger FastApi](./docs/all_solicitudes.png)

4. Actualizar solicitud
![swagger FastApi](./docs/update.png)
