# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from php_json_json import *

class Test_1_php(unittest.TestCase):
    
    # -----------------------------------------------
    # Este test comprueba que todo este bien devuelto 
    # -----------------------------------------------
    
    
    # Creamos el ambiente con el archivo bueno y cosas al rededor simulando un proyecto
    def setUpClass():
        
        os.makedirs('composer')
        os.makedirs('json')
        os.makedirs('composerjson')
        
        file = open("./composer.json", "w") # ESTE ES EL BUENO Composer.json
        file.write('{"name": "composer/composer","description": "Composer helps you declare, manage and install dependencies of PHP projects. It ensures you have the right stack everywhere.","keywords": ["package","dependency","autoload"],"homepage": "https://getcomposer.org/","license": "MIT","authors": [{"name": "Nils Adermann","email": "naderman@naderman.de","homepage": "https://www.naderman.de"},{"name": "Jordi Boggiano","email": "j.boggiano@seld.be","homepage": "https://seld.be"}],"require": {"php": "^7.2.5 || ^8.0","composer/ca-bundle": "^1.0","composer/class-map-generator": "^1.0","composer/metadata-minifier": "^1.0","composer/semver": "^3.0","composer/spdx-licenses": "^1.5.7","composer/xdebug-handler": "^2.0.2 || ^3.0.3","justinrainbow/json-schema": "^5.2.11","psr/log": "^1.0 || ^2.0 || ^3.0","seld/jsonlint": "^1.4","seld/phar-utils": "^1.2","symfony/console": "^5.4.11 || ^6.0.11","symfony/filesystem": "^5.4 || ^6.0","symfony/finder": "^5.4 || ^6.0","symfony/process": "^5.4 || ^6.0","react/promise": "^2.8","composer/pcre": "^2 || ^3","symfony/polyfill-php73": "^1.24","symfony/polyfill-php80": "^1.24","seld/signal-handler": "^2.0"},"require-dev": {"symfony/phpunit-bridge": "^6.0","phpstan/phpstan": "^1.4.1","phpstan/phpstan-phpunit": "^1.0","phpstan/phpstan-deprecation-rules": "^1","phpstan/phpstan-strict-rules": "^1","phpstan/phpstan-symfony": "^1.2.10"}}')
        file.close()
        
        file = open("./composer.txt", "w")
        file.write('no')
        file.close()
        file = open("./json.json", "w")
        file.write('no')
        file.close()
        file = open("./php.json", "w")
        file.write('no')
        file.close()
    
    # Borramos lo que habiamos creado para que quede bonito
    def tearDownClass():
        
        os.rmdir("composer")
        os.rmdir("json")
        os.rmdir("composerjson")
        
        os.remove("composer.txt")
        os.remove("json.json")
        os.remove("php.json")
        os.remove("composer.json")
         
        
    # Como vamos a estar llamando todo el rato en cada uno de los test al main
    # de la clase lo hacemos aqui, a si hay menos codigo repetido    
    def setUp(self):
        self.datos =  php_json_json.liderDelTrabajo()


    def test_nombre(self):
        self.assertEqual(self.datos['name'],'composer/composer')
        
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'Composer helps you declare, manage and install dependencies of PHP projects. It ensures you have the right stack everywhere.')

    def test_keywords(self):
        keywords  =  ["package","dependency","autoload"]
        self.assertEqual(self.datos['keywords'], keywords)
        
    def test_homepage(self):  
        self.assertEqual(self.datos['homepage'], 'https://getcomposer.org/')
        
    def test_license(self):  
         self.assertEqual(self.datos['license'], 'MIT')       
     
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'Nils Adermann')
        self.assertEqual(self.datos['authors'][1]['name'], 'Jordi Boggiano')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'naderman@naderman.de')
        self.assertEqual(self.datos['authors'][1]['email'], 'j.boggiano@seld.be')
        
    
    def test_require(self):
        self.assertEqual(self.datos['dependencies']['php'], '^7.2.5 || ^8.0')
        self.assertEqual(self.datos['dependencies']['composer/ca-bundle'], '^1.0')
        self.assertEqual(self.datos['dependencies']['composer/class-map-generator'], '^1.0')
        self.assertEqual(self.datos['dependencies']['composer/metadata-minifier'], '^1.0')
        self.assertEqual(self.datos['dependencies']['composer/semver'], '^3.0')
        self.assertEqual(self.datos['dependencies']['composer/spdx-licenses'], '^1.5.7')
        self.assertEqual(self.datos['dependencies']['composer/xdebug-handler'], '^2.0.2 || ^3.0.3')
        self.assertEqual(self.datos['dependencies']['justinrainbow/json-schema'], '^5.2.11')
        self.assertEqual(self.datos['dependencies']['psr/log'], '^1.0 || ^2.0 || ^3.0')
        self.assertEqual(self.datos['dependencies']['seld/jsonlint'], '^1.4')
        
    def test_requireDev(self):
        self.assertEqual(self.datos['dev-dependencies']['symfony/phpunit-bridge'], '^6.0')
        self.assertEqual(self.datos['dev-dependencies']['phpstan/phpstan'], '^1.4.1')
        self.assertEqual(self.datos['dev-dependencies']['phpstan/phpstan-phpunit'], '^1.0')
        self.assertEqual(self.datos['dev-dependencies']['phpstan/phpstan-deprecation-rules'], '^1')
        self.assertEqual(self.datos['dev-dependencies']['phpstan/phpstan-strict-rules'], '^1')
        self.assertEqual(self.datos['dev-dependencies']['phpstan/phpstan-symfony'], '^1.2.10')
if __name__ == '__main__':
    unittest.main()