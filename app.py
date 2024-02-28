import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# get all albums

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums = albums)



#test get a specific album with name
    # GET /books/<id>
    # Returns a single book
    # Try it:
    #   ; curl http://localhost:5001/albums/1
@app.route('/albums/<int:id>')
def get_albums_and_artist_name(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repo = ArtistRepository(connection) 
    album = album_repository.find(id)
    artist_id = album.artist_id
    artist = artist_repo.find(artist_id)
    return render_template("albums/show.html", album=album, artist=artist)

# get a specific artist

@app.route('/albums/artists/<int:id>')
def get_artist_page(id):
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection) 
    artist = artist_repo.find(id)
    return render_template("artists/specific_artist.html", artist=artist)


# get all artists

@app.route('/albums/artists')
def get_artists_index():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists/artists_index.html", artists = artists)


# create a new album

@app.route('/albums/new')
def get_new_album():
    return render_template('/albums/new.html')   

@app.route('/albums', methods = ['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    album = Album(None, title, release_year, artist_id)

    if not album.is_valid():
        errors = album.generate_errors()
        return render_template('albums/new.html', errors = errors)

    repository.create(album)
    return redirect(f"/albums/{album.id}")


# create a new artist

@app.route('/albums/artists/new')
def get_new_artist():
    return render_template('/artists/new.html')   



@app.route('/albums/artists', methods = ['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    
    return redirect(f"/albums/artists/{artist.id}")

"""
    if not album.is_valid():
        errors = album.generate_errors()
        return render_template('albums/new.html', errors = errors)

    repository.create(album)
    return redirect(f"/albums/{album.id}")
"""

# POST /books/<id>/delete
# Deletes a book

# @app.route('/albums/delete')
# def get_delete_album():
#     return render_template('albums/delete.html')


# @app.route('/album/delete', methods=['POST'])
# def delete_album():
#         connection = get_flask_database_connection(app)
#         repository = AlbumRepository(connection)
#         album_id = request.form['album_id']
#         repository.delete(album_id)
#         return redirect('/albums')

# POST /books/<id>/delete
# Deletes a book
@app.route('/albums/<int:id>/delete', methods=['POST'])
def delete_book(id):
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        repository.delete(id)
        return redirect(url_for('get_albums'))



# == Example Code Below ==
# # GET /goodye
# # returns a Bye! in HTML

# @app.route('/goodbye', methods=['GET'])
# def get_bye():
#     return render_template('goodbye.html', goodbye ='Bye!')


# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
