print("clases version 2 el contructor")

class perro:
    #funcion contructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    #funciones creadas por el usuario 
    def morder(self):
        print("chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
    def chatperra(self,mensajepe):
        print(f"chat perro:{mensajepe}") 
    def datos(self):
        print(f"color  {self.color} edad {self.edad}")
#crear el objeto
chihuas=perro("Negro",2)
#llamadas a funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("hola canina")
chihuas.chatperra("quieres ser mi gugguu")
chihuas.chatperro("gruu..... ")