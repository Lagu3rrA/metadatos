# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 00:32:38 2022

@author: Lagu3rrA
"""

# -*- coding: utf-8 -*-
import os
import json
import xml.etree.cElementTree as ET 


# Creo el diccionario en el que voy a meter la informacion
datos = {}

class java_xml_json:
    
    def cargar_el_xml(ruta):
        
            tree = ET.ElementTree(file = 'pom.xml')
            return tree.getroot()
        
    def rellenar_el_diccionario(xmlo):
        for atributos in xmlo:
            
          
            if atributos.tag.endswith('name') and atributos.text:
                datos['name'] = atributos.text
            elif atributos.tag.endswith('artifactId') and atributos.text: # Si no existe nombre como tal de damos el del artifactId
                datos['name'] = atributos.text
            
            if atributos.tag.endswith('url') and atributos.text:
                datos['homepage'] = atributos.text
                
            if atributos.tag.endswith('scm'):
                # Dentro del atributo scm
                for scm in atributos:
                    # Vuelvo a iterar sobre el para llegar al url 
                    # del repositorio que es lo que me interesa
                    if scm.tag.endswith('url') and scm.text:
                        datos['repository'] = scm.text
            
            if atributos.tag.endswith('version')and atributos.text:
                datos['version'] = atributos.text 
            
                
            if atributos.tag.endswith('developers'):
                #Entramos dentro de los developers
                
                listaDeAutores = []
                
                for autores in atributos:
                    # iteramos cada uno de los desarolladores
                    
                    # al crearse aqui este mapa, se pondra a cero cada vez que acabe con un developer
                    autor = {}
                    
                    for __a__ in autores:
                        # para cada uno vemos si tiene los atributos de nombre y de email
                        if __a__.tag.endswith('name') and __a__.text:
                            autor['name'] = __a__.text
                         
                        if __a__.tag.endswith('email') and __a__.text:
                            autor['email'] = __a__.text
                    
                    # cuando acabamos de iterar los atributos 
                    listaDeAutores.append(autor)
                        
                datos['authors'] = listaDeAutores
                
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
                            if infor.tag.endswith('artifactId') and infor.text:
                                tupla['name'] = infor.text
                        
                            if infor.tag.endswith('version') and infor.text:
                                tupla['version'] = infor.text
                               
                            # Y la meto en la lista de dependecias
                            dependecias.append(tupla)
                           
                # una vez cnstruida la lista de dependecias la guardo en el diccionario grande de datos 
                datos['dependencies'] = dependecias
              
            if atributos.tag.endswith('licenses'):
                
                  listaDeLicencias = []
                  for licencias in atributos:
                      #tupla = {}
                      for licencia in licencias:
                          if licencia.tag.endswith('name') and licencia.text:
                              datos['license'] = licencia.text
                          """
                          if licencia.tag.endswith('name') and licencia.text:
                              tupla['name'] = licencia.text
                      
                          if licencia.tag.endswith('url') and licencia.text:
                              tupla['url'] = licencia.text
                        
                          listaDeLicencias.append(tupla)
                          """
            if atributos.tag.endswith('description') and atributos.text:
                datos['description'] = atributos.text 
                


    def liderDelTrabajo():
           
            xmlo = java_xml_json.cargar_el_xml('./pom.xml')
            
            java_xml_json.rellenar_el_diccionario(xmlo)
            return datos
                    
            
           
    
            
            
        
        