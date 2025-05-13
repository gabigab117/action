import pytest


@pytest.mark.django_db
def test_set_to_default(note_1, note_2):
    """
    Test the set_to_default method of the Note model.
    """
    # Set note_1 as default
    note_1.set_to_default()
    note_1.refresh_from_db()

    # Check that note_1 is set to default
    assert note_1.is_default is True

    # Check that note_2 is not set to default
    assert note_2.is_default is False

    # Set note_2 as default
    note_2.set_to_default()
    note_2.refresh_from_db()
    note_1.refresh_from_db()

    # Check that note_2 is set to default
    assert note_2.is_default is True

    # Check that note_1 is not set to default
    assert note_1.is_default is True