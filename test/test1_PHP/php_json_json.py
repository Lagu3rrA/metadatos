# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: jacan
"""

import os
import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class php_json_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_json(ruta):
        with open(ruta) as contenido: 
            curso = json.load(contenido)
            return curso
    
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
            datos['authors'] = jsono['authors']      
        
        if 'keywords' in jsono: 
            datos['keywords'] = jsono['keywords']
            
        if 'license' in jsono: 
            datos['license'] = jsono['license']
            
        if 'description' in jsono: 
            datos['description'] = jsono['description']    
            
    
    # Vuelco los datos del diccionario en un archivo json 
    def crear_el_nuevo_json():
    
            
            dir = r"."
            file_name =  "php_metadatos.json"
            
            with open(os.path.join(dir, file_name), 'w') as file:
                json.dump(datos, file) 
                
                
    def liderDelTrabajo():#ruta
        
        print('php')
        # Sacamos la informacion del json
        jsono = php_json_json.cargar_el_json('./composer.json')
        
        # La guardamos en el diccionario
        php_json_json.rellenar_el_diccionario(jsono)
        
        # Creamos el archivo que vamos a devolver
        php_json_json.crear_el_nuevo_json()
        
        

        
        
        
        