class Evento:
    def __init__(self, nome, local =""):
        self.nome = nome
        self.local = local

    def imprime_informacoes(self):    
        print("Nome do evento", self.nome)
        print("Local do evento", self.local)

    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local= "https://tamarcado.com.eventos?id=1")
        return evento
    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if area >=5 and area <10: # 5<= area <10
            return 5
        elif area >= 10 and area <20: 
           return 15
        elif area >= 20:
            return 30
        else:
            return 0

ev = Evento ("Aula Py")
ev2 = Evento("Aula jS", "DF")

ev.imprime_informacoes()
ev2.imprime_informacoes()

ev_online = Evento.cria_evento_online("Live coding Python")
ev_online.imprime_informacoes()

print(Evento.calcula_limite_pessoas_area(5))