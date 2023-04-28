# youtube-songs
Downloads music from a Youtube playlist.

### Setup Conda environment
```
conda create --name youtube python=3.8 -y
conda activate youtube
git clone https://github.com/r1cc4rdo/youtube-songs.git
cd youtube-songs
pip install -r requirements.txt
```

### Download whole playlist.
*Note* as of Apr 28, 2023 this does not work anymore.
It appears to be a problem with PyTube, whose last update is 2 years ago :(
```
python download.py
```

### Convert downloaded files to .mp3s
```
find . -exec ffmpeg -y -hide_banner -loglevel warning -i {} -c:a libmp3lame -aq 2 {}.mp3 \;
```

### Compute SHA256 for all files
```
find . -type f -print0 | sort -z | xargs -r0 sha256sum > sha256SumOutput
```

### Add metadata with [musicbrainz picard](https://picard.musicbrainz.org/)
On Mac. On Windows you're on your own :(
