from rich.console import Console
from rich.table import Table

# Crear un objeto Console
console = Console()

# Crear una tabla
table = Table(show_header=False)  # Sin cabecera

# Añadir filas con colores personalizados en cada celda
table.add_row("[red]Celda 1,1[/red]", "[blue]Celda 1,2[/blue]", "[green]Celda 1,3[/green]")
table.add_row("[yellow]Celda 2,1[/yellow]", "[magenta]Celda 2,2[/magenta]", "[cyan]Celda 2,3[/cyan]")

# Imprimir la tabla
console.print(table)