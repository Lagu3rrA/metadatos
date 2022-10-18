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
            # Uso read porque asi  tengo todo en un string para poder usarlo como conjunto y no como lineas
            # Esto nos ayudara al hacer los autores y  la descripcion
            txt = contenido.read()
        return txt

def darle_formato(txt):
    # Separo todo el bloque todas las lineas, para unirlas o separarlas segun necesidad
    separadoEnListasPorBarraN = txt.split('\n')
    return separadoEnListasPorBarraN

def casoAutores(txtFormato):
    
    # Esta la usaremos como borrador para meter los datos en sucio
    listaDeAutores = []
    
    # Esta lista sera la ultima que devolvamos con todo bonito y bien unido
    listaAutoresDevolver = []
    
    # Controlamos que no coja mas de una linea que comiencen por espacio
    estamosDentroDeAutores = False
    
    # Con esto juntamos todo en una lista
    for atributo  in txtFormato:
        
        # Para salirnos y no meter lineas con espacios al principio de mas, salimos cuando
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
    
    # Juntamos el nombre y el apellido en un mismo string
    nombreAutor = autorConFormato[0] + autorConFormato[1]
    
    return nombreAutor
    
def encontrar_email(autorConFormato):

    # Iteramos sobre los  datos que tenemos del autor que nos pasan
    # y si encontramos algun elemento con la @ significa que es el mail
    for valor in autorConFormato:
        if valor.find("@") > 0:
            return valor
          
    
# Relleno el diccionario con la informacion de json que nos han dado
def rellenar_el_diccionario(txtFormato):
    
    # Tenemos una copia para los casos que hay que recorer el caso entero
    txtFormatoSave = txtFormato
    
    # recorriendo el txt iterando sobre cada linea
    for palabra in txtFormato:
        
        # Como tiene un formato parecido a clave valor lo separamos por : y guardamos la key y el value
        dividido = palabra.split(': ',3)
        key = dividido[0]
        if(len(dividido) > 1):
            value = dividido[1]
        
        # Vamos rellenado  el diccionario con los datos 
        
        if key == 'Title':
            datos['Name'] = value
            
        if key == 'Version':
            datos['Version'] = value
            
        if key == 'URL':
            datos['Homepage'] = value
            
        if key == 'BugReports': # usamos el de los issues pero le quitamso el directorio issues
            datos['Repository'] = casoRepositor(value)
            
        if key == 'Description': # si la descripcion esta en mas de una linea esto resuelve ese problema
            datos['Description'] = casoDescripcion(txtFormatoSave)
        
        if key == 'License':
            datos['License'] = value
        
        if key == 'Authors@R': # organiza el formato para que salga nombre y mail
            datos['Authors'] = casoAutores(txtFormatoSave)
    
def casoDescripcion(txtFormato):
    
    # Union en una lista de toda la descripcion
    descripcionEntera = []
    
    
    # Seguimos la misma linea que hemos realizado con los autores para juntar la descripcion en un script
    estamosDentroDeDescripcion = False
    
    # Con esto juntamos todo en una lista
    for atributo  in txtFormato:
        
        # Para salirnos y no meter lineas con espacios al principio de mas salimos cuando
        # la primera letra despues de haber entrado en el if de abajo es diferente al espacio
        if estamosDentroDeDescripcion and not atributo[0][0] == ' ':
            break
        
        # Buscamos que la primera letra sea D o espacio 
        if (atributo[0][0] == 'D') or (atributo[0][0] == ' ' and estamosDentroDeDescripcion):
            estamosDentroDeDescripcion = True
            
            # Si lo es significa que estamos en los autores y lo añadimos a nuestra lista
            descripcionEntera.append(atributo)
    
    
    stringCompleto = ''.join(descripcionEntera)
    
    # Lo junto, lo separaro para quitar descripcion y lo vuelvo unir para devolverlo
    dos = stringCompleto.split(':')
    dos.pop(0)
    
    return ''.join(dos)
    
def casoRepositor(valor):
    
    # Lo separo por / y quito la ultima que es la que esta el issue
    realRepositorio = valor.split('/')
    realRepositorio.pop(len(realRepositorio)-1)
    
    # lo vuelve a jutnar con / entre los huecos 
    return '/'.join(realRepositorio)
    
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
        
        

        
        
        
        