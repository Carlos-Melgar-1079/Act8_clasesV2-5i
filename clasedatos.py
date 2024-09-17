class Informacion:
    
    def mi_lista(self):
        lista_nomperros=["boby","dollar","fany"]
        for x in lista_nomperros:
            print(x)
            
    def mi_tuplas(self):
        tupla_Razas=["chihuahuas","pug","pastor aleman"]
        for x in tupla_Razas:
            print(x)

    #diccionario
    def midicci(self):
        print("genero:")
        diccionario_py={
            "chihuahuas":"perro",
            "pug":"perra",
            "pastor aleman":"perro",
        }
        for x,y in diccionario_py.items():
            print(x,y)
#creando el objeto 

datos=Informacion()
print("listados de nombres de perros")
datos.mi_lista()
print("listados de razas de perros")
datos.mi_tuplas()
print("lista diccionario")
datos.midicci()
