import sure
import webapp2
import gestorhtml

class TestStringMethods:

	def test_alumnos(self):
		request = webapp2.Request.blank('/alumnos')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Alumnos registrados' in response.body)
		(response.body).should.contain('Alumnos registrados')
		
	def test_asignaturas(self):
		request = webapp2.Request.blank('/asignaturas')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Asignaturas registradas' in response.body)
		(response.body).should.contain('Asignaturas registradas')

	def test_cursos(self):
		request = webapp2.Request.blank('/cursos')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Cursos registrados' in response.body)
		(response.body).should.contain('Cursos registrados')

	def test_grupos(self):
		request = webapp2.Request.blank('/grupos')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Grupos registrados' in response.body)
		(response.body).should.contain('Grupos registrados')

	def test_imparticiones(self):
		request = webapp2.Request.blank('/imparticiones')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Imparticiones registradas' in response.body)
		(response.body).should.contain('Imparticiones registradas')

	def test_pertenencias(self):
		request = webapp2.Request.blank('/pertenencias')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Pertenencias registradas' in response.body)
		(response.body).should.contain('Pertenencias registradas')

	def test_profesores(self):
		request = webapp2.Request.blank('/profesores')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Profesores registrados' in response.body)
		(response.body).should.contain('Profesores registrados')

	def test_registroAlumno(self):
		request = webapp2.Request.blank('/registroAlumno')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de alumno' in response.body)
		(response.body).should.contain('Registro de alumno')

	def test_registroAsignatura(self):
		request = webapp2.Request.blank('/registroAsignatura')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de asignatura' in response.body)
		(response.body).should.contain('Registro de asignatura')

	def test_registroCursa(self):
		request = webapp2.Request.blank('/registroCursa')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de cursar' in response.body)
		(response.body).should.contain('Registro de cursar')

	def test_registroGrupo(self):
		request = webapp2.Request.blank('/registroGrupo')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de grupo' in response.body)
		(response.body).should.contain('Registro de grupo')

	def test_registroImparte(self):
		request = webapp2.Request.blank('/registroImparte')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de imparticiones' in response.body)
		(response.body).should.contain('Registro de imparticiones')

	def test_registroPertenece(self):
		request = webapp2.Request.blank('/registroPertenece')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de pertenece' in response.body)
		(response.body).should.contain('Registro de pertenece')

	def test_registroProfesor(self):
		request = webapp2.Request.blank('/registroProfesor')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Registro de Profesor' in response.body)
		(response.body).should.contain('Registro de Profesor')

	def test_base(self):
		request = webapp2.Request.blank('/')
		response = request.get_response(gestorhtml.Server())
		#self.assertTrue('Students Management System' in response.body)
		(response.body).should.contain('Students Management System')

