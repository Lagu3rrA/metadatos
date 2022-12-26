# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from ruby_gemspec_json import *

class Test_1_ruby(unittest.TestCase):
    
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
        self.datos = ruby_gemspec_json.liderDelTrabajo()

    def test_nombre(self):
        self.assertEqual(self.datos['name'],'gitmodel') 
        
    def test_url(self):
        self.assertEqual(self.datos['url'],'http://github.com/pauldowman/gitmodel')
        
    def test_version(self):
        self.assertEqual(self.datos['version'],'0.0.8')
        
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'Paul Dowman')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'paul@pauldowman.com')
        
    def test_dependecies(self):
        self.assertEqual(self.datos['dependencies'][' activemodel'], ' ~> 3.0.1')
        self.assertEqual(self.datos['dependencies'][' activesupport'], ' ~> 3.0.1')
        self.assertEqual(self.datos['dependencies'][' dalli'], '')
        self.assertEqual(self.datos['dependencies'][' grit'], '>= 2.3.0')
        
    def test_devDependecies(self):
        self.assertEqual(self.datos['dependencies'][' ZenTest'], '>= 4.4.0')
        self.assertEqual(self.datos['dependencies'][' autotest'], '>= 4.4.1')
        self.assertEqual(self.datos['dependencies'][' rspec'], '>= 2.0.1')
        
    
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'<<-DESC.strip.gsub(/\n\s+/, " ") GitModel persists Ruby objects using Git as a data storage engine. Its an' )
        
        
if __name__ == '__main__':
    unittest.main()