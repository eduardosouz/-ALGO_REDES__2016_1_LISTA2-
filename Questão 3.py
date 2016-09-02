nome = input('Digite o nome do aluno(a): ')
print ('Lembre de usar . (ponto) ao invés de , (vírgula).')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 7.00:
    print (nome, 'muito bem você foi a aprovado(a) e sua média foi: %.2f' %media)
elif media >= 4.00 and media < 7.00:
    print (nome, 'você está quase lá, vai precisar fazer recuperação, sua média é: %.2f' %media)
else:
    print (nome, 'não foi dessa vez, sua média foi %.2f e você está reprovado(a)' %media)
