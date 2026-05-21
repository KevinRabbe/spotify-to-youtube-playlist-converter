from dataclasses import dataclass


@dataclass
class SpotifyTrack:
    title: str
    artist: str
    album: str
    duration_seconds: int


@dataclass
class YouTubeOption:
    video_id: str
    title: str
    channel: str
    duration_seconds: int
    score: int


@dataclass
class MatchResult:
    spotify_track: SpotifyTrack
    youtube_options: list[YouTubeOption]
