Inicio

regular = 0
bom = 0
otimo = 0

Repita 10 vezes (for i in range(10):)
   Escreva ( nota = int(input('O que você achou do filme? 3 - ótimo, 2 - bom e 1 - regular: ')))

    Se (nota == 1:)Então
       Enquanto (regular = regular + 1)
    Senão se (nota == 2:)Então
       Enquanto (bom = bom + 1)
    Senão se (nota == 3:)Então
       enquanto (otimo = otimo + 1)
    Senão:
        Escreva ('Opção inválida')

Escreva (('1) %s pessoa(as) respondeu(ram) ótimo.' %otimo))
Escreva (('2) %s pessoa(as) respondeu(ram) bom.' %bom))
Escreva (('3) %s pessoa(as) respondeu(ram) regular.' %regular))

Fim