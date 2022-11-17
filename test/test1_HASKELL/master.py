# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:12:28 2022

@author: jacan
"""
import os
#from php_json_json import *
#from R_txt_json import *
#from java_xml_json import *
#from css_json_json import *
#from rust_toml_json import *
#from julia_toml_json import * 
from haskell_cabal_json import *


for f in os.listdir(r"."):
    
    if (f == 'setup.cfg'): 
        print('1')
        
    if (f == 'setup.py'):
        print('2')
        
    if (f == 'Cargo.toml'):
        print('3')
        rust_toml_json.liderDelTrabajo()
        
    if (f == 'pom.xml'):
        print('4')
        java_xml_json.liderDelTrabajo()
  
    if (f == 'bower.json'):
        print('5')
        
        
    if (f == 'package.json'):
        print('6')
        css_json_json.liderDelTrabajo()
    
    if (f == 'composer.json'):
        print('7')
        php_json_json.liderDelTrabajo()
    
    if (f == 'DESCRIPTION.txt'):
        print('8')
        R_txt_json.liderDelTrabajo()
        
    if (f == 'Project.toml'):
        print('9')
        julia_toml_json.liderDelTrabajo()
        
    if (f.endswith('.cabal')):
        print('10')
        haskell_cabal_json.liderDelTrabajo(f)
        
    
    if (f.endswith('.gemspec')):
        print('11')        
        

      
                  
    
    
    