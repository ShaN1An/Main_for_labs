import random

import notes_data


random.seed(24762876)

# Все заметки хранятся в списке, а теги — в словаре по индексу заметки.
notes = []
tags = {}
all_tags = set()


def help():
    return notes_data.HELP_TEXT


def add_note(notes, text):
    """Добавляет текст заметки в список заметок."""
    if text == "":
        print("Ошибка: текст заметки не указан.")
        return notes

    notes.append(text)
    print("Заметка добавлена.")
    return notes


def list_notes(notes):
    if not notes:
        print("Заметок пока нет.")
        return

    print("Ваши заметки:")
    for note in notes:
        print(note)


def find_note(notes, word):
    """Возвращает заметки, в которых встречается указанное слово."""
    if word == "":
        print("Ошибка: укажите слово для поиска.")
        return []

    found_or_empty = [
        note if word.lower() in note.lower() else ""
        for note in notes
    ]
    found_notes = [note for note in found_or_empty if note]
    if found_notes:
        print("Найдено.")
    else:
        print("Не найдено.")
    return found_notes


def add_tag(tags, idx, tag):
    """Добавляет тег к заметке по её индексу."""
    if idx not in tags:
        tags[idx] = set()
    tags[idx].add(tag)
    all_tags.add(tag)
    return tags


def get_long_notes(notes):
    return [n for n in notes if len(n) > 12]


def get_upper_notes(notes):
    return [n.upper() for n in notes]


def random_tip():
    number = random.randint(1, 4)

    if number == 1:
        print(notes_data.TIP_1)
    elif number == 2:
        print(notes_data.TIP_2)
    elif number == 3:
        print(notes_data.TIP_3)
    else:
        print(notes_data.TIP_4)


def run():
    global notes, tags, all_tags

    print(notes_data.APP_NAME)
    print(help())

    while True:
        command = input("> ")

        if command == "exit":
            print("Программа завершена.")
            break
        elif command == "help":
            print(help())
        elif command == "list":
            list_notes(notes)
        elif command == "clear":
            notes = []
            tags = {}
            all_tags = set()
            print("Все заметки удалены.")
        elif command == "tip":
            random_tip()
        elif command[:4] == "add ":
            add_note(notes, command[4:])
        elif command[:5] == "find ":
            find_note(notes, command[5:])
        elif command == "":
            print("Ошибка: введите команду.")
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    run()
