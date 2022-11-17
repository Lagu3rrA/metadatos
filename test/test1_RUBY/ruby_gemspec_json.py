from gemfileparse import GemfileParser

parser = GemfileParser('./nombre.gemspec','diaspora')

deps = parser.parse()

for key in deps:
   if deps[key]:
       print (key)
       for dependency in deps[key]:
           print("\t", dependency)