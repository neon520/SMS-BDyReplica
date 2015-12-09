#! /usr/bin/python

from gestorhtml import *





def main():

    app = Server()
    ap=httpserver.serve(app, host='0.0.0.0', port='80')

if __name__ == '__main__':
    main()
