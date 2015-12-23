from fabric.api import run, local, hosts, cd

#infomacion del host
def informacion_host():
    run('uname -s')
