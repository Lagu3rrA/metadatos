# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: Lagu3rrA
"""

import json


# Creo el diccionario en el que voy a meter la informacion
datos = {}

 
class javascript_json_json:
    
    
    # Cargo en una varible el json de informacion del proyecto
    #def cargar_el_json(ruta):
    def cargar_el_json(ruta):
        with open('./package.json','r') as contenido: 
            curso = json.load(contenido)
            return curso
              
    
    def casoAutores(jsono):
        autor = {}
        listaDeAutores = []
        
        if 'maintainers' in jsono:
            a = jsono['maintainers'][0]
            listaDeAutores.append(a)
            return listaDeAutores
        
        if 'author' in jsono:
            autorEntero = jsono['author']
            autorito = autorEntero.split('<')
            autor['name'] = autorito[0]
            if len(autorito)>0:
                autor['email'] = autorito[1].replace(">","")
            listaDeAutores.append(autor)
            return listaDeAutores
        
        return listaDeAutores


    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(jsono):
        
        # Es asi de facil sacar los datos del json 
        
        # Preguntamos si esta donde hemos volcado los datos 
        # y si encuentra una key igual la copiamos junto al valor
        # en nuestro diccionario
        
     
        if 'name' in jsono and jsono['name']: 
            datos['name'] = jsono['name']
            
        if 'homepage' in jsono and jsono['homepage']: 
            datos['homepage'] = jsono['homepage'] 
        
        if 'repository' in jsono and jsono['repository']['url']: 
            datos['url'] = jsono['repository']['url'].replace("git+","")
            
        if 'version' in jsono and jsono['version']: 
            datos['version'] = jsono['version'] 
        
        if 'author' in jsono and jsono['author']: 
            datos['authors'] = javascript_json_json.casoAutores(jsono)
        
        if 'dependencies' in jsono and jsono['dependencies']:
            datos['dependencies'] = jsono['dependencies']
            
        if 'devDependencies' in jsono and jsono['devDependencies']:
            datos['dev-dependencies'] = jsono['devDependencies']
        
        if 'keywords' in jsono and jsono['keywords']: 
            datos['keywords'] = jsono['keywords']
            
        if 'license' in jsono and jsono['license']: 
            datos['license'] = jsono['license']
            
        if 'description' in jsono and jsono['description']: 
            datos['description'] = jsono['description']   
        

    def liderDelTrabajo():#ruta
        
        # Sacamos la informacion del json
        jsono = javascript_json_json.cargar_el_json('./package.json')
        
        # La guardamos en el diccionario
        javascript_json_json.rellenar_el_diccionario(jsono)

        return datos
