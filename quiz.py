class Quiz:
    disciplina: str
    aluno: str
    __acertos: int
    __erros: int

    def __int__(self, d : str, a : str, acertos : int, erros : int):
        self.disciplina = d
        self.aluno = a
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
