import pytest, uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db interaction")
def test_register_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_info = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "http://www.test.com",
        "title": "Test Link"
    }

    links_repository.register_link(link_info)

@pytest.mark.skip(reason="db interaction")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links_from_trip(trip_id)
    print(links)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
