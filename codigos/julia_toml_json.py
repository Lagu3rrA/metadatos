# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: Lagu3rrA
"""

import toml


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
        

        if 'name' in toml and toml['name']:
            datos['name'] = toml['name']
            
        if 'version' in toml and toml['version']: 
            datos['version'] = toml['version']
            
        if 'authors' in toml and toml['authors']: 
            
            # Metemos la lista en el diccionario
            datos['authors'] = julia_toml_json.crearListaAutores(toml['authors'])

        if 'compat' in toml and toml['compat']:
            datos['dependencies'] = toml['compat'] 
     
        if 'keywords' in toml and toml['keywords']:
           datos['keywords'] = toml['keywords']
       
        if 'desc' in toml and toml['desc']:
           datos['description'] = toml['desc']
           
                
                
    def liderDelTrabajo():
        
        # Sacamos la informacion del json
        toml = julia_toml_json.cargar_el_toml('./Project.toml')
        
        # La guardamos en el diccionario
        julia_toml_json.rellenar_el_diccionario(toml)
        
        return datos