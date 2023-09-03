# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7s do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

# @dataclass(frozen=True, repr=False)
# @dataclass(order=True)
# @dataclass()
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
  
    def __post_init__(self):
        print('POST INIT')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome }'
    
    @nome_completo.setter
    def nome_completo(self, valor: str):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)




if __name__ == '__main__':
    p1 = Pessoa('Caio', 'Dantas')
    print(p1)
    print(p1.nome_completo)
    p1.nome_completo = 'Dore Durado'
    print(p1.nome_completo)
    p1.nome_completo = 'Dore Durado Durou Duro'
    print(p1.nome_completo)










