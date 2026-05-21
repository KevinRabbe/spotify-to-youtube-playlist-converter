from difflib import SequenceMatcher

from models import SpotifyTrack, YouTubeOption


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def calculate_score(track: SpotifyTrack, option: YouTubeOption) -> int:
    score = 0

    title_text = option.title.lower()
    channel_text = option.channel.lower()

    title_similarity = similarity(track.title, option.title)
    artist_similarity = similarity(track.artist, option.title + ' ' + option.channel)

    score += int(title_similarity * 40)
    score += int(artist_similarity * 35)

    duration_difference = abs(track.duration_seconds - option.duration_seconds)

    if duration_difference <= 5:
        score += 15
    elif duration_difference <= 10:
        score += 10
    elif duration_difference <= 20:
        score += 5

    if 'official audio' in title_text:
        score += 8

    if 'topic' in channel_text:
        score += 7

    if 'live' in title_text:
        score -= 10

    if 'remix' in title_text:
        score -= 10

    if 'cover' in title_text:
        score -= 15

    return max(0, min(score, 100))


def sort_youtube_options(track: SpotifyTrack, options: list[YouTubeOption]) -> list[YouTubeOption]:
    scored_options = []

    for option in options:
        option.score = calculate_score(track, option)
        scored_options.append(option)

    return sorted(scored_options, key=lambda option: option.score, reverse=True)
