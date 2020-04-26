# Connect to Spotify

1. Go to the [Spotify Developer Console](https://developer.spotify.com/dashboard/applications) and create a developer profile for your Spotify account
2. Create a client ID
3. Install Spotipy: `pip install spotipy`
4. Create an auth file with with the client ID and secret
```python
#inside auth.py
SPOTIPY_CLIENT_ID='' #add your client id here
SPOTIPY_CLIENT_SECRET='' #add your secret id here
```
5. Import the client and secret into your script
