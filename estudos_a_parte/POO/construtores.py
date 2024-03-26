class Evento:
    def __init__(self, nome):
        self.nome = nome
        self.local = "Brasil"

    def altera_nome_ev(self, novo_nome):
        print("Alterando nome")
        self.nome = novo_nome


ev = Evento("aula de Python")
ev2 = Evento("Aula JS")
print(ev.nome)
print(ev.local)
print(ev2.nome)
print(ev2.local)