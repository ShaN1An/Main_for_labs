notes = ""

print("Менеджер заметок")
print("Доступные команды:")
print("add <текст> - добавить заметку")
print("list - показать заметки")
print("find <слово> - найти слово")
print("clear - удалить все заметки")
print("exit - выйти")
while True:
    command = input("> ")

    if command == "exit":
        print("Программа завершена.")
        break

    elif command == "list":
        if notes == "":
            print("Заметок пока нет.")
        else:
            print("Ваши заметки:")
            print(notes)

    elif command == "clear":
        notes = ""
        print("Все заметки удалены.")

    elif command[:4] == "add ":
        text = command[4:]

        if text == "":
            print("Ошибка: текст заметки не указан.")
        else:
            if notes == "":
                notes = text
            else:
                notes = notes + "\n" + text

            print("Заметка добавлена.")

    elif command[:5] == "find ":
        word = command[5:]

        if word == "":
            print("Ошибка: укажите слово для поиска.")
        else:
            if word in notes:
                print("Найдено.")
            else:
                print("Не найдено.")

    elif command == "":
        print("Ошибка: введите команду.")

    else:
        print("Неизвестная команда.")
