from quiz import*

if __name__ == '__main__':
    q1 = Quiz(5,3)
    q2 = Quiz(10,4)
    q3 = Quiz(12,1)

    print(q1)
    print(q2)
    print(q3)

    print('Testando metodos separados')
    print(q1.get_acertos())
    print(q1.get_erros())
    print(q1.calcular_pontos())

    lista_qs = [q1, q2, q3]
    a1 = Aluno(1,"Maria" ,lista_qs)
    a2 = Aluno(2,"Renata", lista_qs)
    print(a1)

    d = Disciplina("POO", "Manuella", 2024, 4)
    d = add_aluno(a1)
    d = add_aluno(a2)
    print(d)
    #nvnc