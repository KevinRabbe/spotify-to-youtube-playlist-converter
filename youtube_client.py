from models import SpotifyTrack
from models import YouTubeOption


class YouTubeClient:
    def search_track(self, track: SpotifyTrack):
        return [
            YouTubeOption(
                video_id='example_video_id',
                title=track.artist + ' - ' + track.title,
                channel=track.artist,
                duration_seconds=track.duration_seconds,
                score=0
            )
        ]

    def create_playlist(self, playlist_name: str):
        return 'youtube_playlist_placeholder'
