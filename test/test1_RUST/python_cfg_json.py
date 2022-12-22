# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: jacan
"""
import os
import json
import configparser

# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class python_cfg_json:

    
    # Cargo en una varible el json de informacion del proyecto
    def cargar_el_cfg(ruta):
        cfg = configparser.ConfigParser()
        cfg.read_file(open(ruta))
        return cfg

    def crearListaAutores(cfg):
        
        listaDeAutores = []
        autor = {}
        
        autor['name'] = cfg.get('metadata', 'author')
        
        if (cfg.get('metadata', 'author_email')):
            autor['email'] = cfg.get('metadata', 'author_email')
        
        listaDeAutores.append(autor)
        
        return listaDeAutores

    def casoDependecias(cfg):
        
        mapaDeDependecias = {}
        listaNoOrdenada = cfg.get('options', 'install_requires')
        
        __l__ = listaNoOrdenada.split('\n')
        
        __l__.pop(0)
        for dependecia in __l__:
            
            keyValue = dependecia.split(" ", 1)
            valor = ""
            clave = keyValue[0]
            
            if len(keyValue) > 1:
                valor = keyValue[1]
                
            mapaDeDependecias[clave] = valor
        
        return mapaDeDependecias
        
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(cfg):
        
        # Es asi de facil sacar los datos del json 
        
        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        
        if cfg.get('metadata', 'name'):         
            datos['name'] =  cfg.get('metadata', 'name')
        
        if cfg.get('metadata', 'version'):         
            datos['version'] =  cfg.get('metadata', 'version')
            
        if cfg.get('metadata', 'author'):         
            datos['authors'] =  python_cfg_json.crearListaAutores(cfg)
        
        if cfg.get('metadata', 'description'):         
            datos['description'] =  cfg.get('metadata', 'description')
        
        if cfg.get('metadata', 'url'):         
            datos['url'] =  cfg.get('metadata', 'url')
            
        if cfg.get('options', 'install_requires'):         
            datos['dependencies'] =  python_cfg_json.casoDependecias(cfg)
            
   
    
    # Vuelco los datos del diccionario en un archivo json 
    def crear_el_nuevo_json():

        dir = r"."
        file_name =  "python_cfg_metadatos.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file) 
                
                
    def liderDelTrabajo():
        
        # Sacamos la informacion del json
        cfg = python_cfg_json.cargar_el_cfg('./setup.cfg')

        # La guardamos en el diccionario
        python_cfg_json.rellenar_el_diccionario(cfg)
        
        # Creamos el archivo que vamos a devolver
        python_cfg_json.crear_el_nuevo_json()
            