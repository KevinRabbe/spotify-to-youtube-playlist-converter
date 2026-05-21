from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import SpotifyTrack, YouTubeOption, MatchResult
from matcher import sort_youtube_options

app = FastAPI(title='Spotify to YouTube Converter')

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {'request': request}
    )


@app.post('/convert', response_class=HTMLResponse)
def convert_playlist(request: Request, playlist_url: str = Form(...)):
    spotify_track = SpotifyTrack(
        title='Blinding Lights',
        artist='The Weeknd',
        album='After Hours',
        duration_seconds=200
    )

    youtube_options = [
        YouTubeOption(
            video_id='test_video_1',
            title='The Weeknd - Blinding Lights Official Audio',
            channel='The Weeknd',
            duration_seconds=200,
            score=0
        ),
        YouTubeOption(
            video_id='test_video_2',
            title='Blinding Lights Live Performance',
            channel='Random Music Channel',
            duration_seconds=245,
            score=0
        )
    ]

    sorted_options = sort_youtube_options(spotify_track, youtube_options)

    matches = [
        MatchResult(
            spotify_track=spotify_track,
            youtube_options=sorted_options
        )
    ]

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
    return templates.TemplateResponse(
        'success.html',
        {
            'request': request,
            'playlist_url': 'https://www.youtube.com/'
        }
    )
