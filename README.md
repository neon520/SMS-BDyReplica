# Subproyecto de SMS: StudentsManagementSystem
![travis](https://travis-ci.org/neon520/SMS-BDyReplica.svg?branch=master)
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

