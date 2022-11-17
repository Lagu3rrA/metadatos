# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 00:32:38 2022

@author: jacan
"""

# -*- coding: utf-8 -*-
import os
import json
import xml.etree.cElementTree as ET 


# Creo el diccionario en el que voy a meter la informacion
datos = {}


def cargar_el_xml(ruta):
    
        tree = ET.ElementTree(file = 'pom.xml')
        return tree.getroot()
    
def rellenar_el_diccionario(xmlo):
    for atributos in xmlo:
        
        if atributos.tag.endswith('name'):
            datos['name'] = atributos.text
        
        if atributos.tag.endswith('url'):
            datos['homepage'] = atributos.text
            
        if atributos.tag.endswith('scm'):
            # Dentro del atributo scm
            for scm in atributos:
                # Vuelvo a iterar sobre el para llegar al url 
                # del repositorio que es lo que me interesa
                if scm.tag.endswith('url'):
                    datos['repository'] = scm.text
        
        if atributos.tag.endswith('version'):
            datos['version'] = atributos.text 
        
        if atributos.tag.endswith('groupId'):
            datos['groupId'] = atributos.text
            
        if atributos.tag.endswith('developers'):
            
            for autores in atributos:
                if autores.tag.endswith('name'):
                    datos['name'] = autores.text
                    
                if autores.tag.endswith('email'):
                    datos['email'] = autores.text
         
      
    
        if atributos.tag.endswith('dependencyManagement'):
            
            # Creo un lisa en la que voy  a meter todas las dependecias
            dependecias = []
          
            # itero sobre dependencyManagement 
            for dependeciasVarias in atributos:
              
                #itero sobre dependencies 
                for cadauna in dependeciasVarias:
                   
                    # creo otro dicionario como tupla para que este el nombre y la version 
                    # de la dependecia
                    tupla = {}
                   
                    # y por ultimo itero sobre la dependecia en si viendo sus componentes
                    for infor in cadauna:
                       
                        # Saco su nombre y su version
                        if infor.tag.endswith('artifactId'):
                            tupla['name'] = infor.text
                    
                        if infor.tag.endswith('version'):
                            tupla['version'] = infor.text
                           
                        # Y la meto en la lista de dependecias
                        dependecias.append(tupla)
                       
            # una vez cnstruida la lista de dependecias la guardo en el diccionario grande de datos 
            datos['Dependencies'] = dependecias
          
        if atributos.tag.endswith('licenses'):
              listaDeLicencias = []
              for licencias in atributos:
                  tupla = {}
                  for licencia in licencias:
                      if licencia.tag.endswith('name'):
                          tupla['name'] = licencia.text
                  
                      if licencia.tag.endswith('url'):
                          tupla['url'] = licencia.text
                    
                      listaDeLicencias.append(tupla)
      
        if atributos.tag.endswith('description'):
            datos['Description'] = atributos.text 
            

def crear_el_nuevo_json():
        
        
        dir = r"D:\Universidad\Univerisdad\tfg"
        file_name = "java_metadatos.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file)
            

for f in os.listdir(r"D:\Universidad\Univerisdad\tfg"):
    if f.startswith("pom"):
       
        ###
        ruta = r'D:\Universidad\Univerisdad\tfg\pom.xml'
        xmlo = cargar_el_xml(ruta)
        
        rellenar_el_diccionario(xmlo)
            
        crear_el_nuevo_json()
                
        
       

        
        
        
        