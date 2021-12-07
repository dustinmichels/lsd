from rich.progress import Progress, BarColumn, TextColumn, FileSizeColumn


progress = Progress(
    "[progress.description]{task.description}",
    BarColumn(),
    "[progress.percentage]{task.percentage:>3.0f}%",
    TextColumn("[bold purple]{task.fields[size]}"),
    FileSizeColumn(),
)

with progress:
    task1 = progress.add_task("[red]File1", total=100, completed=10, size=20)
    task2 = progress.add_task("[green]File2", total=100, completed=20, size=20)
    task3 = progress.add_task("[cyan]File3", total=100, completed=30, size=20)
