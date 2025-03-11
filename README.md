# TorrentMate

A comprehensive Python tool to create torrent files, NFO files, and BBCode descriptions for media content.

## Features

- **Automatic detection** of content type (movie or TV series)
- **Technical analysis** of media files using mediainfo
- **Smart extraction** of important metadata:
  - Title and year
  - Resolution and video codec
  - Audio languages and subtitles
  - Source (BluRay, WEB-DL, etc.)
- **Generation of files**:
  - .torrent file using mktorrent
  - .nfo file formatted according to standards
  - BBCode description for forums

## Requirements

- Python 3.6+
- [mediainfo CLI: for media file analysis](https://mediaarea.net/fr/MediaInfo/Download)
- [mktorrent: for torrent file creation](https://github.com/pobrn/mktorrent)

## Installation

```bash
# Install dependencies (for Debian/Ubuntu)
sudo apt install mediainfo mktorrent

# Install the package
pip install torrentmate
```

Or install from source:

```bash
git clone https://github.com/LounisBou/TorrentMate.git
cd TorrentMate
pip install -e .
```

## Usage

### As a command-line tool

```bash
# Basic usage
torrent-mate /path/to/media/folder

# With custom tracker URL
torrent-mate /path/to/media/folder --tracker http://your-tracker.com:6969/announce
```

### As a Python module

```python
from torrentmate import TorrentMate

# Create an instance
creator = TorrentMate("/path/to/media/folder", 
                    tracker_url="http://your-tracker.com:6969/announce")

# Create all files
creator.create_all()

# Or create individual files
creator.create_nfo()
creator.create_bbcode()
creator.create_torrent()
```

## Output Files

For a media folder named "Movie Title (2023)", the script generates:

1. `Movie Title (2023) - LANGUAGE - SOURCE - RESOLUTION - CODEC.torrent`
2. `Movie Title (2023) - LANGUAGE - SOURCE - RESOLUTION - CODEC.nfo`
3. `Movie Title (2023) - LANGUAGE - SOURCE - RESOLUTION - CODEC.txt` (BBCode)

## License

[MIT License](./LICENSE)