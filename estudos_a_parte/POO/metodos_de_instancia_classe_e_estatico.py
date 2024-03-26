class Evento:
    def metodo_instancia(self):
        return("metodo de instancia chamado ", self)
    #metodo de class
    @classmethod
    def metodo_classe(cls):
        return ("metodo de classe chamado ", cls)
    @staticmethod
    def metodo_estatico():
        return "estatico metodo"

ev = Evento()
a = ev.metodo_instancia()
print(a)


b = Evento.metodo_classe()
print(b)

c = Evento.metodo_estatico()
print(c)