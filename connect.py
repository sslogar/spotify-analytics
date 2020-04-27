import auth
import pandas as pd
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID= auth.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET=auth.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI=auth.SPOTIPY_REDIRECT_URI
SPOTIFY_USER_ID=auth.SPOTIFY_USER_ID

scope = 'playlist-modify-public'
username = SPOTIFY_USER_ID
token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
spotify = spotipy.Spotify(auth=token)
