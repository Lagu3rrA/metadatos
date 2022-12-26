
import os



from java_xml_json import *
"""
from php_json_json import *
from R_txt_json import *
from css_json_json import *
from rust_toml_json import *
from julia_toml_json import * 
from haskell_cabal_json import *
from ruby_gemspec_json import *
from python_py_json import *
from javascript_json_json import *
from python_cfg_json import *
from javascript_json_json import *
"""

# Esta es la lista de json que vamos a devolver sui encopntramos mas de un archivo 
# enciam vendra de que lengujes es
listaDeJsonDevueltos = []
    

for f in os.listdir(r"."):

    if (f == 'pom.xml'):
        datos = java_xml_json.liderDelTrabajo()
        
        if datos:
            listaDeJsonDevueltos.append('JAVA_pom.xml')
            listaDeJsonDevueltos.append(datos)
        continue
 

#print(listaDeJsonDevueltos)   


dir = r"."

print('¿Como quieres llamar al archivo de metadatos?')
name =  input()
file_name = name + '.json'

with open(os.path.join(dir, file_name), 'w') as file:
    json.dump(listaDeJsonDevueltos, file) 


    
    