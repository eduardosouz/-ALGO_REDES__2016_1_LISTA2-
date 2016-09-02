regular = 0
bom = 0
otimo = 0

for i in range(10):
    nota = int(input('O que você achou do filme? 3 - ótimo, 2 - bom e 1 - regular: '))
    if nota == 1:
        regular = regular + 1
    elif nota == 2:
        bom = bom + 1
    elif nota == 3:
        otimo = otimo + 1
    else:
        print('Opção inválida')

print ('1) %s pessoa(as) respondeu(ram) ótimo.' %otimo)
print ('2) %s pessoa(as) respondeu(ram) bom.' %bom)
print ('3) %s pessoa(as) respondeu(ram) regular.' %regular)