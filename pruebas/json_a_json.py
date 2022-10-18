import os
import json

name = 'name'
version = 'version'
author = 'author'

nombreReal = ''
versionReal = ''
autorReal = ''


def cargar_el_json(ruta):
    with open(ruta) as contenido: 
        curso = json.load(contenido)
        return curso


def crear_el_nuevo_json():
        print("yes")
        data = {}
        data[name] = nombreReal
        data[version] = versionReal
        data[author] = autorReal
        
        dir = r"D:\Universidad\Univerisdad\tfg"
        file_name = "metadata.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(data, file)
        print("no")
            

for f in os.listdir(r"D:\Universidad\Univerisdad\tfg"):
    if f.startswith("prime"):
       
        ###
        ruta = r'D:\Universidad\Univerisdad\tfg\primer.json'
        jsono = cargar_el_json(ruta)
        
        if name in jsono:
            nombreReal = jsono[name]
        else: 
            nombreReal = "N\A"
        
        if version in jsono:
            versionReal = jsono[version]
        else: 
            versionReal = "N\A"
            
        if author in jsono:
            autorReal = jsono[author]
        else: 
            autorReal = "N\A"
            
        crear_el_nuevo_json()
        
        

        
        
        
        