from pathlib import Path
from time import sleep

from yandex_music import Client

DEFAULT_CACHE_FOLDER = Path(__file__).resolve().parent / '.YMcache'
MAX_ERRORS = 3

client = Client('y0_AgAAAAAr9MNqAAG8XgAAAADWsiR8Aiopl21lTdSN92L1FSRWfnTOTuk').init()

tracks = client.users_likes_tracks()
total_tracks = len(tracks.tracks)
print("total tracks = ", total_tracks)
error_count = 0
for (i, short_track) in enumerate(tracks):
    while error_count < MAX_ERRORS:
        try:
            track = short_track.track if short_track.track else short_track.fetchTrack()
            artist_dir = Path(f'{track.artists[0].name}')
            file_path = DEFAULT_CACHE_FOLDER / artist_dir / f'{track.title}.mp3'

            if not file_path.exists():
                print('Downloading...')
                file_path.parent.mkdir(parents=True, exist_ok=True)
                while error_count < MAX_ERRORS:
                    try:
                        track.download(file_path)
                        error_count = 0
                        break
                    except Exception as e:
                        print('Error:', e)
                        error_count += 1
                        sleep(1)
            else:
                i+=1
                error_count = 0
                break

        except Exception as e:
            print('Error:', e)
            error_count += 1
            sleep(1)

