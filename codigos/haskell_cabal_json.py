# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: jacan
"""


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
               
            
            if 'author' in keyValueNombre and not salir:
                autorUnido['name'] = keyValueNombre['author'].replace("  ","")
                for otraPalabra in cabalSeparadoSave:
                    
                    keyValueEmail = haskell_cabal_json.dejarBonito(otraPalabra)
                    
                    if 'maintainer' in keyValueEmail and not salir:
                       autorUnido['email'] = keyValueEmail['maintainer'].replace("  ","")
                       salir = True
                       
                     
        listaDeAutoresADevolver.append(autorUnido)
        return listaDeAutoresADevolver
                
            
    def casoDependencias(cabalSeparadoSave):
        
        # donde las devolveremos 
        mapaDeDependencias = {}
        
        
        # Seguimos la misma linea que hemos realizado con los autores para juntar la descripcion en un script
        estamosDentroDeDependencias = False
        
        # Con esto juntamos todo en un mapa de dependecias
        for atributo  in cabalSeparadoSave:
            
            # Para salirnos y no meter lineas con espacios al principio de mas salimos cuando
            # la primera letra despues de haber entrado en el if de abajo es diferente al espacio
            if len(atributo) > 1  and estamosDentroDeDependencias and not atributo[3] == ' ':
                break
            
            # Buscamos que la primera letra sea b o espacio 
            if len(atributo) > 1  and ((atributo[2] == 'b' and atributo[4] == 'i') or (atributo[2] == ' ' and estamosDentroDeDependencias)):
                estamosDentroDeDependencias = True
                
                # esto saca el buil-depends de la primera dependencia 
                if atributo[2] == 'b':
                    _s_ = atributo.split(":",1)
                    atributo = _s_[1]
                
                valor = ""
                entro = False # Esto lo uso por si no hay mayor o menor solo la dependencias
                
                # Con esto elif contamplamos los casos de mayoro menor de las dependencias 
                if atributo.find('>') > -1: 
                    entro = True
                    keyValue = atributo.split(">", 1)
                    if len(keyValue) > 1:
                        valor = '>' + keyValue[1].replace('  ', "")
                    
                elif atributo.find('<') > -1: 
                    entro = True
                    keyValue = atributo.split("<", 1)
                    if len(keyValue) > 1:
                        valor = '<' + keyValue[1].replace('  ', "")

                elif atributo.find('=') > -1:
                    entro = True
                    keyValue = atributo.split("=", 1)
                    if len(keyValue) > 1:
                        valor = '=' + keyValue[1].replace('  ', "")
                if entro:
                    clave = keyValue[0].replace(',', "").replace('  ', "")
                else:
                    clave = atributo.replace(',', "").replace('  ', "")
                    
                mapaDeDependencias[clave] = valor
                
        return mapaDeDependencias             
        
    # Relleno el diccionario con la informacion de json que nos han dado
    def rellenar_el_diccionario(cabalSeparado):
        
        # Tenemos una copia para los casos que hay que recorer el caso entero
        cabalSeparadoSave = cabalSeparado
        
        
        # recorriendo el txt iterando sobre cada linea
        for palabra in cabalSeparado:
            
            keyValue = haskell_cabal_json.dejarBonito(palabra)
            
            entro = False
            
            if 'name' in keyValue and keyValue['name']:
                datos['name'] = keyValue['name'].replace("  ","")
                
            if 'homepage' in keyValue and keyValue['homepage']:
                datos['url'] = keyValue['homepage'].replace("  ","") 
                
            if 'version' in keyValue and keyValue['version']:
                datos['version'] = keyValue['version'].replace("  ","")
            
            if 'author' in keyValue and keyValue['author']:
                datos['authors'] = haskell_cabal_json.casoAutores(cabalSeparadoSave)

            if not entro and '  build-depends' in keyValue and keyValue['  build-depends']:
                datos['dependencies'] = haskell_cabal_json.casoDependencias(cabalSeparadoSave) 
                entro = True # entraba varias ces y con esto solo entra 1
            
            if 'license' in keyValue and keyValue['license']:
                datos['license'] =  keyValue['license'].replace("  ","")
             
            if 'synopsis' in keyValue and keyValue['synopsis']:
                datos['description'] =  keyValue['synopsis'].replace("  ","")
            

               
    def liderDelTrabajo(f):
                   
        rutaArchivo = './' + f
        
        cabal = haskell_cabal_json.cargar_el_txt(rutaArchivo)
        
        a = haskell_cabal_json.darle_formato(cabal)
            
        haskell_cabal_json.rellenar_el_diccionario(a)
        
        return datos
    

    
    
    
    