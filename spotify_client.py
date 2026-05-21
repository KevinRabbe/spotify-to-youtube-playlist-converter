import requests

from models import SpotifyTrack


class SpotifyClient:
    def __init__(self):
        self.base_url = 'https://api.spotify.com/v1'

    def extract_playlist_id(self, playlist_url: str) -> str:
        if 'playlist/' not in playlist_url:
            raise ValueError('Invalid Spotify playlist URL')

        playlist_id = playlist_url.split('playlist/')[1]
        playlist_id = playlist_id.split('?')[0]

        return playlist_id

    def get_playlist_tracks(self, playlist_url: str) -> list[SpotifyTrack]:
        # Placeholder implementation.
        # Real Spotify OAuth + API requests will be added later.

        return [
            SpotifyTrack(
                title='Blinding Lights',
                artist='The Weeknd',
                album='After Hours',
                duration_seconds=200
            )
        ]
