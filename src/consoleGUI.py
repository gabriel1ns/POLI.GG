from rich.console import Console
from rich.panel import Panel
from rich.text import Text

#this class basically takes the gui, all of the project's logic is on the other archives.

class Rich:
    def __init__(self):
        self.console = Console()

    def display_matches(self, matches):
        for match in matches:
            border = "green" if match.outcome == "Victory" else "red"
            outcome_text = Text(match.outcome.upper(), style=f"bold {border}")
            
            score = Text()
            score.append(f"{match.kills} / ")
            score.append(str(match.deaths), style="bold red")
            score.append(f" / {match.assists}")

            kda = match.calculate_kda()
            
            content = Text()
            content.append(f"{match.champion:12}", style="bold cyan")
            content.append(" ")
            content.append(score)
            content.append("\n")
            content.append(f"{kda:.2f}:1 KDA", style="yellow")
            
            cs_per_min = match.cs / match.duration_minutes
            content.append(f"    CS: {match.cs} ({cs_per_min:.1f}/min)\n", style="bright_white")
            content.append(f"Itens: {', '.join(match.items)}", style="grey70")

            self.console.print(
                Panel(
                    content,
                    title=outcome_text,
                    subtitle=f"Duração: {match.duration_minutes} min",
                    border_style=border,
                    width=60
                )
            )

    def display_champion_summary(self, champion, stats):
        text = Text()
        wr = stats['win_rate']
        wins = stats['victories']
        total = stats['total_matches']
        losses = total - wins
        
        wr_color = 'green' if wr >= 50 else 'red'
        text.append("Win Rate: ")
        text.append(f"{wr:.2f}%", style=f"bold {wr_color}")
        text.append(f" ({wins}V / {losses}D)\n")
        
        text.append("KDA Médio: ")
        text.append(f"{stats['avg_kda_ratio']:.2f}:1", style="yellow")
        text.append(f" ({stats['avg_kills']:.1f} / {stats['avg_deaths']:.1f} / {stats['avg_assists']:.1f})")

        self.console.print(
            Panel(
                text,
                title=f"[bold cyan]Resumo de Performance com {champion}[/bold cyan]",
                subtitle=f"Baseado em {total} partidas",
                width=60
            )
        )

    def display_history_header(self, criterion):
        self.console.print(f"\n[bold underline]Histórico de Partidas Recentes[/bold underline] (Ordenado por: {criterion.upper()})")

    def display_error(self, msg):
        self.console.print(f"\n[bold red]{msg}[/bold red]")

    def display_message(self, msg):
        self.console.print(f"\n[bold green]{msg}[/bold green]")

    def display_queue_header(self):
        self.console.print("\n[bold underline]Processando Próxima Partida da Fila[/bold underline]")