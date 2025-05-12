import pytest
from note.models import Note


@pytest.fixture
def note_1():
    return Note.objects.create(
        title="Test Note",
        content="This is a test note.",
    )


@pytest.fixture
def note_2():
    return Note.objects.create(
        title="Another Test Note",
        content="This is another test note.",
    )
    