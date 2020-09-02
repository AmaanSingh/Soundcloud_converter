import json
import os
import sys

import requests
import requests.exceptions
from run import songs, artists
from secrets import spotify_token, spotify_user_id, playlist_name, description

def create_playlist():
    """Create A New Playlist"""
    request_body = json.dumps({
        "name": playlist_name,
        "description": description,
        "public": True
        })
    query = "https://api.spotify.com/v1/users/{}/playlists".format(
        spotify_user_id)
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()
    # playlist id
    print(response_json["id"])
    return response_json["id"]

def get_spotify_uri(song_name, artist, x, y):
    try:
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        #print(response_json["tracks"]["limit"])
        songs = response_json["tracks"]["items"]
        # only use the first song
        uri = songs[0]["uri"]
        return uri
    except Exception:
        x = x - 1
        y = y - 1

def add_song_to_playlist(x, y, list_songs):
    uris = []
    for song in list_songs:
            song_name = songs[song-1]
            artist = artists[song-1]
            spotify_uri = get_spotify_uri(song_name, artist, x, y)
            uris.append(spotify_uri)
    print(uris)
    v = len(songs)
    # create a new playlist
    playlist_id = create_playlist()
    for i in range(len(uris)):
        if v != 0:
    # add all songs into new playlist
            request_data = json.dumps({
                "uris": [uris[x-1]]
                })

            query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id
            )

            response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
                }
                )
            x = x - 1

if __name__ == '__main__':
    add_song_to_playlist(len(songs), len(artists), range(len(songs)))
