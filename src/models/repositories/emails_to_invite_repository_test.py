import pytest, uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db interaction")
def test_register_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trips_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olaMundo@email.com"
    }

    emails_to_invite_repository.register_email(email_trips_info)

@pytest.mark.skip(reason="db interaction")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)
