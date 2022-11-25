# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: jacan
"""
import os
import toml
import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class rust_toml_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_toml(ruta):
        curso = toml.load("Cargo.toml")
        return curso

    def crearListaAutores(listaDeAutoresTOML):
        listaDeAutores = []
        for autor in listaDeAutoresTOML:
            # aqui guardaremos el autor y su email
            unidadDeAutor = {}
            
            #Separo entre autor y su email
            autorPartido = autor.split("<")
            
            #guardo la primera parete que es el nombre del autor
            unidadDeAutor['name'] = autorPartido[0]
            
            # guardo la segunda parte poniendo lo bonito como el email
            unidadDeAutor['email'] = autorPartido[1].replace(">", "")
            
            listaDeAutores.append(unidadDeAutor)
            
        return listaDeAutores
    
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(toml):
        
        # Es asi de facil sacar los datos del json 
        
        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        
        if 'package' in toml: 
            
           if 'name' in toml['package']:
               datos['name'] = toml['package']['name']
               
           if 'version' in toml['package']: 
               datos['version'] = toml['package']['version']
               
           if 'authors' in toml['package']: 
               
               #Cojo la lista de autores del json del toml
               listaDeAutoresTOML = toml['package']['authors']
               
               #creo la lista en la que metere todos los autores
               listaDeAutoresJSON = []
               
               #guardamos la lista para meterla en el diccionario
               listaDeAutoresJSON = rust_toml_json.crearListaAutores(listaDeAutoresTOML)
               
               datos['authors'] = listaDeAutoresJSON
               
           if 'license' in toml['package']:
               datos['license'] = toml['package']['license']
        
           if 'keywords' in toml['package']:
              datos['keywords'] = toml['package']['keywords']
              
           if 'repository' in toml['package']:
              datos['repository'] = toml['package']['repository']
               
           if 'description' in toml['package']:
              datos['description'] = toml['package']['description']
              
           if 'documentation' in toml['package']:
              datos['homepage'] = toml['package']['documentation']
           
        if 'dependencies' in toml:
            datos['dependecies'] = toml['dependencies']
            
            
    
    # Vuelco los datos del diccionario en un archivo json 
    def crear_el_nuevo_json():

        dir = r"."
        file_name =  "rust_metadatos.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file) 
                
                
    def liderDelTrabajo():
        
        print('rust')
        # Sacamos la informacion del json
        toml = rust_toml_json.cargar_el_toml('./Cargo.toml')
        
        
        # La guardamos en el diccionario
        rust_toml_json.rellenar_el_diccionario(toml)
        
        
        # Creamos el archivo que vamos a devolver
        rust_toml_json.crear_el_nuevo_json()
            