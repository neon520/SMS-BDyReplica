import unittest
import webapp2
import gestorhtml

class TestStringMethods(unittest.TestCase):
        def test_alumnos(self):
            request = webapp2.Request.blank('/alumnos')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Alumnos registrados' in response.body)
'''
        def test_borrarCalificacion(self):
            request = webapp2.Request.blank('/borrarCalificacion')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Borrado de una Calific' in response.body)
'''
        def test_asignaturas(self):
            request = webapp2.Request.blank('/asignaturas')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Asignaturas registradas' in response.body)

        def test_cursos(self):
            request = webapp2.Request.blank('/cursos')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Cursos registrados' in response.body)

        def test_grupos(self):
            request = webapp2.Request.blank('/grupos')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Grupos registrados' in response.body)

        def test_imparticiones(self):
            request = webapp2.Request.blank('/imparticiones')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Imparticiones registradas' in response.body)

        def test_pertenencias(self):
            request = webapp2.Request.blank('/pertenencias')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Pertenencias registradas' in response.body)

        def test_profesores(self):
            request = webapp2.Request.blank('/profesores')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Profesores registrados' in response.body)

        def test_registroAlumno(self):
            request = webapp2.Request.blank('/registroAlumno')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de alumno' in response.body)

        def test_registroAsignatura(self):
            request = webapp2.Request.blank('/registroAsignatura')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de asignatura' in response.body)

        def test_registroCursa(self):
            request = webapp2.Request.blank('/registroCursa')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de cursar' in response.body)

        def test_registroGrupo(self):
            request = webapp2.Request.blank('/registroGrupo')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de grupo' in response.body)

        def test_registroImparte(self):
            request = webapp2.Request.blank('/registroImparte')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de imparticiones' in response.body)

        def test_registroPertenece(self):
            request = webapp2.Request.blank('/registroPertenece')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de pertenencia' in response.body)

        def test_registroProfesor(self):
            request = webapp2.Request.blank('/registroProfesor')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Registro de Profesor' in response.body)

        def test_base(self):
            request = webapp2.Request.blank('/')
            response = request.get_response(gestorhtml.Server())
            self.assertTrue('Students Management System' in response.body)

if __name__ == '__main__':
    unittest.main()