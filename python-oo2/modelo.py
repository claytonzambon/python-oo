class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_likes(self):
        self.likes += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

friends = Serie('friends', 1995, 12)
print (f'Nome: {friends.nome} - Ano: {friends.ano} - Temporadas: {friends.temporadas} - Likes: {friends.likes}')