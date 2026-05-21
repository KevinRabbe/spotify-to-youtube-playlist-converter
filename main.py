from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from matcher import sort_youtube_options
from models import MatchResult
from spotify_client import SpotifyClient

try:
    from youtube_client import YouTubeClient
except ImportError:
    YouTubeClient = None

app = FastAPI(title='Spotify to YouTube Converter')

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')
spotify_client = SpotifyClient()
youtube_client = YouTubeClient() if YouTubeClient else None
latest_matches = []


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {'request': request}
    )


@app.post('/convert', response_class=HTMLResponse)
def convert_playlist(request: Request, playlist_url: str = Form(...)):
    global latest_matches

    spotify_tracks = spotify_client.get_playlist_tracks(playlist_url)
    matches = []

    for track in spotify_tracks:
        if youtube_client:
            youtube_options = youtube_client.search_track(track)
        else:
            youtube_options = []

        sorted_options = sort_youtube_options(track, youtube_options)

        matches.append(
            MatchResult(
                spotify_track=track,
                youtube_options=sorted_options
            )
        )

    latest_matches = matches

    return templates.TemplateResponse(
        'review.html',
        {
            'request': request,
            'playlist_url': playlist_url,
            'matches': matches
        }
    )


@app.post('/create-youtube-playlist', response_class=HTMLResponse)
def create_youtube_playlist(request: Request):
    if youtube_client:
        playlist_url = youtube_client.create_playlist('Converted Spotify Playlist')
    else:
        playlist_url = 'https://www.youtube.com/'

    return templates.TemplateResponse(
        'success.html',
        {
            'request': request,
            'playlist_url': playlist_url
        }
    )
