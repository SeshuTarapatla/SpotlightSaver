from datetime import datetime
from hashlib import md5
from pathlib import Path
from shutil import copy2

from PIL import Image
from rich.console import Console

THEMES_DIR = Path("~/AppData/Roaming/Microsoft/Windows/Themes").expanduser()
SAVE_DIR = Path("~/Pictures/Windows Spotlight").expanduser()
console = Console(highlighter=None)


def img_md5(file: Path) -> str:
    with Image.open(file) as img:
        return md5(img.tobytes()).hexdigest()



class Spotlight:
    def __init__(self) -> None:
        SAVE_DIR.mkdir(exist_ok=True, parents=True)
        self.current_spotlight = THEMES_DIR / "TranscodedWallpaper"
        self._last_spotlight = None

    def save(self):
        if not self.current_spotlight.exists():
            console.print("[bold red]ERROR[/] : No spotlight found to extract.")
        if self.last_spotlight and img_md5(self.current_spotlight) == img_md5(
            self.last_spotlight
        ):
            console.print(
                f"[bold blue]INFO [/] : Spotlight already extracted. [magenta]'{self.last_spotlight}'[/]"
            )
        else:
            export: Path = (
                SAVE_DIR
                / f"Windows-Spotlight-{datetime.now().strftime('%Y-%m-%d')}.jpg"
            )
            copy2(self.current_spotlight, export)
            console.print(
                f"[bold blue]INFO [/] : Spolight extracted: [cyan]'{export}'[/]."
            )

    @property
    def last_spotlight(self) -> Path | None:
        if self._last_spotlight is None:
            files = sorted(
                SAVE_DIR.glob("*.jpg"),
                key=lambda file: file.stat().st_mtime,
                reverse=True,
            )
            if files:
                self._last_spotlight = files[0]
        return self._last_spotlight
