# youtube-songs
Downloads music from a Youtube playlist.

Convert downloaded files to .mp3s
```
find . -exec ffmpeg -y -hide_banner -loglevel warning -i {} -c:a libmp3lame -aq 2 {}.mp3 \;
```

Compute SHA256 for all files
```
find . -type f -print0 | sort -z | xargs -r0 sha256sum > sha256SumOutput
```

Add metadata with *musicbrainz picard*
