# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:12:28 2022

@author: jacan
"""
import os
#from php_json_json import *
#from R_txt_json import *
from java_xml_json import *
#from css_json_json import *
#from rust_toml_json import *
#from julia_toml_json import * 
#from haskell_cabal_json import *
#from ruby_gemspec_json import *
#from python_py_json import *
#from javascript_json_json import *
#from python_cfg_json import *

for f in os.listdir(r"."):
    
    if (f == 'setup.cfg'): 
        print('1')
        python_cfg_json.liderDelTrabajo()
        
    if (f == 'setup.py'):
        print('2')
        python_py_json.liderDelTrabajo()
        break
        
    if (f == 'Cargo.toml'):
        print('3')
        rust_toml_json.liderDelTrabajo()
        break
        
    if (f == 'pom.xml'):
        print('4')
        java_xml_json.liderDelTrabajo()
        break
  
    if (f == 'bower.json'):
        print('5')
        css_json_json.liderDelTrabajo()
        break
        
        
    if (f == 'package.json'):
        print('6')
        # Aqui hay dos casos 

        for f in os.listdir(r"."):
            # que sea con bower.json de CSS
            if (f == 'bower.json'):
                css_json_json.liderDelTrabajo()
                break
   
        # que sea solo con el package.json de Javascript
        javascript_json_json.liderDelTrabajo()
        break
    
    if (f == 'composer.json'):
        print('7')
        php_json_json.liderDelTrabajo()
        break
    
    if (f == 'DESCRIPTION.txt'):
        print('8')
        R_txt_json.liderDelTrabajo()
        break
        
    if (f == 'Project.toml'):
        print('9')
        julia_toml_json.liderDelTrabajo()
        break
        
    if (f.endswith('.cabal')):
        print('10')
        haskell_cabal_json.liderDelTrabajo(f)
        break
        
    if (f.endswith('.gemspec')):
        print('11')       
        ruby_gemspec_json.liderDelTrabajo(f)
        break
        

      
                  
    
    
    