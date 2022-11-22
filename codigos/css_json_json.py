# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: jacan
"""

import os
import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class css_json_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_json(ruta):
        with open(ruta) as contenido: 
            curso = json.load(contenido)
            return curso
    
    def casoDependecias(jsono, mapaDeDependecias):
        
        if 'devDependencies' in jsono:
            for key, value in jsono['devDependencies'].items():
                mapaDeDependecias[key] = value
            
        if 'dependencies' in jsono:
            for key, value in jsono['dependencies'].items():
                mapaDeDependecias[key] = value
 
    def casoAutores(listaCreadores):
        listaDeAutores = []
        
        autor = {}
        
        # Recorro la lista de autores 
        for auto in listaCreadores:
            
            # Para cada uno separo el mail del nombre
            _a_ = auto.split('<')
            
            # guardo el nombre como name
            autor['name'] = _a_[0]
            
            # En el caso de que hubiese email, es decir que se pudiera dividir
            if len(_a_)>0:
                
                # guardo el email en el mapa del autor 
                autor['email'] = _a_[1].replace(">","")
            
            # añado el autor a la la lista de autores que devolveremos
            listaDeAutores.append(autor)
            
            return listaDeAutores
        
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(jsonoPackage,jsonoBower):
        
        # Es asi de facil sacar los datos del json 
        
        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        
        if 'name' in jsonoPackage: 
            datos['name'] = jsonoPackage['name']
            
        if 'homepage' in jsonoPackage: 
            datos['homepage'] = jsonoPackage['homepage']
        
        if 'repository' in jsonoPackage: 
            datos['url'] = jsonoPackage['repository']['url']
            
        if 'version' in jsonoPackage: 
            datos['version'] = jsonoPackage['version'] 
            
        if 'authors' in jsonoBower: 
            # llamos al caso autores con la lista de autores que nos da el bower
            datos['authors'] = css_json_json.casoAutores(jsonoBower['authors'])   
        
        if 'keywords' in jsonoPackage: 
            datos['keywords'] = jsonoPackage['keywords']
            
        if 'license' in jsonoPackage: 
            datos['license'] = jsonoPackage['license']
            
        if 'description' in jsonoBower: 
            datos['description'] = jsonoBower['description']   
          
        mapaDeDependecias = {}
        if 'devDependencies' in jsonoPackage or 'dependencies' in jsonoPackage :
            css_json_json.casoDependecias(jsonoPackage,mapaDeDependecias)
        
        if 'devDependencies' in jsonoBower or 'dependencies' in jsonoBower :
            css_json_json.casoDependecias(jsonoBower,mapaDeDependecias)   
            
        if not mapaDeDependecias == {}:
            datos['dependecies'] = mapaDeDependecias
        
    
    # Vuelco los datos del diccionario en un archivo json 
    def crear_el_nuevo_json():
    
            
            dir = r"."
            file_name =  "css_metadatos.json"
            
            with open(os.path.join(dir, file_name), 'w') as file:
                json.dump(datos, file) 
                
                
    def liderDelTrabajo():#ruta
        
        
        # Sacamos la informacion del json
        jsonoPackage = css_json_json.cargar_el_json('./package.json')
        jsonoBower = css_json_json.cargar_el_json('./bower.json')
        
        # La guardamos en el diccionario
        css_json_json.rellenar_el_diccionario(jsonoPackage,jsonoBower)
        print(datos)
        # Creamos el archivo que vamos a devolver
        css_json_json.crear_el_nuevo_json()
        