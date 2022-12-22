# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:45:06 2022

@author: Lagu3rrA
"""

import unittest
import os 

#import sys 
#sys.path.insert(1, './tfg/codigos')
from java_xml_json import *

class Test_1_java(unittest.TestCase):
    
    # -----------------------------------------------
    # Este test comprueba que todo este bien devuelto 
    # -----------------------------------------------
    
    
    # Creamos el ambiente con el archivo bueno y cosas al rededor simulando un proyecto
    def setUpClass():
      
        os.makedirs('pom')
        os.makedirs('xml')
        os.makedirs('pomxml')
        
        file = open("./pom.xml", "w") # ESTE ES EL BUENO bower.json
        file.write('<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"><modelVersion>4.0.0</modelVersion><artifactId>client-java-parent</artifactId><groupId>io.kubernetes</groupId><version>18.0.0-SNAPSHOT</version><packaging>pom</packaging><name>Kubernetes Client API</name><url>https://github.com/kubernetes-client/java</url><description>Kubernetes Client Library</description><scm><connection>scm:git:git@github.com:kubernetes-client/java.git</connection><developerConnection>scm:git:git@github.com:kubernetes-client/java.git</developerConnection><url>https://github.com/kubernetes-client/java</url><tag>HEAD</tag></scm><licenses><license><name>The Apache Software License, Version 2.0</name><url>http://www.apache.org/licenses/LICENSE-2.0.txt</url><distribution>repo</distribution></license></licenses><developers><developer><name>The Kubernetes Authors</name><email>kubernetes-dev@googlegroups.com</email><organization>Kubernetes</organization><organizationUrl>https://kubernetes.io</organizationUrl></developer></developers><dependencyManagement><dependencies><dependency><groupId>org.apache.commons</groupId><artifactId>commons-lang3</artifactId><version>${apache.commons.lang3.version}</version></dependency><dependency><groupId>org.apache.commons</groupId><artifactId>commons-collections4</artifactId><version>${apache.commons.collections4.version}</version></dependency><dependency><groupId>org.yaml</groupId><artifactId>snakeyaml</artifactId><version>${snakeyaml.version}</version></dependency><dependency><groupId>commons-codec</groupId><artifactId>commons-codec</artifactId><version>${common.codec.version}</version></dependency><dependency><groupId>org.apache.commons</groupId><artifactId>commons-compress</artifactId><version>${apache.commons.compress}</version></dependency><dependency><groupId>commons-io</groupId><artifactId>commons-io</artifactId><version>${apache.commons.io}</version></dependency><dependency><groupId>com.github.ben-manes.caffeine</groupId><artifactId>caffeine</artifactId><version>${caffeine.version}</version></dependency><dependency><groupId>org.slf4j</groupId><artifactId>slf4j-api</artifactId><version>${slf4j.version}</version></dependency><dependency><groupId>org.bouncycastle</groupId><artifactId>bcpkix-jdk18on</artifactId><version>${bouncycastle.version}</version></dependency><dependency><groupId>com.microsoft.azure</groupId><artifactId>adal4j</artifactId><version>1.6.7</version><optional>true</optional></dependency></dependencies></dependencyManagement></profile><profile><id>fluent-gen</id><modules><module>fluent-gen</module></modules></profile></profiles></project>')
        file.close()
        
        file = open("./pom.txt", "w")
        file.write('no')
        file.close()
        file = open("./xml.xml", "w")
        file.write('no')
        file.close()
        file = open("./java.xml", "w")
        file.write('no')
        file.close()

    # Borramos lo que habiamos creado para que quede bonito
    def tearDownClass():


        os.rmdir("pom")
        os.rmdir("xml")
        os.rmdir("pomxml")
        
        os.remove("pom.txt")
        os.remove("xml.xml")
        os.remove("java.xml")
        os.remove("pom.xml")
         
        
    # Como vamos a estar llamando todo el rato en cada uno de los test al main
    # de la clase lo hacemos aqui, a si hay menos codigo repetido    
    def setUp(self):
        self.datos =  java_xml_json.liderDelTrabajo()

    def test_nombre(self):
        self.assertEqual(self.datos['name'],'Kubernetes Client API')
    
    def test_paginaweb(self):
        self.assertEqual(self.datos['homepage'],'https://github.com/kubernetes-client/java')
    
    def test_url(self):
        self.assertEqual(self.datos['url'],'https://github.com/kubernetes-client/java')
        
    def test_version(self):
        self.assertEqual(self.datos['version'],'18.0.0-SNAPSHOT')
        
    def test_authors(self):
        self.assertEqual(self.datos['authors'][0]['name'], 'The Kubernetes Authors')
        
    def test_email(self):
        self.assertEqual(self.datos['authors'][0]['email'], 'kubernetes-dev@googlegroups.com')
    
    def test_require(self):
        self.assertEqual(self.datos['dependencies']['commons-lang3'], '${apache.commons.lang3.version}')
        self.assertEqual(self.datos['dependencies']['commons-collections4'], '${apache.commons.collections4.version}')
        self.assertEqual(self.datos['dependencies']['snakeyaml'], '${snakeyaml.version}')
        self.assertEqual(self.datos['dependencies']['commons-codec'], '${common.codec.version}')
        self.assertEqual(self.datos['dependencies']['commons-compress'], '${apache.commons.compress}')
        self.assertEqual(self.datos['dependencies']['commons-io'], '${apache.commons.io}')
    
    def test_license(self):  
         self.assertEqual(self.datos['license'], 'The Apache Software License, Version 2.0') 
         
    def test_descripcion(self):
        self.assertEqual(self.datos['description'],'Kubernetes Client Library')
        
        
if __name__ == '__main__':
    unittest.main()