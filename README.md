TFG -Trabajo de Fin De Grado
============================

Con este trabajo el objetivo era poder unificar la manera en que, en diferentes proyectos en diferentes lenguajes se guardan los metadatos de dicho proyectos. 
El codigo parse cada una de las extensiones en donde los lenguajes los depositan y los va guardando en una lista que posteriormente exporta a un archivo JSON. 
Aqui es donde se podran ver todos los archivos de metadatos  encontrados y su información. 

Como ejecutarlo
---------------

Para poder ejecutarlo necesitas  copiar todos los archivos que hay  dentro de la carpeta códigos en tu proyecto y ejecutar

`python master.py`

Te preguntara como quieres que se llame el archivo y posteriormente se guardara en el mismo directorio que guardaste el master.


Organizacion de las carpetas 
----------------------------

  - `archivosJsonDevueltos`
  
      En esta carpeta encontramos un archivo donde podemos ver como se devuelven en un archivo toda la informacion que ha encontrado.
      Ademas tabien hay  un "Ejemplo.json" que es el formato en el que todos los archivos estan siendo devueltos.
  
  - `codigos`
  
      Aquí encontramos todos los diferentes códigos y el master, que es desde el que se ejecutan todos.
  
  - `test`
  
      Hay una carpeta archivos donde estan los archivos de ejemplo de los metadatos de lo lenguajes, los tenemos aqui para cuando se hagan los 
      test, se les llame desde aqui y esten todos juntos.
      Aparte encontramos todos los test correspondietes a las distintas clase que tenemos.
    
