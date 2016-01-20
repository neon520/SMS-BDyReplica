USUARIO=$(shell echo $$USUARIO)
CONTRASENA=$(shell echo $$CONTRASENA)

install:
	. ./VARIABLES_ENTORNO && sudo ./docker_run && mysql -u $(USUARIO) -p $(CONTRASENA) < SMS_BD/DBCreator.sql && pip install -r requirements_sql.txt

install_sin_local:
	sudo apt-get update && pip install -r requirements.txt

travis:
	. ./VARIABLES_ENTORNO && mysql -u $(USUARIO)  --password=$(CONTRASENA) < SMS_BD/DBCreator.sql && pip install -r requirements_sql.txt &&  apt-get install python-dev && apt-get install python-mysqldb 

test:
	cd SMS_BD && nosetests test_sure.py




