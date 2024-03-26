class Evento:
    #novo
    #variavel de class
    id = 1

    def __init__(self, nome, local =""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id +=1

    def imprime_informacoes(self):    
        print("Id do evento:", self.id)
        print("Nome do evento", self.nome)
        print("Local do evento", self.local)
        print("----------------------")

    @classmethod
    def cria_evento_online(cls, nome):
        #uso do f-string
        evento = cls(nome, local= f"https://tamarcado.com.eventos?id={cls.id}")
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

ev_online = Evento.cria_evento_online("Live coding Python")
ev_online2 = Evento.cria_evento_online("Live coding Java")

ev_online.imprime_informacoes()
ev_online2.imprime_informacoes()

print(ev_online.id)
print(ev_online2.id)
print(Evento.id)