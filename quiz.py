from typing import List
class Quiz:
    __acertos: int
    __erros: int

    def __int__(self, d : str, a : str, acertos : int, erros : int):
        self.__acertos = acertos
        self.__erros = erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return  self.__erros

    def calcular_pontos(self):
        return self.__acertos - self.__erros

    def __str__(self):
        info = f'Disciplina: {self.disciplina}\n'
        info += f'Aluno: {self.aluno}\n'
        info += f'Acertos: {self.acertos}\n'
        info += f'Erros: {self.erros}\n'
        info += f'Total:{self.calcular_pontos()}'
        return info

class Quiz2A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - 4 *(self.get_erros())

class Quiz3A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - 2 *(self.get_erros())
class Aluno:
    __matricula : int
    __nome: str
    __quizes : List[Quiz]

    def __int__(self, mat : int, nom : str, kahoots : List[Quiz]):
        self.__matricula = mat
        self.__nome = nom
        self.__quizes = kahoots

    def __str__(self):
        info = f'Matricula: {self.__matricula}\n'
        info += f'Nome: {self.__nome}\n'
        soma = 0
        for q in self.__quizes:
            soma += q.calcular_pontos()
        info += f'Total de pontos {soma}\n'
        return info

    def get_matricula(self):
        return self.__matricula

class Diciplina:
    __nome : str
    __professor : str
    __ano : int
    __semestre : int
    __alunos : list[Aluno] = []

    def __init__(self, n : str, p : str, ano : int, semest : int):
        self.__nome = n
        self.__professor = p
        self.__ano = ano
        self.__semestre = semest

    def add_aluno(self, a : Aluno):
        for aluno in self.__alunos:
            if aluno.get_matricula() == a.get_matricula():
                raise Exception('Aluno já existe!')
        self.__alunos.append(a)
    def __str__(self):
        info = f'Disciplina: {self.__nome} Professor: {self.__professor}\n'
        info += f'Ano: {self.__ano} Semestre: {self.__semestre}\n'
        for aluno in self.__alunos:
            info += f'{aluno}'
            return info