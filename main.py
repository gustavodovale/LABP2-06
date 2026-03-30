from collections import defaultdict

# Tarefa 01 - O Motor de Frequências 
vocabularios = {
 'l o w </w>': 5,
 'l o w e r </w>': 2,
 'n e w e s t </w>': 6,
 'w i d e s t </w>': 3
}

def get_stats(lista_vocabularios):

    pares = {}
    
    for palavra, frequencia in lista_vocabularios.items():
        print("listar as palavras e suas frquencias")
        print(palavra,frequencia)
        simbolos = palavra.split()
        print('lista os simbolos')
        print(simbolos)
        
        for i in range(len(simbolos) - 1):
            par_atual = (simbolos[i], simbolos[i+1])
            print("Mostrar o Par atual")
            par_atual
            if par_atual not in pares:
                pares[par_atual] = 0
                pares[par_atual] += frequencia
            
    return pares

if __name__ == "__main__":
    estatisticas = get_stats(vocabularios)
    
    print("Frequência de todos os pares:\n")
    for par, contagem in estatisticas.items():
        print(f"{par}: {contagem}")
        
    print("\nVerificarda funcionalidade da tarefa 1 especificando apenas a frequencia de um par ('l', 'o)")
    par_teste = ('l', 'o')
    print(f"O par {par_teste} aparece {estatisticas[par_teste]} vezes.")