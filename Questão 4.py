Inicio

Escreva (nome = input('Digite o nome do aluno(a): '))
Escreva ('Lembre de usar . (ponto) ao invés de , (vírgula).')

Escreva n1 = float(input('Digite a primeira nota: '))
Escreva n2 = float(input('Digite a segunda nota: '))
Escreva n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

Se (media >= 7.00:) Então
    Escreva (nome, 'muito bem você foi a aprovado(a) e sua média foi: %.2f' %media)
Senão se (media >= 4.00 and media < 7.00:) Então
    Escreva (nome, 'você está quase lá, vai precisar fazer recuperação, sua média é: %.2f' %media)
Senão :
    Escreva (nome, 'não foi dessa vez, sua média foi %.2f e você está reprovado(a)' %media)

Fim