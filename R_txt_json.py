# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: jacan
"""

import os
import json

datos = {}

def cargar_el_txt(ruta):
        with open(ruta) as contenido:
            txt = contenido.read()
        return txt

def darle_formato(txt):
    separadoEnListasPorBarraN = txt.split('\n')
    return separadoEnListasPorBarraN

def casoAutores(txtFormato):
    
    listaDeAutores = []
    listaAutoresDevolver = []
    
    estamosDentroDeAutores = False
    
    # COn esto juntamos todo en una lista
    for atributo  in txtFormato:
        
        # Para salirnos y no meter lineas con espacios al principio de mas salimos cuando
        # la primera letra despues de haber entrado en el if de abajo es diferente al espacio
        if estamosDentroDeAutores and not atributo[0][0] == ' ':
            break
        
        # Buscamos que la primera letra sea A o espacio 
        if (atributo[0][0] == 'A') or (atributo[0][0] == ' ' and estamosDentroDeAutores):
            estamosDentroDeAutores = True
            # Si lo es significa que estamos en los autores y lo añadimos a nuestra lista
            listaDeAutores.append(atributo)
    
    # Ahora para poder dividirlo en person tenemos que unirlo todo en un string
    stringCompleto = ' '.join(listaDeAutores)
      
    # Y ahora lo separamos por person
    autoresSeparados = stringCompleto.split('person(')
    autoresSeparados.pop(0) # con esto me quito la palabra autores de delante

    
    
    for autorito in autoresSeparados:
        
        # Corregimos el formato en el que recibimos los autores
        autorConFormato = dejarlo_con_formato(autorito)
        
        # Creamos un diccionario por autor 
        autor = {}
        
        # Y metemos el nombre
        autor['name'] = encontrar_nombre(autorConFormato)
        
        # Y el email
        autor['email'] = encontrar_email(autorConFormato)
        
        # Añadimos el autor a la lista
        listaAutoresDevolver.append(autor)
        
    return listaAutoresDevolver
    
def dejarlo_con_formato(autorito):
    
    # Vamos borrando y eliminando cosas para hacerlo accesible
    
    autorito = autorito.replace("email = ", "")
    autorito = autorito.replace("email=", "")
    autorito = autorito.replace("c(", "")
    autorito = autorito.replace(")", "")
    autorito = autorito.replace('"',"")
    listaDeValor = autorito.split(",")
    
    posicionAEliminar = 0
    for tres in listaDeValor:
        if tres.find('role') > 0:
            listaDeValor.pop(posicionAEliminar)
           
        if tres.find(".") > 0 and len(tres) < 4:
            listaDeValor.pop(posicionAEliminar)
        
        posicionAEliminar = posicionAEliminar + 1 
    
    return listaDeValor
    
def encontrar_nombre(autorConFormato):
    
    nombreAutor = autorConFormato[0] + ' ' + autorConFormato[1]
    
    return nombreAutor
    
def encontrar_email(autorConFormato):

    for valor in autorConFormato:
        if valor.find("@") > 0:
            return valor
          
    
# Relleno el diccionario con la informacion de json que nos han dado
def rellenar_el_diccionario(txtFormato):
    txtFormatoSave = txtFormato
    for qew in txtFormato:
        
        dividido = qew.split(': ',3)
        key = dividido[0]
        if(len(dividido) > 1):
            value = dividido[1]
        
        if key == 'Title':
            datos['Name'] = value
            
        if key == 'Version':
            datos['Version'] = value
            
        if key == 'URL':
            datos['Homepage'] = value
            
        if key == 'BugReports': # hay que quitarle losissues
            datos['Repository'] = value
            
        if key == 'Description': # hay que ver si entra todo
            datos['Description'] = value
        
        if key == 'License':
            datos['License'] = value
        
        if key == 'Authors@R': 
            datos['Authors'] = casoAutores(txtFormatoSave)
    

# Vuelco los datos del diccionario en un archivo json 
def crear_el_nuevo_json():
        
        dir = r"D:\Universidad\Univerisdad\tfg"
        file_name =  "R_metadatos.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(datos, file)
        
            

for f in os.listdir(r"D:\Universidad\Univerisdad\tfg"):
    if f.startswith("DESCRIPTION"):
       
        
        ruta = r'D:\Universidad\Univerisdad\tfg\DESCRIPTION.txt'
        
        txt = cargar_el_txt(ruta)
        
        a = darle_formato(txt)
        
        rellenar_el_diccionario(a)
     
        crear_el_nuevo_json()
        
        

        
        
        
        