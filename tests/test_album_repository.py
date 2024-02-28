from lib.album_repository import *

"""
When I call all()
I get all albums in the table
"""

def test_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "Entretanto", 1999, 1),
        Album(2, "Sangue Lagrimas Suor", 2001, 2)
    ]


"""
When we call albumRepository#find
We get a single album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(1)
    assert album == Album(1, "Entretanto", 1999, 1)

"""
When we call albumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Sobretudo", 2001, 1))

    result = repository.all()
    assert result == [
        Album(1, "Entretanto", 1999, 1),
        Album(2, "Sangue Lagrimas Suor", 2001, 2),
        Album(3, "Sobretudo", 2001, 1)
    ]

"""
When we call albumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(2) # Apologies to Maggie Nelson fans

    result = repository.all()
    assert result == [
        Album(1, "Entretanto", 1999, 1)

    ]
