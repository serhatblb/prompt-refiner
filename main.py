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
def fix(
        prompt: str = typer.Argument(..., help="Refine edilecek ham prompt")
):
    """
    Ham promptunu gir, refine et ve otomatik olarak geçmişe kaydet.
    """
    with console.status("[bold green]🧠 Hafıza taranıyor ve prompt iyileştiriliyor...", spinner="dots"):
        try:
            # 1. Refine İşlemi
            refined = refine_prompt(prompt)

            # 2. Geçmişe Kaydet
            save_to_history(prompt, refined)

            # 3. Sonucu Göster
            console.print(Panel(refined, title="✨ Refined Prompt", border_style="green"))

            # 4. Panoya Kopyala
            pyperclip.copy(refined)
            console.print("[dim]✅ Sonuç panoya kopyalandı ve geçmişe kaydedildi![/dim]")

        except Exception as e:
            console.print(f"[bold red]Hata:[/bold red] {e}")


@app.command()
def history():
    """
    Geçmişte refine ettiğin son promptları listeler.
    """
    logs = load_history()
    if not logs:
        console.print("[yellow]Henüz geçmiş kaydı yok. Birkaç 'fix' işlemi yapmalısın.[/yellow]")
        return

    # Tablo Oluştur
    table = Table(title="📜 Prompt Geçmişi", show_header=True, header_style="bold magenta")
    table.add_column("Zaman", style="dim", width=20)
    table.add_column("Ham Girdi", style="cyan")
    table.add_column("Sonuç (Kısaltılmış)", style="green")

    for log in logs:
        # Sonucu tabloda çok yer kaplamasın diye kısaltıyoruz
        short_refined = (log["refined"][:60] + "...") if len(log["refined"]) > 60 else log["refined"]
        table.add_row(log["timestamp"], log["raw"], short_refined)

    console.print(table)


@app.command()
def clean():
    """
    Tüm geçmiş kayıtlarını siler.
    """
    clear_history()
    console.print("[bold red]🗑️ Geçmiş başarıyla temizlendi![/bold red]")


if __name__ == "__main__":
    app()