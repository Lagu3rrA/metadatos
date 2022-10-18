# -*- coding: utf-8 -*-
import os
import json
import xml.etree.cElementTree as ET 


groupID = ''
versionReal = ''
urlReal = ''




def cargar_el_xml(ruta):
        tree = ET.ElementTree(file = 'equisml.xml')
        return tree.getroot()
        print("yes")


def crear_el_nuevo_json():
        print("yes")
        data = {}
        data['groupID'] = groupID
        data['version'] = versionReal
        data['url'] = urlReal
        
        dir = r"D:\Universidad\Univerisdad\tfg"
        file_name = "metadata2.json"
        
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(data, file)
        print("no")
            

for f in os.listdir(r"D:\Universidad\Univerisdad\tfg"):
    if f.startswith("equis"):
       
        ###
        ruta = r'D:\Universidad\Univerisdad\tfg\equisml.xml'
        root = cargar_el_xml(ruta)
        print(root)
      
        for datos in root:
            if datos.tag.endswith('modelVersion'):
                versionReal = datos.text 
                print(versionReal)
            
            if datos.tag.endswith('groupId'):
                groupID = datos.text 
                print(groupID)
                
            if datos.tag.endswith('url'):
                urlReal = datos.text 
                print(urlReal)
        
        crear_el_nuevo_json()
                
        
       

        
        
        
        