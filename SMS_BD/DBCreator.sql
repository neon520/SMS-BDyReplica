/**
  Fichero de creación de la base de datos de SMM--
  Uso:
    > mysql -u root -p < DBCreator.sql
  Ejecutado en el mismo directorio que este fichero.

**/

#DROP DATABASE smm;

#Creamos la base de datos.
CREATE DATABASE mdb;

USE mdb;

#Creación de la tabla Alumno
CREATE TABLE Alumno(
  dni CHAR(9),
  nombre CHAR(20),
  PRIMARY KEY (dni)
);

#Creación de la tabla Asignatura
CREATE TABLE Asignatura(
  id CHAR(9),
  nombre CHAR(20),
  PRIMARY KEY (id)
);

#Creación de la tabla Profesor
CREATE TABLE Profesor(
  dni CHAR(9),
  nombre CHAR(50),
  apellidos CHAR(50),
  municipio CHAR(50),
  provincia CHAR(50),
  domicilio CHAR(100),
  email CHAR(100),
  telefono CHAR(10),
  PRIMARY KEY(dni)
);

CREATE TABLE Grupo(
  curso CHAR(2),
  letra char(1),
  PRIMARY KEY(curso,letra)
);

CREATE TABLE Pertenece(
  curso_p CHAR(2),
  letra_p char(1),
  idAsignatura CHAR(9),
  PRIMARY KEY(curso_p,letra_p,idAsignatura),
  FOREIGN KEY (curso_p) REFERENCES Grupo(curso),
  FOREIGN KEY (letra_p) REFERENCES Grupo(letra),
  FOREIGN KEY (idAsignatura) REFERENCES Asignatura(id)
);

CREATE TABLE Imparte(
  curso_i CHAR(2),
  letra_i char(1),
  idAsignatura CHAR(20),
  dniProfesor CHAR(9),
  PRIMARY KEY(curso,letra,idAsignatura,dniProfesor),
  FOREIGN KEY (dniProfesor) REFERENCES Profesor(dni),
  FOREIGN KEY (idAsignatura) REFERENCES Pertenece(idAsignatura),
  FOREIGN KEY (curso_i) REFERENCES Pertenece(curso_p),
  FOREIGN KEY (letra_i) REFERENCES Pertenece(letra_p)
);

CREATE TABLE Cursa(
  curso_c CHAR(2),
  letra_c char(1),
  idAsignatura CHAR(20),
  dniAlumno CHAR(9),
  PRIMARY KEY(curso,letra,idAsignatura,dniAlumno),
  FOREIGN KEY (dniAlumno) REFERENCES Alumno(dni),
  FOREIGN KEY (idAsignatura) REFERENCES Pertenece(idAsignatura),
  FOREIGN KEY (curso_c) REFERENCES Pertenece(curso_p),
  FOREIGN KEY (letra_c) REFERENCES Pertenece(letra_p)
);

/**
Inserción de datos de prueba.
**/
/**
INSERT INTO Profesor VALUES('Emilio','Robot', 'xxxxxxxxZ','Albolote','Granada','C/La colmena','emilio@correo.com','600112233');
INSERT INTO Profesor VALUES('Lucia','Robertson', 'xxxxxxxxY','Pulianas','Granada','C/La mancha azul','Lucia@correo.com','500212121');

INSERT INTO Alumno VALUES('Nombre 1', 'xx');
INSERT INTO Alumno VALUES('Nombre 2', 'yy');
INSERT INTO Alumno VALUES('Nombre 3', 'zz');

INSERT INTO Asignatura VALUES ('Asig1', 'A1');
INSERT INTO Asignatura VALUES ('Asig2', 'A2');
INSERT INTO Asignatura VALUES ('Asig3', 'A3');

#El alumno con DNI xx cursa la asignatura de código A1.
INSERT INTO Cursa VALUES('xx','A1');
#El alumno con DNI yy cursa la asignatura de código A1.
INSERT INTO Cursa VALUES('yy','A1');
INSERT INTO Cursa VALUES('zz','A2');

#El profesor con DNI yy imparte la asignatura A1.
INSERT INTO Imparte VALUES('xxxxxxxxZ','A1');
#El profesor con DNI ww imparte la asignatura A2.
INSERT INTO Imparte VALUES('xxxxxxxxY','A2');
**/

/*
Si ahora quisiéramos saber a que alumnos imparte clase el profesor de nombre , ¿Cómo sería la consulta?
mysql> select Alumno.nombre  from Profesor, Imparte, Cursa, Alumno where Profesor.dni=Imparte.dniProfesor and Imparte.idAsignatura=Cursa.idAsignatura and Cursa.dniAlumno=Alumno.dni and Profesor.nombre="Prof 1";
+----------+
| nombre   |
+----------+
| Nombre 1 |
| Nombre 2 |
+----------+
2 rows in set (0,00 sec)

Para nombre="Prof 2"
Empty set (0,00 sec)

Para nombre="Profe 3"
+----------+
| nombre   |
+----------+
| Nombre 3 |
+----------+
1 row in set (0,00 sec)



*/


/**
Si intentásemos hacer: INSERT INTO Cursa VALUES('xx','A5');
nos daría un fallo referente a la clave foránea, no puede añadir que un alumno (xx) vaya
a cursar una asignatura A5 que no existe en el sistema.
**/
