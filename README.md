# POLI.GG - Ferramenta de Análise de Partidas

Uma aplicação de linha de comando para análise e visualização de histórico de partidas de League of Legends, inspirada em plataformas como OP.GG e U.GG.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para permitir que jogadores de League of Legends acompanhem seu desempenho através de estatísticas detalhadas e visualizações organizadas. A ferramenta oferece análise de performance por campeão, histórico de partidas com múltiplos critérios de ordenação, cálculos automáticos de KDA e um sistema de fila para VOD Review.

**Inspiração:** Sites como OP.GG, U.GG e Mobalytics, que fornecem estatísticas detalhadas e insights sobre o desempenho dos jogadores.

## ✨ Funcionalidades

### 📊 Análise de Partidas
- **Histórico Completo:** Visualize todas as suas partidas com informações detalhadas
- **Análise por Campeão:** Estatísticas específicas de performance com cada campeão
- **Múltiplos Critérios de Ordenação:**
  - Por data (mais recente primeiro)
  - Por KDA (melhor performance primeiro)
  - Por campeão (ordem alfabética)

### 🎬 Sistema de VOD Review
- **Fila de Análise:** Adicione partidas específicas a uma fila para análise posterior
- **Review Organizado:** Processe partidas uma por uma na ordem em que foram adicionadas
- **Seleção Intuitiva:** Escolha partidas específicas de um campeão para adicionar à fila

### 📈 Estatísticas Calculadas
- Taxa de vitória (Win Rate)
- KDA médio
- CS médio por minuto
- Médias de kills, deaths e assists

## 🛠️ Tecnologias e Bibliotecas

### Python 3.17
Linguagem principal do projeto.

### Bibliotecas Externas
- **Rich** - Biblioteca para criação de interfaces de terminal com formatação avançada, cores e painéis
  - Exibição de partidas em painéis coloridos e estilizados
  - Formatação de texto com estilos e cores dinâmicas
  - Interface visual rica e interativa no terminal

### Estruturas de Dados Implementadas

#### Linked List (Lista Encadeada)
- Armazenamento do histórico completo de partidas
- Implementação própria com operações de inserção e iteração
- Permite crescimento dinâmico sem necessidade de redimensionamento

#### Queue (Fila - FIFO)
- **Sistema de VOD Review:** Gerencia a fila de partidas para análise
- Implementação própria usando estrutura encadeada
- Operações `enqueue` (adicionar) e `dequeue` (remover e processar)
- Segue o princípio First-In-First-Out (primeira partida adicionada é a primeira a ser revisada)

#### Merge Sort
- Algoritmo de ordenação O(n log n) para organizar partidas
- Suporte para múltiplos critérios de ordenação
- Implementação recursiva eficiente

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/poli-gg.git
cd poli-gg
```

2. Instale as dependências:
```bash
pip install rich
```

## 🚀 Como Usar

Execute o programa principal:
```bash
python main.py
```

### Menu Principal

```
Ferramenta de Análise de Partidas
1. Ver Histórico Completo de Partidas
2. Buscar Performance por Campeão
3. Adicionar partida à Fila de Análise
4. Vod-review da primeira partida na fila
5. Sair
```

### 📖 Guia de Funcionalidades

#### 1️⃣ Ver Histórico Completo
Visualize todas as partidas registradas com opções de ordenação:
- **Por Data:** Partidas mais recentes aparecem primeiro
- **Por KDA:** Suas melhores performances no topo
- **Por Campeão:** Organização alfabética para fácil navegação

#### 2️⃣ Buscar por Campeão
Digite o nome de um campeão para ver:
- Win rate específico daquele campeão
- KDA médio em todas as partidas
- Lista detalhada de cada partida jogada
- Estatísticas agregadas (média de kills, deaths, assists)

#### 3️⃣ Sistema de Fila para VOD Review
**Como funciona:**
1. Digite o nome do campeão
2. O sistema mostra todas as partidas com aquele campeão
3. Escolha o número da partida que deseja adicionar à fila
4. A partida é adicionada ao final da fila de análise

**Por que usar?**
- Organize quais partidas você quer revisar depois
- Útil para marcar partidas importantes para estudar
- Processe suas análises de forma organizada

#### 4️⃣ Processar VOD Review
- Remove e exibe a primeira partida da fila
- Permite revisar partidas na ordem em que foram marcadas
- A partida é removida da fila após ser processada
- Ideal para sessões de estudo focadas

## 📁 Estrutura do Projeto

```
.
├── main.py              # Ponto de entrada e menu principal
├── match.py             # Classe Match com dados da partida
├── replayAnalyser.py    # Lógica de análise e gerenciamento de fila
├── replaySorting.py     # Implementação do Merge Sort
├── replayQueue.py       # Estrutura de fila para VOD review
├── LinkedList.py        # Implementação de lista encadeada
├── consoleGUI.py        # Interface visual com Rich
└── README.md            # Documentação do projeto
```

## 🎮 Exemplo de Uso Completo

```python
# 1. Adicionar uma partida ao histórico
analyzer.add_match(Match(
    champion="Jinx",
    outcome="Victory",
    kills=10,
    deaths=2,
    assists=8,
    items=["Gume do Infinito", "Furacão de Runaan"],
    cs=250,
    duration_minutes=30,
    date=datetime.datetime(2025, 10, 5)
))

# 2. Analisar performance com um campeão
stats, matches = analyzer.analyze_champion_performance("Jinx")

# 3. Adicionar partida específica à fila de review
analyzer.add_to_replay_queue(matches[0])

# 4. Processar a próxima partida da fila
next_match = analyzer.process_next_in_queue()
```

## 🔧 Detalhes Técnicos

### Como funciona a Fila de VOD Review

```
Adicionar:     [Match 1] -> [Match 2] -> [Match 3] -> None
               HEAD                                    TAIL

Processar:     [Match 2] -> [Match 3] -> None
               HEAD                      TAIL
               (Match 1 foi processada)
```

A fila segue o princípio **FIFO (First In, First Out)**:
- Partidas são adicionadas no final (enqueue)
- Partidas são removidas do início (dequeue)
- Garante que você revise na ordem que marcou

### Algoritmos Implementados

**Merge Sort - O(n log n)**
```
Para ordenação eficiente de partidas
- Divide a lista ao meio recursivamente
- Mescla as metades de forma ordenada
- Suporta ordenação por diferentes critérios
```

**Busca Linear - O(n)**
```
Para filtrar partidas por campeão
- Percorre toda a lista de partidas
- Compara nome do campeão (case-insensitive)
```

## 📊 Exemplo de Saída

### Partida Individual
```
╭─────────────── VICTORY ────────────────╮
│ Jinx         10 / 2 / 8                │
│ 9.00:1 KDA    CS: 250 (8.3/min)        │
│ Itens: Gume do Infinito, Furacão...    │
╰────────────── Duração: 30 min ─────────╯
```

### Resumo de Campeão
```
╭── Resumo de Performance com Jinx ──────╮
│ Win Rate: 66.67% (2V / 1D)             │
│ KDA Médio: 8.33:1 (12.5 / 3.0 / 6.5)  │
╰────── Baseado em 3 partidas ──────────╯
```
