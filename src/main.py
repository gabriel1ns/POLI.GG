import datetime
from match import Match
from replayAnalyser import HistoryAnalyzer
from consoleGUI import Rich 

def main_menu():
    analyzer = HistoryAnalyzer()
    gui = Rich() 

    # add random games
    analyzer.add_match(Match(
        champion="Garen", 
        outcome="Victory", 
        kills=8, 
        deaths=1, 
        assists=4,
        items=["Passos de Mercúrio", "Quebrapassos", "Couraça do Defunto", 
               "Força da Natureza", "Sinal de Sterak", "Dança da Morte"],
        cs=180, 
        duration_minutes=25, 
        date=datetime.datetime(2025, 10, 6)
    ))
    
    analyzer.add_match(Match(
        champion="Jinx", 
        outcome="Victory", 
        kills=10, 
        deaths=2, 
        assists=8,
        items=["Grevas do Berserker", "Arco-escudo Imortal", "Gume do Infinito", 
               "Canhão Fumegante", "Furacão de Runaan", "Dançarina Fantasma"],
        cs=250, 
        duration_minutes=30, 
        date=datetime.datetime(2025, 10, 5)
    ))
    
    analyzer.add_match(Match(
        champion="Jinx", 
        outcome="Defeat", 
        kills=15, 
        deaths=4, 
        assists=5,
        items=["Grevas do Berserker", "Mata-Cráquens", "Gume do Infinito", 
               "Dançarina Fantasma", "A Coletora", "Anjo Guardião"],
        cs=280, 
        duration_minutes=35, 
        date=datetime.datetime(2025, 10, 4)
    ))
    
    analyzer.add_match(Match(
        champion="Lux", 
        outcome="Defeat", 
        kills=3, 
        deaths=7, 
        assists=10,
        items=["Sapatos do Feiticeiro", "Tormenta de Luden", "Foco do Horizonte", 
               "Cajado do Vazio", "Rabadon", "Zhonya"],
        cs=150, 
        duration_minutes=28, 
        date=datetime.datetime(2025, 10, 3)
    ))

    # main loop
    while True:
        print("\n Ferramenta de Análise de Partidas")
        print("1. Ver Histórico Completo de Partidas")
        print("2. Buscar Performance por Campeão")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nOrdenar por:")
            print("1. Data (mais recente primeiro)")
            print("2. KDA (maior primeiro)")
            print("3. Campeão (ordem alfabética)")
            
            sort_opcao = input("Escolha o critério de ordenação: ")
            
            if sort_opcao == '1':
                criterion = 'date'
            elif sort_opcao == '2':
                criterion = 'kda'
            elif sort_opcao == '3':
                criterion = 'champion'
            else:
                print("Opção inválida, usando ordenação por data.")
                criterion = 'date'
            
            matches = analyzer.get_sorted_history(criterion)
            gui.display_history_header(criterion)
            gui.display_matches(matches)
            
        elif opcao == '2':
            champ = input("Digite o nome do campeão para buscar: ")
            resultado = analyzer.analyze_champion_performance(champ)
            
            if resultado:
                stats, matches = resultado
                gui.display_champion_summary(champ, stats)
                gui.display_matches(matches)
            else:
                gui.display_error(f"Nenhuma partida encontrada com o campeão '{champ}'.")

        elif opcao == '3':
            print("Obrigado por usar a ferramenta.")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()