from lib.artist import Artist
from lib.database_connection import DatabaseConnection

class ArtistRepository:

    def __init__(self, connection):
        self._connection = connection
    
    # Retrieve all artists
    
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"],row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by its id
    def find(self, Artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [Artist_id])
        row = rows[0]
        return Artist(row["id"],row["name"], row["genre"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        rows = self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        row = rows[0]
        artist.id = row['id']
        return artist

    # Delete a book by its id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [id])
        return None


