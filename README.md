# Subproyecto de SMS: StudentsManagementSystem

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


## Segunda práctica

He realizado esta práctica en python ya que el proyecto original se está realizando en python con MySQL y webbapp2.

Los pasos que he realizado son similares a los que he ido haciendo en los ejercicios, ya que mi aplicación tiene similaridad con el ejercicio 2 ya entregado. En primer paso he realizado la aplicación con la estructura MVC. 

Después he realizado los test utilizando la librería de testeo sure y ejecutándolo con nosetests (paquete "nose" de python). Una vez hecho esto he creado mi archivo .travis.yml donde configuro la conexión con travis-ci y le digo como instalar mis dependencias y como ejecutar los tests.

Aquí dejo enlace al manual de instrucciones del makefile:

[Instrucciones](https://github.com/neon520/SMS-BDyReplica/blob/master/instrucciones.md)
