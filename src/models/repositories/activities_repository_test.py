import pytest, uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .activities_repository import ActivitiesRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db interaction")
def test_register_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Atividades",
        "occurs_at": "01-01-2024"
    }

    activities_repository.register_activity(activity_info)

@pytest.mark.skip(reason="db interaction")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)