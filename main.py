# Blibiotecas utilizadas
import re
from transformers import AutoTokenizer


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

        simbolos = palavra.split()
        
        for i in range(len(simbolos) - 1):
            par_atual = (simbolos[i], simbolos[i+1])
   
            if par_atual not in pares:
                pares[par_atual] = 0
            pares[par_atual] += frequencia
            
    return pares

# Tarefa 2: O Loop de Fusão

def merge_vocab(par, vocabulario_atual):
    vocab_atualizado = {}
    
    # Transforma o par ('e', 's') em uma string 'e s' com espaço
    bigrama = re.escape(' '.join(par))
    
    # Cria a regra Regex para encontrar exatamente o 'e s' isolado por espaços
    padrao = re.compile(r'(?<!\S)' + bigrama + r'(?!\S)')
    
    for palavra in vocabulario_atual:
        # Substitui o 'e s' separado pelo 'es' junto
        palavra_fundida = padrao.sub(''.join(par), palavra)
        
        # Salva a nova palavra no dicionário atualizado com a mesma frequência
        vocab_atualizado[palavra_fundida] = vocabulario_atual[palavra]
        
    return vocab_atualizado


if __name__ == "__main__":
    print('Teste de avaliação da Tarefa 1: O Motor de Frequências\n')
    estatisticas = get_stats(vocabularios)
    
    print("Frequência de todos os pares:\n")
    for par, contagem in estatisticas.items():
        print(f"{par}: {contagem}")
        
    print("\nVerificar a funcionalidade da tarefa 1 especificando apenas a frequencia de um par ('e', 's')")
    par_teste = ('e', 's')
    print(f"O par {par_teste} aparece {estatisticas[par_teste]} vezes.")

    print("\n Teste de avaliação da Tarefa 2: O Loop de Fusão\n")
    
    # O número de iterações do treinamento
    K = 5
    
    for i in range(K):
        # 1. Conta a frequência atual de todos os pares
        estatisticas = get_stats(vocabularios)
        
        # 2. Pega o par com o maior número de aparições
        melhor_par = max(estatisticas, key=estatisticas.get)
        
        # 3. Funde esse par no vocabulário inteiro
        vocabularios = merge_vocab(melhor_par, vocabularios)
        
        # 4. Imprime os resultados da rodada
        print(f"Iteração {i+1}: Par fundido: {melhor_par}")
        print(f"Vocabulário atualizado: {vocabularios}\n")


# Tarefa 03: Integração Industrial e WordPiece

print("\nTarefa 3: O WordPiece na Prática (BERT)")
    
# Baixa e carrega as regras de tokenização do BERT Multilíngue
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    
# A frase teste obrigatoria
frase_teste = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
    
# O método .tokenize() fatiar a frase aplicando as regras do WordPiece
tokens = tokenizer.tokenize(frase_teste)
    
print(f"\nFrase original: '{frase_teste}'")
print(f"Tokens gerados:\n{tokens}")

