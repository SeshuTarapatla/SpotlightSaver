__all__ = ["spotlight"]

from typer import Typer

from spotlight_saver.controller import Spotlight


spotlight = Typer(
    name="spotlight",
    help="Windows Spotlight wallpaper extractor.",
    add_completion=False,
    no_args_is_help=False,
)


@spotlight.command(name="extract", help="Extract current spotlight wallpaper.")
def save_spotlight():
    Spotlight().save()
    