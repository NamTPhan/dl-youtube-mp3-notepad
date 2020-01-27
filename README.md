# dl-youtube-mp3-notepad
Downloading YouTube music in an easy way. Bulk download music with notepad.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install youtube-dl.

```bash
pip install youtube-dl
```
In case you run into the error: *ffprobe or avprobe not found. Please install one*.

Download [LIBAV](http://builds.libav.org/windows/release-gpl/), I used libav-11.3-win64.7z. Just copy all files from "/win64/usr/bin" to where "youtube-dl.py" is.

or

```bash
sudo apt-get install ffmpeg
```
```bash
brew install ffmpeg
```

## Usage

1. Copy one or multiple YouTube urls
2. Paste it in the youtube-links.txt file
3. Run the following command:

```python
python youtube-dl.py
```
4. Profit

## Used Libraries

- [youtube-dl](https://github.com/ytdl-org/youtube-dl/)
