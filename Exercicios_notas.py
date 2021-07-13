
nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))


med = (nota1 + nota2) / 2

if med >= 7:
    print('Aprovado.')
    print('Media: ',med)

elif med < 7:
    nota3 = float(input('Digite sua nota 3: '))

    if nota1 > nota2:
        aux = nota1
    else:
        aux = nota2

    med = (nota3 + aux) / 2

    if med >= 7:
        print('Aprovado')
        print('Media: ',med)
    else:
        print('Reprovado')
        print('Media: ',med)

