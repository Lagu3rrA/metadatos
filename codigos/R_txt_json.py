# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:36:35 2022

@author: Lagu3rrA
"""


datos = {}

class R_txt_json:

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
        #Para entender mejor este metodo ver al mismo tiempo un ejemplo de documetacion de lo autores en R
        
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
            autorConFormato = R_txt_json.dejarlo_con_formato(autorito)
            
            # Creamos un diccionario por autor 
            autor = {}
            
            # Y metemos el nombre
            nombre = R_txt_json.encontrar_nombre(autorConFormato)
            if nombre:
                autor['name'] = nombre
            
            # Y el email
            email = R_txt_json.encontrar_email(autorConFormato)
            if email:
                autor['email'] = R_txt_json.encontrar_email(autorConFormato)
            
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
            
     
    def casoDescripcion(txtFormato):
        
        # Union en una lista de toda la descripcion
        descripcionEntera = []
        
        
        # Seguimos la misma linea que hemos realizado con los autores para juntar la descripcion en un script
        estamosDentroDeDescripcion = False
        
        # Con esto juntamos todo en una lista
        for atributo  in txtFormato:
            
            # Para salirnos y no meter lineas con espacios al principio de mas salimos cuando
            # la primera letra despues de haber entrado en el if de abajo es diferente al espacio
            if estamosDentroDeDescripcion and not atributo[0] == ' ':
                break
            
            # Buscamos que la primera letra sea D o espacio 
            if (atributo[0] == 'D' and atributo[2] == 's') or (atributo[0] == ' ' and estamosDentroDeDescripcion):
                estamosDentroDeDescripcion = True
                
                # Si lo es significa que estamos en los autores y lo añadimos a nuestra lista
                descripcionEntera.append(atributo)
        
        
        stringCompleto = ''.join(descripcionEntera)
        
        # Lo junto, lo separaro para quitar descripcion y lo vuelvo unir para devolverlo
        dos = stringCompleto.split(':')
        dos.pop(0)
        
        return ''.join(dos)
    
    def casoDependencias(txtFormato):
        mapaDeDependecias = {}
        
        
        estamosDentroDeImport = False
        
        # Con esto juntamos todo en una lista
        for atributo  in txtFormato:
            
            # Para salirnos y no meter lineas con espacios al principio de mas salimos cuando
            # la primera letra despues de haber entrado en el if de abajo es diferente al espacio
            if estamosDentroDeImport and not atributo[0] == ' ':
                break
            
            # Aqui estamos dentro del import
            if (atributo[0] == 'I' and atributo[2] == 'p') or (atributo[0] == ' ' and estamosDentroDeImport):
                
                estamosDentroDeImport = True
                # Hacemos este if para sacar al 'Import:' del mapa 
                if atributo[0] == ' ':
                    
                    # despues limpiamos y lo  metemos con el formatro elegido 
                    valor = ""
                    clave = atributo
                    
                    if atributo.find('(') > -1: 
                        
                        keyValue = atributo.split("(", 1)
                        valor = keyValue[1].replace(')','').replace(',','')
                        clave = keyValue[0].replace(' ','')
                    
                    mapaDeDependecias[clave] = valor
                
        return mapaDeDependecias
                
                
    def casoRepositor(valor):
        
        # Lo separo por / y quito la ultima que es la que esta el issue
        realRepositorio = valor.split('/')
        realRepositorio.pop(len(realRepositorio)-1)
        
        # lo vuelve a jutnar con / entre los huecos 
        return '/'.join(realRepositorio)
              
        
    # Relleno el diccionario con la informacion de txt que nos han dado
    def rellenar_el_diccionario(txtFormato):
        
        # Tenemos una copia para los casos que hay que recorer el caso entero
        txtFormatoSave = txtFormato
        
        # recorriendo el txt iterando sobre cada linea
        for palabra in txtFormato:
            # Como tiene un formato parecido a clave valor lo separamos por : y guardamos la key y el value
            dividido = palabra.split(':',1)
            key = dividido[0]
            if(len(dividido) > 1):
                value = dividido[1]
            
            # Vamos rellenado  el diccionario con los datos 
            if key == 'Title' and value:
                datos['name'] = value
                
            if key == 'URL' and value:
                datos['homepage'] = value
                
            if key == 'BugReports' and value: # usamos el de los issues pero le quitamso el directorio issues
                datos['url'] = R_txt_json.casoRepositor(value)
                
            if key == 'Version' and value:
                datos['version'] = value
                
            if key == 'Authors@R' and value: # organiza el formato para que salga nombre y mail
                datos['authors'] = R_txt_json.casoAutores(txtFormatoSave)
                
            if key == 'Imports' and value:
                datos['dependencies'] = R_txt_json.casoDependencias(txtFormatoSave)
                       
            if key == 'License' and value:
                datos['license'] = value   
                
            if key == 'Description' and value: # si la descripcion esta en mas de una linea esto resuelve ese problema
                datos['description'] = R_txt_json.casoDescripcion(txtFormatoSave)
            
            
        
    def liderDelTrabajo():
            txt = R_txt_json.cargar_el_txt("./DESCRIPTION.txt")
                
            a = R_txt_json.darle_formato(txt)
                
            R_txt_json.rellenar_el_diccionario(a)
            
            return datos
            
    

    
    
    
    