#   Comendatarios do codigo #

#Entrada das notas do usuário.
#Valores aceitos podem ser int e float
#A saida/resultado é sempre em Float.
nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))

#Calculo de verificação da media.
med = (nota1 + nota2) / 2

#   Condição para o resultado.
#   Basicamente, o programa vai verificar 2 notas e ver se o aluno vai para a terceira prova

if med >= 7:
    print('Aprovado.')
    print('Media: ',med)

elif med < 7:
    nota3 = float(input('Digite sua nota 3: '))

#   Essa é a logica para ver qual nota vai ser substituida 
#   No caso, a menor nota vai ver discartada.
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

