# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: Lagu3rrA
"""

import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class css_json_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_json(ruta):
        with open(ruta) as contenido: 
            curso = json.load(contenido)
            return curso
    
 
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
        
        if 'name' in jsonoPackage and jsonoPackage['name']: 
            datos['name'] = jsonoPackage['name']
            
        if 'homepage' in jsonoPackage and jsonoPackage['homepage']: # solo comprueba el package, podria comprobar tambien el bower
            datos['homepage'] = jsonoPackage['homepage'] 
        
        if 'repository' in jsonoPackage and jsonoPackage['repository']['url']: 
            datos['url'] = jsonoPackage['repository']['url']
            
        if 'version' in jsonoPackage and jsonoPackage['version'] : 
            datos['version'] = jsonoPackage['version'] 
            
        if 'authors' in jsonoBower and jsonoBower['authors']: 
            # llamos al caso autores con la lista de autores que nos da el bower
            datos['authors'] = css_json_json.casoAutores(jsonoBower['authors'])   
        
        if 'keywords' in jsonoPackage and jsonoPackage['keywords']: 
            datos['keywords'] = jsonoPackage['keywords']
            
        if 'license' in jsonoPackage and jsonoPackage['license']: 
            datos['license'] = jsonoPackage['license']
            
        if 'description' in jsonoBower and jsonoBower['description']: 
            datos['description'] = jsonoBower['description']   
            
        if 'devDependencies' in jsonoPackage and jsonoPackage['devDependencies']:
            datos['dev-dependencies'] = jsonoPackage['devDependencies']
            
        if 'dependencies' in jsonoBower and jsonoBower['dependencies']:
            datos['dependencies'] = jsonoBower['dependencies']
        
        
    
    def liderDelTrabajo():#ruta
        
        
        # Sacamos la informacion del json
        jsonoPackage = css_json_json.cargar_el_json('./package.json')
        jsonoBower = css_json_json.cargar_el_json('./bower.json')
        
        # La guardamos en el diccionario
        css_json_json.rellenar_el_diccionario(jsonoPackage,jsonoBower)

        return datos
        
