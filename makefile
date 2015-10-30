install:
	sudo apt-get update && mysql -u root < SMS_BD/bd.sql && pip install -r requirements.txt

test:
	cd appIV && nosetests test_sure.py