"""
When I call GET / artists 
I get a list of all artists back
"""

from lib.artist import Artist
from lib.artist_repository import ArtistRepository





def test_post_create_artist_see_list(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post('/artists', data={'name': 'Andre Sheeran', 'genre': 'Classical'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''


def test_get_artists(db_connection, web_client):
    
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(Sam the kid, Rap)\n" \
        "Artist(Chullage, Rap)\n" \
        "Artist(Andre Sheeran, Classical)"



"""
When I call POST /albums with album info
That album is now in the list in GET /albums
"""
# def test_post_albums(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     response = web_client.post("/albums", data = {
#         "title": "Sobretudo", 
#         "release_year": "2001", 
#         "artist_id": "1"})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == ''

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, Entretanto, 1999, 1)\n"
#     "Album(2, Sangue Lagrimas Suor, 2001 , 2)\n"
#     "Album(3, Sobretudo, 2001 , 1)"

# Scenario 2

#  POST /albums
#  expected response: (200 OK)
"""
You need to submit a title, release year and artist id.
"""


#  GET /albums
#  expected response: (200 OK)

# Album(1, Entretanto, 1999, 1)