class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
print(vingadores.nome)