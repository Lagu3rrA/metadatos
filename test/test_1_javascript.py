# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from javascript_json_json import *

class Test_1_javascript(unittest.TestCase):
    
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
        self.datos =  javascript_json_json.liderDelTrabajo()

    def test_nombre(self):
        self.assertEqual(self.datos['name'],'react-native-youtube-iframe')
    
    def test_homepage(self):
        self.assertEqual(self.datos['homepage'],'https://lonelycpp.github.io/react-native-youtube-iframe/')
    
    def test_url(self):
        self.assertEqual(self.datos['url'],'https://github.com/LonelyCpp/react-native-youtube-iframe.git')
        
    def test_version(self):
        self.assertEqual(self.datos['version'],'2.2.2')
        
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'Ananthu P Kanive ')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'antu@yes.com')
        
    def test_dependecies(self):
        self.assertEqual(self.datos['dependencies']['events'], '^3.2.0')
        
    def test_devdependecies(self):
        self.assertEqual(self.datos['dev-dependencies']['@babel/cli'], '^7.2.3')
        self.assertEqual(self.datos['dev-dependencies']['@babel/core'], '^7.2.2')
        self.assertEqual(self.datos['dev-dependencies']['@react-native-community/eslint-config'], '^2.0.0')
        self.assertEqual(self.datos['dev-dependencies']['eslint'], '^7.7.0')
        
    def test_keywords(self):  
         self.assertEqual(self.datos['keywords'][0], 'react-native') 
         self.assertEqual(self.datos['keywords'][1], 'react-component') 
         self.assertEqual(self.datos['keywords'][2], 'react-native-component') 
         self.assertEqual(self.datos['keywords'][3], 'react') 
         self.assertEqual(self.datos['keywords'][3], 'react native') 
         self.assertEqual(self.datos['keywords'][3], 'mobile') 
    
    def test_license(self):  
         self.assertEqual(self.datos['license'], 'MIT') 
         
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'A simple wrapper around the youtube iframe js API for react native')
        
        
if __name__ == '__main__':
    unittest.main()