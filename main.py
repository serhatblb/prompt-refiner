import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from app.core.refiner import refine_prompt
from app.memory.history import save_to_history, load_history, clear_history
import pyperclip

app = typer.Typer()
console = Console()


@app.command()
def fix(prompt: str = typer.Argument(..., help="Refine edilecek ham prompt")):
    """
    Promptu refine eder ve geçmişe kaydeder.
    """
    with console.status("[bold green]🧠 Düşünülüyor...", spinner="dots"):
        try:
            refined = refine_prompt(prompt)

            # Geçmişe kaydet
            save_to_history(prompt, refined)

            console.print(Panel(refined, title="✨ Refined Prompt", border_style="green"))
            pyperclip.copy(refined)
            console.print("[dim]✅ Panoya kopyalandı![/dim]")

        except Exception as e:
            console.print(f"[bold red]Hata:[/bold red] {e}")


@app.command()
def history():
    """
    Son yapılan düzeltmeleri listeler.
    """
    logs = load_history()
    if not logs:
        console.print("[yellow]Henüz geçmiş kaydı yok.[/yellow]")
        return

    table = Table(title="📜 Prompt Geçmişi")
    table.add_column("Zaman", style="dim", width=20)
    table.add_column("Ham Girdi", style="cyan")
    table.add_column("Sonuç (Kısaltılmış)", style="green")

    for log in logs:
        short_refined = (log["refined"][:50] + "...") if len(log["refined"]) > 50 else log["refined"]
        table.add_row(log["timestamp"], log["raw"], short_refined)

    console.print(table)


@app.command()
def clean():
    """Geçmişi temizler."""
    clear_history()
    console.print("[bold red]🗑️ Geçmiş silindi![/bold red]")


if __name__ == "__main__":
    app()