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
            
            dir = r"D:\Universidad\Univerisdad\tfg"
            file_name =  "php_metadatos.json"
            
            with open(os.path.join(dir, file_name), 'w') as file:
                json.dump(datos, file)
            
                
    # Recorremos todos los directorios que encontremos en esta ruta buscando el que empieze por el documento buscado
    # Lo buscamos y no lo hacemos directamente por si el archivo no existe
    for f in os.listdir(r"D:\Universidad\Univerisdad\tfg"):
        if f.startswith("composer"):
           
            # Si lo hemos encontrado cargamos el json 
            ruta = r'D:\Universidad\Univerisdad\tfg\composer.json'
            
            # Sacamos la informacion del json
            jsono = cargar_el_json(ruta)
            
            # La guardamos en el diccionario
            rellenar_el_diccionario(jsono)
            
            # Creamos el archivo que vamos a devolver
            crear_el_nuevo_json()
        
        

        
        
        
        