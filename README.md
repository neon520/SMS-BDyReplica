# Subproyecto de SMS: StudentsManagementSystem

[![Build Status](https://travis-ci.org/neon520/SMS-BDyReplica.svg?branch=master)](https://travis-ci.org/neon520/SMS-BDyReplica)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://smsbdtradicional.herokuapp.com/)

[![Azure](http://www.avtex.com/~/media/base/avtex%20public/logos/windows-azure-logo.ashx?la=en)](http://smsbdyreplica.cloudapp.net/)

## Uso
Copiar el archivo [VARIABLES_ENTORNO](https://github.com/neon520/SMS-BDyReplica/blob/master/variables_entorno/VARIABLES_ENTORNO) en la raíz y rellenarlo, ya que el que doy es una plantilla, después de esto hacer

	make deploy

## Introducción

Este proyecto se ha elegido por petición por parte de algunos profesores de un sistema capaz de dar apoyo en las labores del profesorado en la etapa de enseñanza primaria, secundaria y bachillerato. Brindará soporte y agilizará las tareas de los docentes en el día a día en las aulas (pudiendose implementar gestiones de partes de incidencias de comportamiento, asistencia a clase, calificaciones, comunicación con los padres e interna entre personal del centro, etc.).

Además, dada la índole del proyecto, tenemos intención de presentarlo al Certamen de Software Libre.

## Estructura del proyecto SMS

Será un proyecto que se divide en **3 partes**:
- **La aplicación**:
De esta se encargará @juanAFernandez, que la presentará en su TFG
- **Las máquinas virtuales y el balanceador**:
De este apartado se encargará @JA-Gonz y será un subproyecto
- **La base de datos y su réplica**:
De esta parte (que será otro subproyecto) me encargo yo, @neon520.

## Infraestructura de mi parte (La base de datos y su réplica)

En mi subproyecto me encargaré de desarrollar el sistema de base de datos y de generar una réplica de la misma para evitar problemas de pérdida de datos.

Estas bases de datos estarán desarrolladas en **Mongo DB** y serán desplegadas en diferentes nubes. En concreto, la base de datos principal será desplegada en **Azure**, mientras que la réplica será desplegada en **Bluemix**. Para los despliegues utilizaré **Ansible**.


## Inicio y testeo

He realizado esta práctica en python ya que el proyecto original se está realizando en python con MySQL y webbapp2.

Los pasos que he realizado son similares a los que he ido haciendo en los ejercicios, ya que mi aplicación tiene similaridad con el ejercicio 2 ya entregado. En primer paso he realizado la aplicación con la estructura MVC.

Después he realizado los test utilizando la librería de testeo sure y ejecutándolo con nosetests (paquete "nose" de python). Una vez hecho esto he creado mi archivo .travis.yml donde configuro la conexión con travis-ci y le digo como instalar mis dependencias y como ejecutar los tests.

Poseo 2 herramientas principales de construcción debido a que, por motivos por ahora desconocidos, si utilizo un setup.py, no se me instala nosetests y no consigue ejecutar los test, así que por eso, mientras se soluciona tengo un makefile y un requirements.txt

Aquí dejo enlace al manual de instrucciones del makefile:

[Instrucciones](https://github.com/neon520/SMS-BDyReplica/blob/master/instrucciones.md)

## Despliegue en un PaaS

He realizado el despliegue en Heroku ya que permite configurar el despliegue mediante un archivo, por lo que una vez creado y preparado Heroku lo interpreta. Este archivo es el Procfile.

Me he encontrado además con varios problemas a la hora del despliegue, ya que para poder realizar este he tenido que utilizar la herramienta Gunicorn.

Con Gunicorn, me he encontrado con las siguientes tesituras:
- No puedo pasarle el archivo \_\_main\_\_ por las \_\_ y necesito que se llame así por el setup.py. Como solución he creado un archivo index.py con el mismo contenido que el ya citado.
- No puedo llamar a la aplicación dentro de main() ya que esta necesita estar en la raíz. Como solución he modificado el index.py para que funcione.

## Implementación de docker

Añadimos implementación con docker, para utilizarla debemos instalar docker, después ejecutar:
	docker build -t smsbdtradicional .
Entonces crearemos el contenedor.

Una vez creado el contenedor lo subiremos a [Dockerhub](https://hub.docker.com/). En mi caso, mi aplicación queda alojada [aquí](https://hub.docker.com/r/neon520/sms-bdyreplica/).

Para subirla primero debemos asignarle un tag (que será el ID de la imagen) de esta forma
	docker tag ID_IMAGEN LUGAR_EN_DOCKERHUB
ejemplo:
	docker tag 123124523513 neon520/sms-bdyreplica
Después de esto hacemos:
	docker push neon520/sms-bdyreplica
Una vez  para usarla solo debemos ejecutar:
	docker pull neon520/sms-bdyreplica


## Prueba en Azure
Una vez tenemos nuestra imagen podemos probarla en Azure, aunque está aún en desarrollo hemos visto que Azure presenta problemas al conectar los puertos de Docker en su salida. De todas formas podemos observar que la conexión al servidor se hace:

[Azure](smsbdtradicional-844781u2.cloudapp.net)

(Es posible que, debido a problemas financieros, esta máquina se encuentre apagada)

##Vagrant + Ansible
Añadimos módulos de vagrant y ansible para desplegar nuestras máquinas en Azure (en este caso, realmente es reutilizable a una VM local).

Para ello he desarrollado los archivos [Vagrantfile](https://github.com/neon520/SMS-BDyReplica/blob/master/Vagrantfile) y [ansible/configuracion_ansible.yml](https://github.com/neon520/SMS-BDyReplica/blob/master/ansible/configuracion_ansible.yml) que se encargarán de este depliegue.

Por una parte Vagrant se encargará de la creación de la máquina, gestionando los usuarios y puertos pertinentes.

Por otro lado, Ansible se va a encargar de preparar la máquina para ejecutar la aplicación, para ello instalará las dependencias necesarias para que este funcione.

Estos 2 programas no se ejecutan por separado, es Vagrant el que, tras crear la máquina, le dice a Ansible que proceda a hacer su trabajo.

Para ejecutar todo debemos instalar Vagrant, Ansible y, en este caso, el plugin de Azure que tiene Vagrant.

Este plugin se instala haciendo:

	vagrant plugin install vagrant-azure

Tras instalar todo, vamos a terminar de prepararlo todo para desplegar en Azure: vamos a generar los certificados de servidor (son personales y por eso no están en el repositorio).

Para realizar esta acción ejecutaremos las siguientes ordenes en el terminal:

	openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout azure.pem -out azure.pem
	openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
	chmod 600 azure.pem

Una vez hecho esto subimos nuestro archivo azure.cer a nuestro servidor (en el caso de Azure se hace en el portal antiguo en la sección de configuración).

Tras hacer esto, solo tendremos que ejecutar nuestro archivo de Variables de Entorno ([aquí](https://github.com/neon520/SMS-BDyReplica/blob/master/variables_entorno/VARIABLES_ENTORNO) dejo la plantilla) simplemente haciendo:

	./VARIABLES_ENTORNO

VARIABLES_ENTORNO debe ponerse en la raíz para que funcione, la plantilla está de ejemplo para poder copiarla a la raíz.

Tras esto ya está todo listo, ejecutaremos la orden:

	vagrant up --provider=azure

en caso de querer desplegar en azure, en caso de ser en VM local sin la etiqueta --provider.

**Nota**: instalar desde gem o buscando el .deb, ya que la versión de los repositorios de Ubuntu traen un bug. En los de archlinux no da error.

##Fabric

Fabric se encarga de conectarse por nosotros a la máquina, creada previamente, por ssh y hacer las cosas que haríamos al conectarnos. Así evitamos por ejemplo el error humano, y automatizamos mejor la gestión, ya que con una orden realizaría muchas tareas.

Para poder ver la configuración



 	fab -p tucontraseña -H  tuusuario@IPdelServidor OrdenAEjecutarPorFabric
