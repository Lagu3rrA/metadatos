# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: jacan
"""


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
        for dependencia in __l__:
            
            valor = ""
            entro = False # Esto lo uso por si no hay mayor o menor solo la dependencias
            
            if dependencia.find('>') > -1: 
                entro = True
                keyValue = dependencia.split(">", 1)
                if len(keyValue) > 1:
                    valor = '>' + keyValue[1]
                
            elif dependencia.find('<') > -1: 
                entro = True
                keyValue = dependencia.split("<", 1)
                if len(keyValue) > 1:
                    valor = '<' + keyValue[1]

            elif dependencia.find('=') > -1:
                entro = True
                keyValue = dependencia.split("=", 1)
                if len(keyValue) > 1:
                    valor = '=' + keyValue[1]
            if entro:
                clave = keyValue[0]
            else:
                clave = dependencia
                
            mapaDeDependecias[clave] = valor
            
        return mapaDeDependecias
    
    def casoKeywords(cfg):
        
        # Nos las dan todas juntas en un string y las separamos en una lista
        
        stringDeKeywords = cfg.get('metadata', 'keywords') 
        listaDeKeywords = stringDeKeywords.split(",")
        return listaDeKeywords
        
        
    # Relleno el diccionario con la informacion que nos han dado
    def rellenar_el_diccionario(cfg):

        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        
        if cfg.has_option('metadata', 'name') and cfg.get('metadata', 'name'):   
            datos['name'] =  cfg.get('metadata', 'name')
            
        if cfg.has_option('metadata', 'home-page') and cfg.get('metadata', 'home-page'):         
            datos['homepage'] =  cfg.get('metadata', 'home-page') 
        
        if cfg.has_option('metadata', 'url') and cfg.get('metadata', 'url'):         
            datos['url'] =  cfg.get('metadata', 'url')
        
        if cfg.has_option('metadata', 'version') and cfg.get('metadata', 'version'):         
            datos['version'] =  cfg.get('metadata', 'version')
            
        if cfg.has_option('metadata', 'author') and cfg.get('metadata', 'author'):         
            datos['authors'] =  python_cfg_json.crearListaAutores(cfg)
            
        if cfg.has_option('options', 'install_requires') and cfg.get('options', 'install_requires'):         
            datos['dependencies'] =  python_cfg_json.casoDependecias(cfg)
         
        if cfg.has_option('metadata', 'keywords') and cfg.get('metadata', 'keywords'):         
            datos['keywords'] =  python_cfg_json.casoKeywords(cfg) 
        
        if cfg.has_option('metadata', 'license') and cfg.get('metadata', 'license'):         
            datos['license'] =  cfg.get('metadata', 'license') 

        if cfg.has_option('metadata', 'description') and cfg.get('metadata', 'description'):         
            datos['description'] =  cfg.get('metadata', 'description') 
            
                
    def liderDelTrabajo():
        
        # Sacamos la informacion del json
        cfg = python_cfg_json.cargar_el_cfg('./setup.cfg')

        # La guardamos en el diccionario
        python_cfg_json.rellenar_el_diccionario(cfg)

        return datos
            