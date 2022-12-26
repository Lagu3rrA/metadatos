# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from python_py_json import *

class Test_1_python(unittest.TestCase):
    
    # -----------------------------------------------
    # Este test comprueba que todo este bien devuelto 
    # -----------------------------------------------


    
    # Creamos el ambiente con el archivo bueno y cosas al rededor simulando un proyecto
    def setUpClass():
      
        os.makedirs('cargo')
        os.makedirs('toml')
        os.makedirs('cargotoml') 
        
        file = open("./cargo.txt", "w")
        file.write('no')
        file.close()
        file = open("./toml.toml", "w")
        file.write('no')
        file.close()
        file = open("./rust.toml", "w")
        file.write('no')
        file.close()

    # Borramos lo que habiamos creado para que quede bonito
    def tearDownClass():


        os.rmdir("cargo")
        os.rmdir("toml")
        os.rmdir("cargotoml")
        
        os.remove("cargo.txt")
        os.remove("toml.toml")
        os.remove("rust.toml")
         
        
    # Como vamos a estar llamando todo el rato en cada uno de los test al main
    # de la clase lo hacemos aqui, a si hay menos codigo repetido    
    def setUp(self):
        self.datos =  python_py_json.liderDelTrabajo()

    def test_nombre(self):
        self.assertEqual(self.datos['name'],'Flask-Classy')
    
    def test_url(self):
        self.assertEqual(self.datos['url'],'https://github.com/apiguy/flask-classy')
        
    def test_version(self):
        self.assertEqual(self.datos['version'],'0.6.8')
        
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'Freedom Dumlao')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'freedomdumlao@gmail.com')
    
    def test_dependecies(self):
        self.assertEqual(self.datos['dependencies']['six'], '>=1.11.0')
        self.assertEqual(self.datos['dependencies']['numpy'], '')
        self.assertEqual(self.datos['dependencies']['pandas'], '')
        self.assertEqual(self.datos['dependencies']['cherrypy'], '')
        self.assertEqual(self.datos['dependencies']['jinja2'], '')
        
    def test_license(self):  
         self.assertEqual(self.datos['license'], 'BSD') 
         
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'Class based views for Flask')
        
        
if __name__ == '__main__':
    unittest.main()