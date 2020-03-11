class Pessoa:
    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if  __name__ == '__main__':
    erica = Pessoa(nome='Erica')
    alex = Pessoa(erica, nome='Alex')
    print(Pessoa.cumprimentar(erica))
    print(id(erica))
    print(erica.cumprimentar())

    print(erica.nome)
    erica.nome = 'Alexandre'
    print(erica.nome)
    print(erica.idade)
    for filho in alex.filhos:
        print(filho.nome)
    erica.sobrenome = "Galvão"
    del erica.filhos
    print(erica.__dict__)
    print(alex.__dict__)