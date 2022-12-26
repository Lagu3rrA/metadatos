# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:37:21 2022

@author: jacan
"""


datos = {}


class python_py_json:
    
    def cargar_el_py(rutaArchivo):
        with open(rutaArchivo) as contenido:
            # Uso read porque asi  tengo todo en un string para poder usarlo como conjunto y no como lineas
            # Esto nos ayudara al hacer los autores y  la descripcion
            py = contenido.read()
        return py
        
    
    def darle_formato(py):
        # Separo todo el bloque todas las lineas, para unirlas o separarlas segun necesidad
        separadoEnListasPorBarraN = py.split('\n')
        return separadoEnListasPorBarraN
    
    def cojerSoloSetup(pyFormato):
        informacionDividida = pyFormato.split('setup(')
        return informacionDividida[1]
    
    # con esto agrupamos en atributos, es decir en grupos de datos 
    def odenarEnUnaLista(PYseparadoEnLineas):
        
        
        # aquie iremos guardado una a una los diferentes strings 
        listaSeparadaPorAtributos = []
        
        # cada string 
        linea = ''
        
        # comprueba si estamos en mas de una linea
        esMasDeUnaLinea = False
        
        for palabra in PYseparadoEnLineas:

        
            if len(palabra) > 3 :
                # como es mas de una linea y no empieza por el atributo 
                # concatenamos la linea con la nueva que estamos leyendo
                if esMasDeUnaLinea and palabra[4] == ' ' or palabra[4] == "]" or palabra[4] == ")"or palabra[4] == "}":
                    linea = linea + palabra
            
                # como es mas de una linea y es difentente a ' ' por 
                # tanto lo mas seguro es que sea el atributo 
                # Por ello añadimos la linea a la lista, reiniciamos la linea a '' y salimos de que
                # sea mas de una linea
                if esMasDeUnaLinea and not palabra[4] == ' ' and not palabra[4] == "]" and not palabra[4] == ")" and not palabra[4] == "}":
                    listaSeparadaPorAtributos.append(linea)
                    linea = ''
                    esMasDeUnaLinea = False

               
                if not palabra[4] == ' ' and not palabra[4] == "]" and not palabra[4] == ")" and not palabra[4] == "}":
                    linea = palabra
                    esMasDeUnaLinea = True
                    
            if palabra and palabra[0] == ')':
                listaSeparadaPorAtributos.append(linea)
                linea = ''
                esMasDeUnaLinea = False
                

        return listaSeparadaPorAtributos
    
    # crearemos un mapa con todos los datos que luego indexaremos
    def ordenarElMapa(PYseparadoEnLineas)  :
        
        mapaDeLosAtributos = {}
        
        
        # Recorremos el archivo
        listaSeparadaPorAtributos = python_py_json.odenarEnUnaLista(PYseparadoEnLineas)
        
        
       
        for atributo in listaSeparadaPorAtributos:
            atributoSeparado = atributo.split("=",1)
            
            
            # dejamos bonito la key
            atri_Sep_0 = atributoSeparado[0].replace("    ", "")
            
            if len(atributoSeparado) > 1:
                # dejamos bonito el value
                atri_Sep_1 = atributoSeparado[1].replace("[", "").replace("]", "").replace("'", "").replace('"', "").replace("    ", "")
            
            # metemos la key con el value en el mapa
            mapaDeLosAtributos[atri_Sep_0] = atri_Sep_1
            
        
        return mapaDeLosAtributos
        
    def casoAutores(mapaDeLosAtributos):
        
        listaDeAutores = []
        autor = {}
        
        if 'author' in mapaDeLosAtributos:
            autor['name']  = mapaDeLosAtributos['author'].replace(",", "")
        
        if 'author_email' in mapaDeLosAtributos:
            autor['email'] = mapaDeLosAtributos['author_email'].replace(",", "")

        listaDeAutores.append(autor)
        return listaDeAutores
    
    def casoDependencias(valorDeLasDependecias):

        # Las separamos por la coma 
        listaDeDependecias = valorDeLasDependecias.split(',')
        
        # Quitamos el ultimo espacio porque no contiene nada
        listaDeDependecias.pop(len(listaDeDependecias)-1)
        
        # Las metemos en el mapa que depues devolveremos 
        mapaDeDependecias = {}
        
        for dependencia in listaDeDependecias:
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
    
    # Relleno el diccionario con la informacion de json que nos han dado
    
    def rellenar_el_diccionario(pyFormato):
 
        # quito lo primero, antes del setup( , porque no nos interesa
        PYsoloLoImportante = python_py_json.cojerSoloSetup(pyFormato)
        
        # lo separo en lineas para utilizarlo
        PYseparadoEnLineas= python_py_json.darle_formato(PYsoloLoImportante)

        # ordeno todos los demas datos en un mapa
        mapaDeLosAtributos = python_py_json.ordenarElMapa(PYseparadoEnLineas)
        
        
        
        if 'name' in mapaDeLosAtributos and mapaDeLosAtributos['name']:
            datos['name'] = mapaDeLosAtributos['name'].replace(",", "")
            
        if 'url' in mapaDeLosAtributos and mapaDeLosAtributos['url']:
            datos['url'] = mapaDeLosAtributos['url'].replace(",", "")

        if 'version' in mapaDeLosAtributos and mapaDeLosAtributos['version']:
            datos['version'] = mapaDeLosAtributos['version'].replace(",", "")
        
        if 'author' in mapaDeLosAtributos and mapaDeLosAtributos['author']:
            datos['authors'] = python_py_json.casoAutores(mapaDeLosAtributos)
            
        if 'install_requires' in mapaDeLosAtributos and mapaDeLosAtributos['install_requires']:
            datos['dependencies'] = python_py_json.casoDependencias(mapaDeLosAtributos['install_requires'])
           
        if 'license' in mapaDeLosAtributos and mapaDeLosAtributos['license']:
            datos['license'] = mapaDeLosAtributos['license'].replace(",", "")
        
        if 'description' in mapaDeLosAtributos and mapaDeLosAtributos['description']:
            datos['description'] = mapaDeLosAtributos['description']
           
    
    def liderDelTrabajo():
        
        py = python_py_json.cargar_el_py('./setup.py')
        python_py_json.rellenar_el_diccionario(py)
        
        return datos 