# POLI.GG - PROJETO ESTRUTURA DE DADOS

Uma aplicação de linha de comando para análise e visualização de histórico de partidas de League of Legends, inspirada em plataformas como OP.GG e U.GG.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para permitir que jogadores de League of Legends acompanhem seu desempenho através de estatísticas detalhadas e visualizações organizadas. A ferramenta oferece análise de performance por campeão, histórico de partidas com múltiplos critérios de ordenação e cálculos automáticos de KDA.

**Inspiração:** Sites como OP.GG, U.GG e Mobalytics, que fornecem estatísticas detalhadas e insights sobre o desempenho dos jogadores.

## ✨ Funcionalidades

- **Histórico de Partidas:** Visualize todas as suas partidas com informações detalhadas
- **Análise por Campeão:** Estatísticas específicas de performance com cada campeão
- **Múltiplos Critérios de Ordenação:**
  - Por data (mais recente primeiro)
  - Por KDA (melhor performance primeiro)
  - Por campeão (ordem alfabética)
- **Estatísticas Calculadas:**
  - Taxa de vitória (Win Rate)
  - KDA médio
  - CS médio por minuto
  - Médias de kills, deaths e assists

## 🛠️ Tecnologias e Bibliotecas

### Python 3.13.7
Linguagem principal do projeto.

### Bibliotecas Externas
- **Rich** - Biblioteca para criação de interfaces de terminal com formatação avançada, cores e painéis
  - Usada para exibir as partidas em painéis coloridos
  - Formatação de texto com estilos e cores dinâmicas

### Estruturas de Dados Implementadas
- **Linked List (Lista Encadeada)** - Armazenamento do histórico de partidas
- **Queue (Fila)** - Sistema de replay de partidas
- **Merge Sort** - Algoritmo de ordenação para organizar partidas por diferentes critérios

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/gabriel1ns/POLI.GG.git
cd src
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
--- Ferramenta de Análise de Partidas ---
1. Ver Histórico Completo de Partidas
2. Buscar Performance por Campeão
3. Sair
```

#### Opção 1: Ver Histórico Completo
Escolha como deseja ordenar suas partidas:
- Por data (mais recentes primeiro)
- Por KDA (melhores performances primeiro)
- Por campeão (ordem alfabética)

#### Opção 2: Buscar por Campeão
Digite o nome de um campeão para ver:
- Win rate com aquele campeão
- KDA médio
- Estatísticas detalhadas de cada partida

## 📁 Estrutura do Projeto

```
.
├── main.py              # Ponto de entrada do programa
├── match.py             # Classe Match com dados da partida
├── replayAnalyser.py    # Lógica de análise e estatísticas
├── replaySorting.py     # Implementação do Merge Sort
├── replayQueue.py       # Estrutura de fila para replays
├── LinkedList.py        # Implementação de lista encadeada
├── consoleGUI.py        # Interface visual com Rich
└── README.md            # Documentação do projeto
```

## 🎮 Exemplo de Uso

```python
# Adicionar uma partida
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

# Analisar performance com um campeão
stats, matches = analyzer.analyze_champion_performance("Jinx")
```

## 🔧 Recursos Técnicos

### Algoritmos Implementados
- **Merge Sort:** O(n log n) para ordenação eficiente de partidas
- **Busca Linear:** Para filtrar partidas por campeão

## 📊 Exemplo de Saída

```
╭─────────────── VICTORY ────────────────╮
│ Jinx         10 / 2 / 8                │
│ 9.00:1 KDA    CS: 250 (8.3/min)        │
│ Itens: Gume do Infinito, Furacão...    │
╰────────────── Duração: 30 min ─────────╯
```
