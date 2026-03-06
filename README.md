# SpotlightSaver

A CLI tool to extract and save Windows Spotlight wallpapers.

## Features

- Extracts the current Windows Spotlight wallpaper
- Saves wallpapers with timestamped filenames
- Prevents duplicate saves by checking image content
- Simple and easy-to-use command line interface

## Installation

### Prerequisites

- Windows operating system
- Python 3.12 or higher

### Install from source

```bash
git clone https://github.com/SeshuTarapatla/SpotlightSaver.git
cd SpotlightSaver
pip install .
```

### Install with pip/uv

```bash
pip install git+https://github.com/SeshuTarapatla/SpotlightSaver.git
```

or

```bash
uv pip install git+https://github.com/SeshuTarapatla/SpotlightSaver.git
```


### Run without install using uvx

```bash
uvx --from git+https://github.com/SeshuTarapatla/SpotlightSaver.git spotlight
```

## Usage

```bash
spotlight
```

This will extract the current Windows Spotlight wallpaper and save it to:
`%USERPROFILE%\Pictures\Windows Spotlight\Windows-Spotlight-{YYYY-MM-DD}.jpg`

## How it works

1. The tool locates the current Windows Spotlight wallpaper at:
   `%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper`

2. It calculates an MD5 hash of the image content to detect duplicates

3. If the image is new (not already saved), it copies the file to the destination folder with a timestamped filename

4. If the image was already extracted, it informs you of the existing file location

## Dependencies

- [Pillow](https://python-pillow.org/) - Python Imaging Library for image processing
- [Rich](https://github.com/Textualize/rich) - For beautiful console output
- [Typer](https://typer.tiangolo.com/) - For building CLI applications

## Development

```bash
# Install development dependencies
uv sync --dev
```

## License

MIT License

## Author

Seshu Tarapatla - [GitHub](https://github.com/SeshuTarapatla)