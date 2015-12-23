install:
	sudo apt-get update && mysql -u $USER -p$PASS < SMS_BD/DBCreator.sql && pip install -r requirements_sql.txt

install_sin_local:
	sudo apt-get update && pip install -r requirements.txt

test:
	cd SMS_BD && nosetests test_sure.py
