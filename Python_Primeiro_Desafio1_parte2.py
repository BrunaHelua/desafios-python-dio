"""
Desafio: 
Leia um valor inteiro entre 1 e 12, inclusive. 
Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, 
em inglês, com a primeira letra maiúscula.
"""

month = input()

months_dict = {
    "1":"Janeiro",
    "2":"Fevereiro",
    "3":"Março",
    "4":"Abril",
    "5":"Maio",
    "6":"Junho",
    "7":"Julho",
    "8":"Agosto",
    "9":"Setembro",
    "10":"Outubro",
    "11":"Novembro",
    "12":"Dezembro"
}
if month in months_dict.keys():
    print(months_dict[month])
else:
    print("Digite um valor entre 1 e 12")