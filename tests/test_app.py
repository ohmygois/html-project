from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "1. Entretanto",
        "2. Sangue Lagrimas Suor",
        "6. Sobretudo"
        ])
    expect(paragraph_tags).to_have_text([
        "Released: 1999",
        "Released: 2001",
        "Released: 2001"
    ])

# tests get album with artist name

def test_get_album_artist_name(page, db_connection, test_web_address):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    paragraph_tags = page.locator("p")
    expect(h1_tags).to_have_text([
        "Album: Entretanto"
        ])
    expect(paragraph_tags).to_have_text([
        "Released: 1999",
        "Artist: Sam the kid"
    ])

# test get specific artist

def test_get_artist_page(page, db_connection, test_web_address):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/artists/1")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text([
        "Sam the kid"
        ])
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Genre: Rap"
    ])  

# test create a new album
# and see it in the album index
    
def test_post_create_album(page, db_connection, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    
    page.fill("input[name=title]", "Test album")
    page.fill("input[name=release_year]", "1999")
    
    page.click("text='Add album'")

    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Entretanto",
        "Sangue Lagrimas Suor",
        "Test album"
        ])
    expect(paragraph_tags).to_have_text([
        "Released: 1999",
        "Released: 2001",
        "Released: 1999"
    ])

"""
Delete an album
"""
def test_delete_album(page, db_connection, test_web_address):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Delete Album")

    page.fill("input[name=album_id]", "3")

    page.click("text='Delete album'")

    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Entretanto",
        "Sangue Lagrimas Suor"
        ])
    expect(paragraph_tags).to_have_text([
        "Released: 1999",
        "Released: 2001"
    ])

"""
Create an album without title or release year or artist id
"""
def test_create_album_with_errors(page, db_connection, test_web_address):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.click("text='Add album'")

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "There were errors in your submission: title can't be blank, "\
        "release date can't be black, "\
        "nor artist id")