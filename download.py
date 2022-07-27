from pytube import Playlist
from pathlib import Path
from tqdm import tqdm

songs = Playlist('https://www.youtube.com/playlist?list=PLe7_EMUG1m1nCE2W6z4HnqQ8u2iyGlMD5')
print(f'Playlist "{songs.title}": {songs.length} videos ({len(songs)} still available)')

def on_progress(stream, chunk, bytes_remaining):
  on_progress.progress.update(stream.filesize - bytes_remaining)

for index, song in enumerate(tqdm(songs.videos)):
  try:
    song.bypass_age_gate()
    song.register_on_progress_callback(on_progress)
    audio = song.streams.filter(only_audio=True).order_by("abr").last()

    on_progress.progress = tqdm(leave=False, total=audio.filesize, desc=song.title)
    audio.download(filename_prefix=f'{index+1:04d} - ', skip_existing=True)

  except Exception as e:
    Path(f'{index+1:04d} - {song.title}.txt').touch()  # leave title as a .txt file
