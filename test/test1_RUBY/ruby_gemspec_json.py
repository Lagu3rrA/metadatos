# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: jacan
"""

import os
import json


datos = {}

class ruby_gemspec_json:
    
    def cargar_el_gemspec(rutaArchivo):
            with open(rutaArchivo) as contenido:
                # Uso read porque asi  tengo todo en un string para poder usarlo como conjunto y no como lineas
                # Esto nos ayudara al hacer los autores y  la descripcion
                gemspec = contenido.read()
            return gemspec
    
    def darle_formato(gemspec):
        # Separo todo el bloque todas las lineas, para unirlas o separarlas segun necesidad
        separadoEnListasPorBarraN = gemspec.split('\n')
        return separadoEnListasPorBarraN
    
    def buscarAtributo(gemspecFormato):
        for palabra in gemspecFormato:
           
           if palabra.rfind('|') > -1:
               
               return palabra.replace("Gem::Specification.new do |", "").replace('|',"")

        return '-1'
    
    # con esto agrupamos en atributos, es decir en grupos de datos 
    def odenarEnUnaLista(loQueBuscamos,gemspecFormato):
        
        # aquie iremos guardado una a una los diferentes strings 
        listaSeparadaPorAtributos = []
        
        # cada string 
        linea = ''
        
        # comprueba si estamos en mas de una linea
        esMasDeUnaLinea = False
        
        for palabra in gemspecFormato:

        
            if(palabra):
               
                # como es mas de una linea y no empieza por el atributo 
                # concatenamos la linea con la nueva que estamos leyendo
                if esMasDeUnaLinea and palabra[2] == ' ' :
                    linea = linea + palabra
            
                # como es mas de una linea y es difentente a ' ' por 
                # tanto lo mas seguro es que sea el atributo 
                # Por ello añadimos la linea a la lista, reiniciamos la linea a '' y salimos de que
                # sea mas de una linea
                if esMasDeUnaLinea and not palabra[2] == ' ' :
                    listaSeparadaPorAtributos.append(linea)
                    linea = ''
                    esMasDeUnaLinea = False

                # como empieza por el atributo empezamos a guardar la linea
                # y entramos en que puede ser mas de una linea
                if palabra.find(loQueBuscamos) == 2:
                    linea = palabra
                    esMasDeUnaLinea = True
                    
        return listaSeparadaPorAtributos
    # crearemos un mapa con todos los datos que luego indexaremos
    def ordenarElMapa(atributo,gemspecFormato)  :
        mapaDeLosAtributos = {}
        
        # Aqui tenemos lo que esta dentro de | ... |
        loQueBuscamos = atributo + '.'
        
        # Recorremos el archivo
        listaSeparadaPorAtributos = ruby_gemspec_json.odenarEnUnaLista(loQueBuscamos,gemspecFormato)
        
        numeroDeDependecias = 0
        for atributo in listaSeparadaPorAtributos:
            atributoSeparado = atributo.split(" = ")
            
            
            # dejamos bonito la key
            atri_Sep_0 = atributoSeparado[0].replace(loQueBuscamos, "").replace("  ", "")
            
            if len(atributoSeparado) > 1:
                # dejamos bonito el value
                atri_Sep_1 = atributoSeparado[1].replace("[", "").replace("]", "").replace("%q{", "").replace("%Q{", "").replace('"', "").replace("  ", "")
            else:
                # Con esto guardamos las dependecias para usarlas posteriormente
                numeroDeDependecias = numeroDeDependecias + 1
                atri_Sep_1 = atri_Sep_0 # hacemos esto porque en un maps solo puede haber una key igual
                atri_Sep_0 = "dependecia" +  str(numeroDeDependecias)
            
            # metemos la key con el value en el mapa
            mapaDeLosAtributos[atri_Sep_0] = atri_Sep_1
            
        
        return mapaDeLosAtributos
        
    def casoAutores(mapaDeLosAtributos):
        
        listaDeAutores = []
        autor = {}
        
        if 'author' in mapaDeLosAtributos:
            autor['name']  = mapaDeLosAtributos['author']
        
        if 'email' in mapaDeLosAtributos:
            autor['email'] = mapaDeLosAtributos['email']
        
        return listaDeAutores.append(autor)
    
    def casoDependencias(mapaDeLosAtributos,listaDeDependecias):
        # Recorro el mapita buscando dependecias
        for dependecias, dps in mapaDeLosAtributos.items():
            
            # Al encontrarlas las pongo bonitas y las meto en la lista
            if dps.find("dependency") > -1:
                valorDeLaDependeciaBonito = dps.replace("add_","").replace('development_',"").replace("dependency","").replace("'","").replace(",","")
                listaDeDependecias.append(valorDeLaDependeciaBonito)
                
        return listaDeDependecias
    
    # Relleno el diccionario con la informacion de json que nos han dado
    
    def rellenar_el_diccionario(gemspecFormato):
 
        # Busco el atributo con el que en gemspec añaden la informacion esta entre |...|
        atributo = ruby_gemspec_json.buscarAtributo(gemspecFormato)
        
        # ordeno todos los demas datos en un mapa
        mapaDeLosAtributos = ruby_gemspec_json.ordenarElMapa(atributo,gemspecFormato)
        
        if 'name' in mapaDeLosAtributos:
            datos['name'] = mapaDeLosAtributos['name']

        if 'version' in mapaDeLosAtributos:
            datos['version'] = mapaDeLosAtributos['version']
        
        if 'author' in mapaDeLosAtributos:
            datos['authors'] = ruby_gemspec_json.casoAutores(mapaDeLosAtributos)
        
        if 'homepage' in mapaDeLosAtributos:
            datos['repository'] = mapaDeLosAtributos['homepage']
           
        if 'license' in mapaDeLosAtributos:
            datos['license'] = mapaDeLosAtributos['license']
        
        if 'description' in mapaDeLosAtributos:
            datos['description'] = mapaDeLosAtributos['description']
           
        listaDeDependecias = []
        if 'dependecia1' in mapaDeLosAtributos:
            
            datos['dependencies'] = ruby_gemspec_json.casoDependencias(mapaDeLosAtributos,listaDeDependecias)
            


        
    # Vuelco los datos del diccionario en un archivo json
    
    def crear_el_nuevo_json():
            
            dir = r"."
            file_name =  "ruby_metadatos.json"
            
            with open(os.path.join(dir, file_name), 'w') as file:
                json.dump(datos, file)
            
        
               
    def liderDelTrabajo(f):
        
        rutaArchivo = './' + f
        
        gemspec = ruby_gemspec_json.cargar_el_gemspec(rutaArchivo)
            
        #a = ruby_gemspec_json.darle_formato(gemspec)
            
        ruby_gemspec_json.rellenar_el_diccionario(a)
        
        ruby_gemspec_json.crear_el_nuevo_json()