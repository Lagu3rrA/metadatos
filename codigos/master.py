
import os

from julia_toml_json import * 
from php_json_json import *
from R_txt_json import *
from css_json_json import *
from rust_toml_json import *
from haskell_cabal_json import *
from ruby_gemspec_json import *
from python_py_json import *
from javascript_json_json import *
from java_xml_json import *
from python_cfg_json import *
from javascript_json_json import *

# Esta es la lista de json que vamos a devolver sui encopntramos mas de un archivo 
# enciam vendra de que lengujes es
listaDeJsonDevueltos = []
    

for f in os.listdir(r"."):
    
    if (f == 'setup.cfg'): 
        datos = python_cfg_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('PYTHON_setup.cfg')
            listaDeJsonDevueltos.append(datos)
        continue
        
    if (f == 'setup.py'):
        datos = python_py_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('PYTHON_setup.py')
            listaDeJsonDevueltos.append(datos)
        
        continue
        
    if (f == 'Cargo.toml'):
        datos = rust_toml_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('RUST_Cargo.toml')
            listaDeJsonDevueltos.append(datos)
        continue
        
    if (f == 'pom.xml'):
        datos = java_xml_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('JAVA_pom.xml')
            listaDeJsonDevueltos.append(datos)
        continue

  
    if (f == 'bower.json'):
        datos = css_json_json.liderDelTrabajo()
        if datos:
            listaDeJsonDevueltos.append('CSS_bower.json')
            listaDeJsonDevueltos.append(datos)
        continue
        
        
    if (f == 'package.json'):
        # Aqui hay dos casos 
        for f in os.listdir(r"."):
            # que sea con bower.json de CSS
            if (f == 'bower.json'):
                datos = css_json_json.liderDelTrabajo()
                
                if datos:
                    listaDeJsonDevueltos.append('CSS_bower.json')
                    listaDeJsonDevueltos.append(datos)
                continue
   
        # que sea solo con el package.json de Javascript 
        # usamos el de javascript por que seri gigual para este caso
        datos = javascript_json_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('JAVASCRIPT_package.json')
            listaDeJsonDevueltos.append(datos)
        continue
    
    if (f == 'composer.json'):
        datos = php_json_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('PHP_composer.json')
            listaDeJsonDevueltos.append(datos)
        continue
    
    if (f == 'DESCRIPTION.txt'):
        datos = R_txt_json.liderDelTrabajo()
       
        if datos:
            listaDeJsonDevueltos.append('R_DESCRIPTION.txt')
            listaDeJsonDevueltos.append(datos)
        continue
        
    if (f == 'Project.toml'):
        datos = julia_toml_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('JULIA_Project.toml')
            listaDeJsonDevueltos.append(datos)
        continue
        
    if (f.endswith('.cabal')):
        datos = haskell_cabal_json.liderDelTrabajo(f)
        
        if datos:
            listaDeJsonDevueltos.append('HASKELL_cabal')
            listaDeJsonDevueltos.append(datos)
        continue
        
    if (f.endswith('.gemspec')):
        datos = ruby_gemspec_json.liderDelTrabajo(f)
        
        if datos:
            listaDeJsonDevueltos.append('RUBY_gemspec')
            listaDeJsonDevueltos.append(datos)
        continue


dir = r"."

print('¿Como quieres llamar al archivo de metadatos?')
name =  input()
file_name = name + '.json'

with open(os.path.join(dir, file_name), 'w') as file:
    json.dump(listaDeJsonDevueltos, file) 
       
    
    
    