# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from R_txt_json import *

class Test_1_r(unittest.TestCase):
    
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
        self.datos =  R_txt_json.liderDelTrabajo()

    def test_nombre(self):
        self.assertEqual(self.datos['name'],'Integrate R with RDocumentation')
    
    def test_homepage(self):
        self.assertEqual(self.datos['homepage'],'https://www.rdocumentation.org')
    
    def test_url(self):
        self.assertEqual(self.datos['url'],'https://github.com/datacamp/RDocumentation')
        
    def test_version(self):
        self.assertEqual(self.datos['version'],'0.8.3')
        
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'Ludovic Vannoorenberghe')
        self.assertEqual(self.datos['authors'][1]['name'], 'Jonathan Cornelissen')
        self.assertEqual(self.datos['authors'][2]['name'], 'Hannes Buseyne')
        self.assertEqual(self.datos['authors'][3]['name'], 'Filip Schouwenaars')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'ludovic@datacamp.com')
        self.assertEqual(self.datos['authors'][1]['email'], 'jonathan@datacamp.com')
        self.assertEqual(self.datos['authors'][3]['email'], 'filip@datacamp.com')
        
    
    def test_dependecies(self):
        self.assertEqual(self.datos['dependencies']['httr'], '>= 1.2.1')
        self.assertEqual(self.datos['dependencies']['proto'], '>= 0.3-10')
        self.assertEqual(self.datos['dependencies']['rjson'], '>= 0.2.15')
        self.assertEqual(self.datos['dependencies']['utils'], '')
        
    def test_license(self):  
         self.assertEqual(self.datos['license'], 'GPL (>= 2)') 
         
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'Wraps around the default help functionality in R. Instead of plain documentation files, documentation will show up as it does on url{www.rdocumentation.org}, a platform that shows R documentation from CRAN, GitHub and Bioconductor, together with informative stats to assess the package quality')
        
        
if __name__ == '__main__':
    unittest.main()