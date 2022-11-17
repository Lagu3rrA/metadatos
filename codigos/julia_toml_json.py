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

 
class julia_toml_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_toml(ruta):
        curso = toml.load("Project.toml")
        return curso

    def crearListaAutores(listaDeAutoresTOML):
        for autor in listaDeAutoresTOML:
            # aqui guardaremos el autor y su email
            unidadDeAutor = {}
            
            #Separo entre autor y su email
            autorPartido = autor.split("<")
            
            #guardo la primera parete que es el nombre del autor
            unidadDeAutor['name'] = autorPartido[0]
            
            # guardo la segunda parte poniendo lo bonito como el email
            unidadDeAutor['email'] = autorPartido[1].replace(">", "")
            
            return unidadDeAutor
    
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(toml):
        
        # Es asi de facil sacar los datos del json 
        
        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        

        if 'name' in toml:
            datos['name'] = toml['name']
            
        if 'version' in toml: 
            datos['version'] = toml['version']
            
        if 'authors' in toml: 
            
            #Cojo la lista de autores del json del toml
            listaDeAutoresTOML = toml['authors']
            
            #creo la lista en la que metere todos los autores
            listaDeAutoresJSON = []
            
            #guardamos la lista para meterla en el diccionario
            listaDeAutoresJSON = julia_toml_json.crearListaAutores(listaDeAutoresTOML)
            
            datos['authors'] = listaDeAutoresJSON
            
        if 'license' in toml:
            datos['license'] = toml['license']
     
        if 'keywords' in toml:
           datos['keywords'] = toml['keywords']
           
        if 'repository' in toml:
           datos['repository'] = toml['repository']
            
        if 'desc' in toml:
           datos['description'] = toml['desc']
           
        if 'documentation' in toml:
           datos['homepage'] = toml['documentation']
           
           
        if 'compat' in toml:
            datos['dependecies'] = toml['compat']
            
            
    
    # Vuelco los datos del diccionario en un archivo json 
    def crear_el_nuevo_json():

        dir = r"."
        file_name =  "julia_metadatos.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file) 
                
                
    def liderDelTrabajo():
        
        print('julia')
        # Sacamos la informacion del json
        toml = julia_toml_json.cargar_el_toml('./Project.toml')
        
        
        # La guardamos en el diccionario
        julia_toml_json.rellenar_el_diccionario(toml)
        
        
        # Creamos el archivo que vamos a devolver
        julia_toml_json.crear_el_nuevo_json()