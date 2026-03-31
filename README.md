# Laboratório 06: Construindo um Tokenizador BPE e Explorando o WordPiece

## Objetivo
Este laboratório tem como objetivo construir o motor fundamental do algoritmo Byte Pair Encoding (BPE) do zero, utilizando apenas Python nativo para compreender a matemática de tokenização em sub-palavras. Na segunda etapa, o projeto explora a aplicação industrial desse conceito utilizando o tokenizador WordPiece do modelo BERT, fornecido pela biblioteca Hugging Face.

## Estrutura do Código
O script principal está dividido nas 3 tarefas exigidas:
* **Tarefa 1 - O Motor de Frequências:** Varredura do corpus e contagem de pares de símbolos adjacentes utilizando `collections.defaultdict`.
* **Tarefa 2 - O Loop de Fusão:** Execução de 5 iterações ($K=5$) do algoritmo BPE, fundindo os pares mais frequentes (ex: 'e' + 's' -> 'es') utilizando Expressões Regulares (`re`).
* **Tarefa 3 - Integração Industrial (WordPiece):** Utilização do `AutoTokenizer` multilíngue do BERT para fatiar morfológicamente uma frase complexa ("inconstitucionalmente").

## Como Executar
Verificar se estar dentro da pasta labP2-06

### Crie e ative o seu ambiente virtual (Opcional):
```bash
   python -m venv .venv
   source .venv/bin/activate
```
### Instale as dependências exigidas (Hugging Face):
```bash
pip install -r requirements.txt
```

### Execute o script teste principal do laboratorio:
```bash
python main.py
```

## Declaração de Integridade Acadêmica (Uso de IA)

Conforme as exigências do roteiro do Laboratório 6, declaro que utilizei assistência de Inteligência Artificial Generativa (Gemini) especificamente para a formulação da lógica de Expressões Regulares (Regex) na Tarefa 2.

* **Trecho gerado:** Criação das regras de compilação e substituição (`re.compile` e `padrao.sub`) na função `c`.
* **Motivo e Revisão:** A IA foi utilizada para construir um padrão de Regex seguro que utiliza *Lookbehind* e *Lookahead* negativos (`(?<!\S)` e `(?!\S)`). Isso garantiu que a fusão dos caracteres ocorresse apenas quando eles estivessem perfeitamente isolados por espaços em branco, evitando a corrupção de sub-palavras que já haviam sido unidas em iterações anteriores do BPE. O código foi lido, testado (validando a formação correta do sufixo `est</w>`) e totalmente compreendido.


## Relatório Tarefa 3: O Funcionamento do WordPiece (Os símbolos ##)

No tokenizador do BERT (que utiliza o algoritmo WordPiece), os sinais de cerquilha duplos (`##`) indicam que aquele token é uma **continuação ou sufixo** de uma palavra, e não o início de uma nova. Por exemplo, na frase obrigatória testada no laboratório, a palavra **"transformer"** foi dividida na raiz "transform" e no sufixo "##er". Outro caso interessante é a palavra **"hiper-parâmetros"**, que foi fatiada em pedaços menores e sufixos como "hip", "##er", "par", "##âm" e "##etros".

O uso dessa estratégia de sub-palavras é fundamental para **impedir o travamento do modelo diante de vocabulário desconhecido** (o temido erro de *Out-Of-Vocabulary* - OOV). Se o modelo encontra uma palavra rara, nova ou com erro de digitação que não está no seu dicionário fixo de treinamento, em vez de gerar um erro ou substituir por uma tag genérica de `<UNK>` (desconhecido), ele quebra essa palavra em pedaços menores (radicais, prefixos e sufixos) que ele já conhece. Isso permite que a rede neural processe qualquer texto sem travar e ainda consiga deduzir o significado da palavra nova juntando os seus pedaços lógicos.
