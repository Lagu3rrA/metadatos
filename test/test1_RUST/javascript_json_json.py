# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: jacan
"""

import os
import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class javascript_json_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    #def cargar_el_json(ruta):
    def cargar_el_json(ruta):
        with open('./package.json','r') as contenido: 
            curso = json.load(contenido)
            return curso
              
    
    def casoAutores(jsono):
        autor = {}
        listaDeAutores = []
        
        if 'maintainers' in jsono:
            a = jsono['maintainers'][0]
            listaDeAutores.append(a)
            return listaDeAutores
        
        if 'author' in jsono:
            autorEntero = jsono['author']
            autorito = autorEntero.split('<')
            autor['name'] = autorito[0]
            if len(autorito)>0:
                autor['email'] = autorito[1].replace(">","")
            listaDeAutores.append(autor)
            return listaDeAutores
        
        return listaDeAutores

    def casoDependecias(jsono):
        mapaDeDependecias = {}
        
        if 'devDependencies' in jsono:
            for key, value in jsono['devDependencies'].items():
                mapaDeDependecias[key] = value
            
        if 'dependencies' in jsono:
            for key, value in jsono['dependencies'].items():
                mapaDeDependecias[key] = value
 
        return mapaDeDependecias
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(jsono):
        
        # Es asi de facil sacar los datos del json 
        
        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        
     
        if 'name' in jsono: 
            datos['name'] = jsono['name']
            
        if 'homepage' in jsono: 
            datos['homepage'] = jsono['homepage'] 
            
        if 'version' in jsono: 
            datos['version'] = jsono['version'] 
        
        if 'author' in jsono: 
            datos['authors'] = javascript_json_json.casoAutores(jsono)      
        
        if 'keywords' in jsono: 
            datos['keywords'] = jsono['keywords']
            
        if 'license' in jsono: 
            datos['license'] = jsono['license']
            
        if 'description' in jsono: 
            datos['description'] = jsono['description']   
        
        if 'repository' in jsono: 
            datos['url'] = jsono['repository']['url'].replace("git+","")
            
        if 'devDependencies' in jsono or 'dependencies' in jsono :
            datos['dependecies'] = javascript_json_json.casoDependecias(jsono)

            
    # Vuelco los datos del diccionario en un archivo json 
    def crear_el_nuevo_json():
    
            
            dir = r"."
            file_name =  "javascript_metadatos.json"
            
            with open(os.path.join(dir, file_name), 'w') as file:
                json.dump(datos, file) 
                
                
    def liderDelTrabajo():#ruta
        
        # Sacamos la informacion del json
        jsono = javascript_json_json.cargar_el_json('./package.json')
        
        # La guardamos en el diccionario
        javascript_json_json.rellenar_el_diccionario(jsono)
        
        # Creamos el archivo que vamos a devolver
        javascript_json_json.crear_el_nuevo_json()
