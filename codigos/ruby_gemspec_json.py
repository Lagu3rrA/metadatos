# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: jacan
"""

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
        autor = {}
        
        if 'authors' in mapaDeLosAtributos:
            autor['name']  = mapaDeLosAtributos['authors'].replace("'", "")
        
        if 'email' in mapaDeLosAtributos:
            autor['email'] = mapaDeLosAtributos['email'].replace("'", "")
        
        listaDeAutores = [autor]
        
        return listaDeAutores
    
    def casoDependencias(mapaDeLosAtributos):
        
        mapaDeDevDependencias = {}
        mapaDeDependencias = {}
        # Recorro el mapita buscando dependecias
        for dependecias, dps in mapaDeLosAtributos.items():
            # Al encontrarlas las pongo bonitas y las meto en la lista
            if dps.find('dependency') > -1:
                valorDeLaDependeciaBonito = dps.replace("add_","").replace("dependency","").replace("'","")
                keyValue = valorDeLaDependeciaBonito.split(",",1)
                
                if dps.find('development_') > -1:
                    if len(keyValue) > 1:
                        mapaDeDevDependencias[keyValue[0].replace('development_',"")] = keyValue[1]
                    else:
                        mapaDeDevDependencias[keyValue[0].replace('development_',"")] = ""
                    continue
                    
                if len(keyValue) > 1:
                    mapaDeDependencias[keyValue[0]] = keyValue[1]
                else:
                    mapaDeDependencias[keyValue[0]] = ""
                    
        return (mapaDeDependencias,mapaDeDevDependencias)
                                    
    

    # Relleno el diccionario con la informacion de json que nos han dado
    
    def rellenar_el_diccionario(gemspecFormato):
 
        # Busco el atributo con el que en gemspec añaden la informacion esta entre |...|
        atributo = ruby_gemspec_json.buscarAtributo(gemspecFormato)
        
        # ordeno todos los demas datos en un mapa
        mapaDeLosAtributos = ruby_gemspec_json.ordenarElMapa(atributo,gemspecFormato)
        
        if 'name' in mapaDeLosAtributos and  mapaDeLosAtributos['name']:
            datos['name'] = mapaDeLosAtributos['name'].replace("'", "")
            
        if 'homepage' in mapaDeLosAtributos and  mapaDeLosAtributos['homepage']:
            datos['url'] = mapaDeLosAtributos['homepage'].replace("'", "")

        if 'version' in mapaDeLosAtributos and  mapaDeLosAtributos['version']:
            datos['version'] = mapaDeLosAtributos['version'].replace("'", "")
        
        if 'authors' in mapaDeLosAtributos and  mapaDeLosAtributos['authors']:
            
            datos['authors'] = ruby_gemspec_json.casoAutores(mapaDeLosAtributos)
        
        if 'dependecia1' in mapaDeLosAtributos and  mapaDeLosAtributos['dependecia1']:
            tuplaDeMapas = ruby_gemspec_json.casoDependencias(mapaDeLosAtributos)
            datos['dependencies'] = tuplaDeMapas[0]
            datos['dev-dependencies'] = tuplaDeMapas[1]
            
        if 'license' in mapaDeLosAtributos and  mapaDeLosAtributos['license']:
            datos['license'] = mapaDeLosAtributos['license'].replace("'", "")
        
        if 'description' in mapaDeLosAtributos and  mapaDeLosAtributos['description']:
            datos['description'] = mapaDeLosAtributos['description'].replace("'", "")
           

               
    def liderDelTrabajo(f):
        
        rutaArchivo = './' + f
        
        gemspec = ruby_gemspec_json.cargar_el_gemspec(rutaArchivo)
            
        a = ruby_gemspec_json.darle_formato(gemspec)
            
        ruby_gemspec_json.rellenar_el_diccionario(a)
        
        return datos