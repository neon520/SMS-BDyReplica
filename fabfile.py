from fabric.api import run, local, hosts, cd

#infomacion del host
def host_info():
    run('uname -s')

#descarga de la aplicacion utilizando git
def get_app():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo git clone https://github.com/neon520/SMS-BDyReplica.git')

#Instalacion necesaria para host virgen
def install():
	run('cd SMS_BD/ && make install')


#Ejecucion de test
def test_app():
	run('cd SMS_BD/ && make test')

#Ejecucion de la aplicacion
def run_app():
	run('cd SMS_BD/ && python __main__.py')

#Peticion
def peticion():
	run('curl http://localhost:80/')



#Ejecucion remota del docker
#Instalacion de docker y descarga de imagen
def get_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull neon520/sms-bdyreplica')

#Ejecucion de docker
def run_docker():
	run('sudo docker run -i -t neon520/sms-bdyreplica')
