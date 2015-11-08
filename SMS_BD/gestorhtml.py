from paste.urlparser import StaticURLParser
from paste.cascade import Cascade
from paste import httpserver
import mimetypes
import datetime
import jinja2
import os
import webapp2
import cgi

from gestorbd import *
from paste import httpserver



STATIC_DIR = os.sep + 'tostatic' + os.path.abspath(os.path.dirname(__file__)) + os.sep + 'static'


template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))


def validaTexto(texto):
    if len(texto)>0:
        return True
    else:
        return False


class StaticView(webapp2.RequestHandler):
    def get(self, path):
        path = os.sep + path
        try:
            f = open(path, 'r')
            self.response.headers.add_header('Content-Type', mimetypes.guess_type(path)[0])
            self.response.out.write(f.read())
            f.close()
        except Exception, e:
            print 'Problem in StaticView:', e
            self.response.set_status(404)

class Alumno(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorAlumno.getAlumnos()

        templateVars = {"alumnos" : resultados}

        template = template_env.get_template('templates/alumnos.html')
        #Cargamos la plantilla y le pasamos los datos cargados
        self.response.out.write(template.render(templateVars))

class Asignatura(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorAsignatura.getAsignaturas()

        templateVars = {"asignaturas" : resultados}

        template = template_env.get_template('templates/asignaturas.html')
        #Cargamos la plantilla y le pasamos los datos cargados
        self.response.out.write(template.render(templateVars))

class Profesor(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorProfesor.getProfesores()

        templateVars = {"profesores" : resultados}

        template = template_env.get_template('templates/profesores.html')
        #Cargamos la plantilla y le pasamos los datos cargados        
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.out.write(template.render(templateVars))



class Grupo(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorGrupo.getGrupos()

        templateVars = {"grupos" : resultados}

        template = template_env.get_template('templates/grupos.html')
        #Cargamos la plantilla y le pasamos los datos cargados        
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.out.write(template.render(templateVars))



class Pertenece(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorPertenece.getPertenencias()

        templateVars = {"pertenencias" : resultados}

        template = template_env.get_template('templates/pertenencias.html')
        #Cargamos la plantilla y le pasamos los datos cargados        
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.out.write(template.render(templateVars))


class Imparte(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorImparte.getImparticiones()

        templateVars = {"imparticiones" : resultados}

        template = template_env.get_template('templates/imparticiones.html')
        #Cargamos la plantilla y le pasamos los datos cargados        
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.out.write(template.render(templateVars))



class Cursa(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorCursa.getCursos()

        templateVars = {"cursos" : resultados}

        template = template_env.get_template('templates/cursos.html')
        #Cargamos la plantilla y le pasamos los datos cargados        
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.out.write(template.render(templateVars))






class WebAlumno(webapp2.RequestHandler):
    
    '''
    def get(self):
        template=template_env.get_template('templates/registroUsuario.html')
        self.response.out.write(template.render())
    '''
    
    def get(self):
        template=template_env.get_template('templates/registroAlumno.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))
    '''
    def post(self):


        nombreUsuario = validaTexto(self.request.get('nombre'))
        dniUsuario = validaTexto(self.request.get('dni'))

        if not(nombreUsuario and dniUsuario):
            template=template_env.get_template('templates/registroUsuario.html')
            self.response.out.write(template.render())
        else:
            #Grabamos los datos en la base de datos.
            user.nuevoUsuario(self.request.get('nombre'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')
    '''
    def post(self):
        nombreAlumno=validaTexto(self.request.get('nombre'))
        dni=validaTexto(self.request.get('nombre'))

        if not (nombrealumno and dni):
            self.get(self)
        else:
            GestorAlumno.nuevoAlumno(str(dni), self.request.get('nombre'))

            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')

class WebAsignatura(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroAsignatura.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        nombreAsignatura = validaTexto(self.request.get('nombre'))
        idAsignatura = validaTexto(self.request.get('id'))

        if not(nombreAsignatura and idAsignatura):
            self.get(self)
        else:
            #Grabamos los datos en la base de datos.
            GestorAsignatura.nuevaAsignatura(int(self.request.get('id')),self.request.get('nombre'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')


class WebProfesor(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroProfesor.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        nombre = validaTexto(self.request.get('nombre'))
        dni = validaTexto(self.request.get('dni'))
        apellidos = validaTexto(self.request.get('apellidos'))
        municipio = validaTexto(self.request.get('municipio'))
        provincia = validaTexto(self.request.get('provincia'))
        domicilio = validaTexto(self.request.get('domicilio'))
        email = validaTexto(self.request.get('email'))
        tfo = validaTexto(self.request.get('telefono'))

        if not(nombre and dni and apellidos and municipio and provincia and domicilio and email and tfo):
            self.get(self)
        else:
            #Grabamos los datos en la base de datos.
            GestorProfesor.nuevoProfesor(int(self.request.get('dni')),self.request.get('nombre'),self.request.get('apellidos'),self.request.get('municipio'),self.request.get('provincia'),self.request.get('domicilio'),self.request.get('email'),self.request.get('telefono'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')


class WebGrupo(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroGrupo.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        curso = validaTexto(self.request.get('curso'))
        letra = validaTexto(self.request.get('letra'))

        if not(curso and letra):
            self.get(self)
        else:
            #Grabamos los datos en la base de datos.
            GestorGrupo.nuevGrupo(self.request.get('curso'),self.request.get('letra')) #, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('curso'))
            self.response.out.write('</pre></body></html>')

class WebPertenece(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroPertenece.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        curso = validaTexto(self.request.get('curso'))
        letra = validaTexto(self.request.get('letra'))
        idAsignatura = validaTexto(self.request.get('idAsignatura'))

        if not(curso and letra and idAsignatura):
            self.get(self)
        else:
            #Grabamos los datos en la base de datos.
            GestorPertenece.nuevaPertenencia(self.request.get('curso'),self.request.get('idAsignatura'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('curso'))
            self.response.out.write('</pre></body></html>')


class WebImparte(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroImparte.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        curso = validaTexto(self.request.get('curso'))
        letra = validaTexto(self.request.get('letra'))
        idAsignatura = validaTexto(self.request.get('idAsignatura'))
        dniProfesor = validaTexto(self.request.get('dniProfesor'))


        if not(curso and letra and idAsignatura and dniProfesor):
            self.get(self)
        else:
            #Grabamos los datos en la base de datos.
            GestorImparte.nuevaImparticion(self.request.get('curso'),self.request.get('letra'),self.request.get('idAsignatura'),self.request.get('dniProfesor'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('curso'))
            self.response.out.write('</pre></body></html>')

class WebCursa(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroCursa.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        curso = validaTexto(self.request.get('curso'))
        letra = validaTexto(self.request.get('letra'))
        idAsignatura = validaTexto(self.request.get('idAsignatura'))
        dniAlumno = validaTexto(self.request.get('dniAlumno'))


        if not(curso and letra and idAsignatura and dniAlumno):
            self.get(self)
        else:
            #Grabamos los datos en la base de datos.
            GestorImparte.nuevaImparticion(self.request.get('curso'),self.request.get('idAsignatura'),self.request.get('dniAlumno'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('curso'))
            self.response.out.write('</pre></body></html>')


'''
class WebBorrarCali(webapp2.RequestHandler):
    def get(self):
        template=template_env.get_template('templates/borrarCalificacion.html')
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))

    def post(self):

        nombreUsuario=validaTexto(self.request.get('nombre'))
        idEmpresa=validaTexto(self.request.get('id'))

        if not(nombreUsuario and idEmpresa):
            template=template_env.get_template('templates/borrarCalificacion.html')
            self.response.out.write(template.render())
        else:
            GestorCalificar.borrarCali(self.request.get('nombre'),int(self.request.get('id')))

            self.response.out.write('<html><body>Calificacion anulada</body></html>')
'''
'''
ge=GestorEmpresa()
gc=GestorCalificar()

ge.nuevaEmpresa(80,"Cali")
gc.nuevaCali("Pepe",80,8)
gc.borrarCali("Pepe",80)

'''

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/base.html')
        '''
        user = self.session.get('user')
        template_values = {
            'user': user
            }
        '''
        template_values = {'STATIC_DIR': STATIC_DIR }
        self.response.write(template.render(template_values))



def Server() :
    app=webapp2.WSGIApplication([('/', MainPage),
                                      ('/registroAlumno', WebAlumno),
                                      ('/registroAsignatura', WebAsignatura),
                                      ('/registroProfesor', WebProfesor),
                                      ('/registroGrupo', WebGrupo),
                                      ('/registroPertenece', WebPertenece),
                                      ('/registroImparte', WebImparte),
                                      ('/registroCursa', WebCursa),
                                      ('/alumnos', Alumno),
                                      ('/asignaturas', Asignatura),
                                      ('/profesores', Profesor),
                                      ('/grupos', Grupo),
                                      ('/pertenencias', Pertenece),
                                      ('/imparticiones', Imparte),
                                      ('/cursos', Cursa),
                                      (r'/tostatic/(.+)', StaticView)],debug=True)
    return httpserver.serve(app, host='127.0.0.1', port='8000')