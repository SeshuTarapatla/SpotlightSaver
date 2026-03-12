__all__ = ["spotlight"]

from typer import Typer, Option

from spotlight_saver.controller import Spotlight


spotlight = Typer(
    name="spotlight",
    help="Windows Spotlight wallpaper extractor.",
    add_completion=False,
    no_args_is_help=False,
)


@spotlight.command(name="extract", help="Extract current spotlight wallpaper.")
def save_spotlight(explorer: bool = Option(False, "-e", "--explorer", help="Open [bold blue]spotlight[/] save directory.")):
    Spotlight.explorer() if explorer else Spotlight().save()
    