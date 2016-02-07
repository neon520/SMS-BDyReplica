#USU=$(shell echo $$USUARIO)
#CON=$(shell echo $$CONTRASENA)

#Como estaba antes
#USUARIO=$(shell echo $$USUARIO)
#CONTRASENA=$(shell echo $$CONTRASENA)

#include VARIABLES_ENTORNO

install:
	sudo ./docker_run && mysql -u $(US) --password=$(PASS) < SMS_BD/DBCreator.sql && pip install -r requirements_sql.txt

install_sin_local:
	sudo apt-get update && pip install -r requirements.txt

travis:
	mysql -u $(USUARIO)  --password=$(CONTRASENA) < SMS_BD/DBCreator.sql && pip install -r requirements_sql.txt

test:
	cd SMS_BD && nosetests test_sure.py
