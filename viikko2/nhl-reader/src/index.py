from rich.table import Table
from rich.console import Console

from player import PlayerReader, PlayerStats

def main():
    console = Console()
    season = ask_season(console)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    nationality = ask_nationality(console)
    players = stats.top_scorers_by_nationality(nationality)

    table = build_table(players, season, nationality)
    console.print(table)

def ask_season(console: Console) -> str:
    season = (
        "[bold yellow]Season[/bold yellow] [cyan]>[/cyan] "
        "[dim][2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25][/dim] "
    )
    return console.input(season)

def ask_nationality(console: Console) -> str:
    nationality = ("[bold yellow]Nationality[/bold yellow] [cyan]>[/cyan] "
    "[dim][USA, FIN, CAN, SWE, CZE, RUS, SLO, FRA, GBR, SVK, DEN, NED, AUT, BLR," \
    " GER, SUI, NOR, UZB, LAT, AUS][/dim] ")
    return console.input(nationality.strip().upper())

def build_table(players, season: str, nationality: str) -> Table:
    table = Table(title=f"Pisteet kaudelta {season} - {nationality}")
    table.add_column("Nimi", width=20)
    table.add_column("Joukkue", width=15)
    table.add_column("G", justify="right")
    table.add_column("A", justify="right")
    table.add_column("P", justify="right")
    for p in players:
        total = p.goals + p.assists
        table.add_row(p.name,p.team,str(p.goals),str(p.assists),str(total))
    return table

if __name__ == "__main__":
    main()

# poetry run python src/index.py
