"""
Desafio: 
Paulinho tem em suas mãos um novo problema. 
Agora a sua professora lhe pediu que construísse um programa para verificar, 
à partir de dois valores muito grandes A e B, 
se B corresponde aos últimos dígitos de A.
"""

N = int(input())
while N > 0:
    A, B = input().split() 
    if len(B) <= len(A):
        c = len(A)-len(B)
        if B == A[c:]:
            print("encaixa")
        else:
            print('nao encaixa')
    else:
        print('nao encaixa')
    N -= 1