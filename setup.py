from setuptools import setup

setup(name='SMS_BD',
      version='0.1',
      description='Subproyecto del proyecto SMS',
      url='https://github.com/neon520/SMS-BDyReplica',
      author='neon_520',
      author_email='javierpg93@correo.ugr.es',
      license='MIT',
      packages=['SMS_BD'],
      install_requires=[
          'mysql-python',
          'jinja2',
          'webapp2',
          'Paste',
          'webob'
      ],
      zip_safe=False)
