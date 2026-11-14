from main import add_note, add_tag, find_note, get_long_notes


def test_add_note():
    notes = []

    add_note(notes, "Купить хлеб")

    assert notes == ["Купить хлеб"]


def test_find_note():
    notes = ["Купить хлеб", "Сделать лабораторную"]

    result = find_note(notes, "хлеб")

    assert result == ["Купить хлеб"]


def test_add_tag():
    tags = {}

    add_tag(tags, 0, "работа")

    assert tags == {0: {"работа"}}


def test_long_notes():
    notes = ["Короткая", "Сделать лабораторную работу"]
    long_notes = get_long_notes(notes)

    assert long_notes == ["Сделать лабораторную работу"]
