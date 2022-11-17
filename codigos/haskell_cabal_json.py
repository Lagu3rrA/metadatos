# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: jacan
"""

import os
import json


datos = {}

class haskell_cabal_json:

    def cargar_el_txt(ruta):
            with open(ruta) as contenido:
                # Uso read porque asi  tengo todo en un string para poder usarlo como conjunto y no como lineas
                # Esto nos ayudara al hacer los autores y  la descripcion
                cabal = contenido.read()
            return cabal
    
    def darle_formato(txt):
        # Separo todo el bloque todas las lineas, para unirlas o separarlas segun necesidad
        separadoEnListasPorBarraN = txt.split('\n')
        return separadoEnListasPorBarraN
    
    def dejarBonito(palabra):
        mapitaADevolver = {}
        if palabra.find(': ') > -1:
            dividido = palabra.split(': ')
            key = dividido[0]
            if(len(dividido) > 1):
                value = dividido[1]
            mapitaADevolver[key] = value
            
        else:
            mapitaADevolver['key'] = palabra
            
    
        return mapitaADevolver
    
    def casoAutores(cabalSeparadoSave):
        listaDeAutoresADevolver = []
        autorUnido = {}
        
        salir = False
        
        for palabra in cabalSeparadoSave:
            
            
            # Como tiene un formato parecido a clave valor lo separamos por : y guardamos la key y el value
            keyValueNombre = haskell_cabal_json.dejarBonito(palabra)
               
            
            if 'name' in keyValueNombre and not salir:
                autorUnido['name'] = keyValueNombre['name']
                
                for otraPalabra in cabalSeparadoSave:
                    
                    keyValueEmail = haskell_cabal_json.dejarBonito(otraPalabra)
                    
                    if 'maintainer' in keyValueEmail and not salir:
                       autorUnido['email'] = keyValueEmail['maintainer']
                       salir = True
                       
                     
        listaDeAutoresADevolver.append(autorUnido)
        return listaDeAutoresADevolver
                
            
              
        
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(cabalSeparado):
        
        # Tenemos una copia para los casos que hay que recorer el caso entero
        cabalSeparadoSave = cabalSeparado
        
        
        # recorriendo el txt iterando sobre cada linea
        for palabra in cabalSeparado:
            
            keyValue = haskell_cabal_json.dejarBonito(palabra)
            
            if 'name' in keyValue:
                datos['name'] = keyValue['name']
            
            if 'version' in keyValue:
                datos['version'] = keyValue['version']
                
            if 'homepage' in keyValue:
                datos['homepage'] = keyValue['homepage']
            
            if 'license' in keyValue:
                datos['license'] =  keyValue['license']
            
            if 'author' in keyValue:
                datos['authors'] = haskell_cabal_json.casoAutores(cabalSeparadoSave)
                
            if 'synopsis' in keyValue:
                datos['description'] =  keyValue['synopsis']
            

        
        
        
   
        
    # Vuelco los datos del diccionario en un archivo json
    def crear_el_nuevo_json():
            
        dir = r"."
        file_name =  "R_metadatos.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file)
            
        
               
    def liderDelTrabajo(f):
                   
        rutaArchivo = './' + f
        
        cabal = haskell_cabal_json.cargar_el_txt(rutaArchivo)
        
        a = haskell_cabal_json.darle_formato(cabal)
            
        haskell_cabal_json.rellenar_el_diccionario(a)
        
        print(datos)
        
        #haskell_cabal_json.crear_el_nuevo_json()
            
    

    
    
    
    