class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
friends = Serie('friends', 1995, 12)
carros = Filme('Carros', 2010, 120)
seinfield = Serie('Seinfield', 1990, 10)

vingadores.dar_like()
carros.dar_like()
carros.dar_like()
carros.dar_like()
carros.dar_like()
seinfield.dar_like()
seinfield.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()

filmes_e_series = [vingadores, friends, seinfield, carros]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tá ou não tá? {friends in playlist_fim_de_semana}')