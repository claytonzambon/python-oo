class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
print(vingadores.nome)

friends = Serie('Friends', 1995, 12)
print (f'Nome: {friends.nome} - Ano: {friends.ano} - Temporadas: {friends.temporadas}')