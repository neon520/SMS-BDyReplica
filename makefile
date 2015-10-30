install:
	sudo apt-get update && mysql -u root < SMS_BD/bd.sql && pip install -r requirements.txt

test:
	cd SMS_BD && nosetests test_sure.py