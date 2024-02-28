from lib.album import *

def test_construct():
    album = Album(1, "Entretanto", 1999, 1)
    assert  album.id == 1
    assert  album.title == "Entretanto"
    assert  album.release_year == 1999
    assert  album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", "Test Release Year", "Test Artist id")
    assert str(album) == "Album(1, Test Title, Test Release Year, Test Artist id)"
    # Try commenting out the `__repr__` method in lib/album.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Title", "Test Release Year", "Test Artist id")
    album2 = Album(1, "Test Title", "Test Release Year", "Test Artist id")
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/album.py
    # And see what happens when you run this test again.
