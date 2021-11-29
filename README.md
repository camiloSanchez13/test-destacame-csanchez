# destacame_sanchez_test
Prueba técnia para Destacame

####Backend
### -----Primer Paso 

##Formas para correr el backend
El Backend puede ser instalado mediante Docke, como tambien sin el .

###Instalacion mediante Docker
Se ingresa al directorio de backend (Tener instalado Docker) \
Ejecutar los siguientes comandos en la terminal:

###Construccion de imagenes
```
$ docker-compose --env-file .local.env build
```
### Ejecutar contenedores
```
$ docker-compose --env-file .local.env up -d
```
**Url Backend:** http://localhost:7000


####Instalacion local (Manual)

### Crear ambiente virtual -- comando windows
```
$python -m venv env

```
### activar entorno

```
$ source venv/Scripts/activate
```
### Instalar requerimientos
```
$ pip install -r requirements.txt
```

### realizar migraciones
```
$ python manage.py migrate
```

### Ejecutar servidor de desarrollo
```
$ python manage.py runserver
```

####Frontend

###Instalacion Manual
```
$ yarn install
```

### Ejecutar servidor de desarrollo
```
$ yarn serve
```

**Url Frontend:** http://localhost:8080 \


**Importante!** Dependiendo de la opcion que se seleccione \
para instalar el backend, se debe cambiar la url en el front:
src-common-config
