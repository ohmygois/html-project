from lib.artist_repository import *

"""
When I call all()
I get all Artists in the table
"""

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist("Sam the kid", "Rap"),
        Artist("Chullage", "Rap")
    ]


"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(1)
    assert artist == Artist("Sam the kid", "Rap")

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist("Andre Sheeran", "Classical"))

    result = repository.all()
    assert result == [
        Artist("Sam the kid", "Rap"),
        Artist("Chullage", "Rap"),
        Artist("Andre Sheeran", "Classical")
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(2) 

    result = repository.all()
    assert result == [
        Artist("Sam the kid", "Rap")
    ]
