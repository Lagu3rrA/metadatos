# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from css_json_json import *

class Test_1_Php(unittest.TestCase):
    
    # -----------------------------------------------
    # Este test comprueba que todo este bien devuelto 
    # -----------------------------------------------
    
    
    # Creamos el ambiente con el archivo bueno y cosas al rededor simulando un proyecto
    def setUpClass():
       
        os.makedirs('bower')
        os.makedirs('package')
        os.makedirs('json')
        os.makedirs('bowerjson')
        os.makedirs('packagejson')
        
        file = open("./package.json", "w") # ESTE ES EL BUENO package.json
        file.write('{"name": "alarm","version": "1.0.0","description": "Alarm clock project during week1 day2 JS at Epicodus.","main": "gulpfile.js","scripts": {"test": "echo \"Error: no test specified\" && exit 1"},"author": "","license": "ISC","devDependencies": {"gulp": "^3.9.1","bower-files": "^3.14.1","browser-sync": "^2.18.5","browserfy": "^1.0.0","browserify": "^13.1.1","del": "^2.2.2","gulp-concat": "^2.6.1","gulp-jshint": "^2.0.4","gulp-uglify": "^2.0.0","gulp-util": "^3.0.8","jshint": "^2.9.4","vinyl-source-stream": "^1.1.0"}}')
        file.close()
        
        file = open("./bower.json", "w") # ESTE ES EL BUENO bower.json
        file.write('{"{"name": "alarm","description": "Alarm clock project during week1 day2 JS at Epicodus.","main": "gulpfile.js","authors": ["Andrew Accuardi <andrewaccuardi@gmail.com>"],"license": "ISC","homepage": "","ignore": ["**/.*","node_modules","bower_components","test","tests"],"dependencies": {"jquery": "^3.1.1","bootstrap": "^3.3.7","moment": "^2.17.1","components-font-awesome": "^4.7.0","font-awesome": "^4.7.0","materialize": "^0.97.8"}}')
        file.close()
        
        file = open("./bower.txt", "w")
        file.write('no')
        file.close()
        file = open("./package.txt", "w")
        file.write('no')
        file.close()
        file = open("./json.json", "w")
        file.write('no')
        file.close()
        file = open("./css.json", "w")
        file.write('no')
        file.close()

    # Borramos lo que habiamos creado para que quede bonito
    def tearDownClass():

        os.rmdir("bower")
        os.rmdir("package")
        os.rmdir("json")
        os.rmdir("bowerjson")
        os.rmdir("packagejson")
        
        os.remove("bower.txt")
        os.remove("package.txt")
        os.remove("json.json")
        os.remove("css.json")
        os.remove("bower.json")
        os.remove("package.json")
         
        
    # Como vamos a estar llamando todo el rato en cada uno de los test al main
    # de la clase lo hacemos aqui, a si hay menos codigo repetido    
    def setUp(self):
        self.datos =  css_json_json.liderDelTrabajo()


    def test_nombre(self):
        self.assertEqual(self.datos['name'],'alarm')
        
    def test_version(self):
        self.assertEqual(self.datos['version'],'1.0.0')
        
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'Alarm clock project during week1 day2 JS at Epicodus.')
        
    def test_license(self):  
         self.assertEqual(self.datos['license'], 'ISC')       
     
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'Andrew Accuardi')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'andrewaccuardi@gmail.com')
        
    
    def test_require(self):
        self.assertEqual(self.datos['dependencies']['jquery'], '^3.1.1')
        self.assertEqual(self.datos['dependencies']['bootstrap'], '^3.3.7')
        self.assertEqual(self.datos['dependencies']['moment'], '^2.17.1')
        self.assertEqual(self.datos['dependencies']['components-font-awesome'], '^4.7.0')
        self.assertEqual(self.datos['dependencies']['font-awesome'], '^4.7.0')
        self.assertEqual(self.datos['dependencies']['materialize'], '^0.97.8')
        
    def test_requireDev(self):
        self.assertEqual(self.datos['dev-dependencies']['gulp'], '^3.9.1')
        self.assertEqual(self.datos['dev-dependencies']['bower-files'], '^3.14.1')
        self.assertEqual(self.datos['dev-dependencies']['browser-sync'], '^2.18.5')
        self.assertEqual(self.datos['dev-dependencies']['browserfy'], '^1.0.0')
        self.assertEqual(self.datos['dev-dependencies']['browserify'], '^13.1.1')
        self.assertEqual(self.datos['dev-dependencies']['del'], '^2.2.2')
        
if __name__ == '__main__':
    unittest.main()