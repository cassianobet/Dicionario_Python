"""
dicionario.py
Cassiano Bet

Funçôes que imprementam um dicionario em python
"""

palavras = set()
def check(palavra): #Retorno bool se a palavra existe na estrutura montada 
    return palavra.lower() in palavras
    
def load(dicionario):  #Função que carrega o arquivo dicionario
    with open(dicionario, "r") as file:
        for line in file:
            palavras.add(line.rstrip("\n")) #Carrega palavra na estrutura  
            pass
    return True

def size():  #Retorna a quantidade de palavras no Dicionario
    return len(palavras)

def unload():
    return True

