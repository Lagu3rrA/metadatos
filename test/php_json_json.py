# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: Lagu3rrA
"""

import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class php_json_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_json(ruta):
        with open(ruta) as contenido: 
            curso = json.load(contenido)
            return curso
    def  casoAutores(autores):
        listaDeAutores = []
        for __a__ in autores:
            autor = {}
            if 'name' in __a__:
                autor['name'] = __a__['name']
                
            if 'email' in __a__:
                autor['email'] = __a__['email']
            listaDeAutores.append(autor)
        return listaDeAutores
        
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
            
        if 'authors' in jsono: 
            datos['authors'] = php_json_json.casoAutores(jsono['authors'])     
        
        if 'keywords' in jsono: 
            datos['keywords'] = jsono['keywords']
            
        if 'license' in jsono: 
            datos['license'] = jsono['license']
            
        if 'description' in jsono: 
            datos['description'] = jsono['description']
        
        if 'require' in jsono:
            datos['dependencies'] = jsono['require']
        
        if 'require-dev' in jsono:
            datos['dev-dependencies'] = jsono['require-dev']
            
            
    def liderDelTrabajo():#ruta
        
        # Sacamos la informacion del json
        jsono = php_json_json.cargar_el_json('.\composer.json')
        
        # La guardamos en el diccionario
        php_json_json.rellenar_el_diccionario(jsono)
        
        return datos
        
        

        
        
        
        