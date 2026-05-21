# Spotify to YouTube Playlist Converter

A small local-only Python web app that converts a Spotify playlist into a YouTube playlist.

## Scope

This tool does exactly one thing:

1. Paste a Spotify playlist link.
2. Read song title, artist, album, and duration.
3. Search matching YouTube videos.
4. Show possible matches for review.
5. Create a YouTube playlist.

No cloud hosting, no user accounts, no database, no recommendations, no AI features.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:

```text
http://localhost:8000
```

## Environment variables

Copy `.env.example` to `.env` and add your own API credentials.

Never commit your real `.env` file.
