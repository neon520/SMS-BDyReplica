from fabric.api import run, local, hosts, cd

#infomacion del host
def host_info():
    run('uname -s')

#descarga de la aplicacion utilizando git
def get_app():
	run('sudo git clone https://github.com/neon520/SMS-BDyReplica.git')

#Instalacion necesaria para host virgen
def install():
	run('cd SMS-BDyReplica && make install')

def remove():
    run('sudo rm -r SMS-BDyReplica')


#Ejecucion de test
def test_app():
	run('cd SMS-BDyReplica && make test')

#Ejecucion de la aplicacion
def run_app():
    run('cd SMS-BDyReplica/SMS_BD && sudo gunicorn -b 0.0.0.0:80 index:app &')

#Peticion
def peticion():
	run('sudo curl http://0.0.0.0:80')

def kill_app():
    run('sudo kill -9 $(pidof python)')


#Ejecucion remota del docker
#Instalacion de docker y descarga de imagen
def get_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull neon520/sms-bdyreplica')

#Ejecucion de docker
def run_docker():
	run('sudo docker run -i -t neon520/sms-bdyreplica')
