from player import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()
    season = console.input("[bold yellow]Season[/bold yellow] [cyan]>[/cyan] [dim][2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24 2024-25][/dim] ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = console.input("[bold yellow]Nationality[/bold yellow] [cyan]>[/cyan] [dim][USA, FIN, CAN, SWE, CZE, RUS, SLO, FRA, GBR, SVK, DEN, NED, AUT, BLR, GER, SUI, NOR, UZB, LAT, AUS][/dim] ")
    nationality = nationality.strip().upper()
    players = stats.top_scorers_by_nationality(nationality)
    table = Table(title=f"Pisteet kaudelta {season} - {nationality}")
    table.add_column("Nimi", width=20)
    table.add_column("Joukkue", width=15)
    table.add_column("G", justify="right")
    table.add_column("A", justify="right")
    table.add_column("P", justify="right")

    for p in players:
        total = p.goals + p.assists
        table.add_row(
            p.name,
            p.team,
            f"{p.goals}",
            f"{p.assists}",
            f"{total}"
        )

    console.print(table)

if __name__ == "__main__":
    main()

# poetry run python src/index.py