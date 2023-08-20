"""
Desafio: 
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
Conferir se um texto vai caber em um tuíte é sua tarefa.
"""
T = input()
tamanho = len(T)
if (tamanho>=1 and tamanho<=140):
    print("TWEET")
elif(tamanho>140):
    print("MUTE")