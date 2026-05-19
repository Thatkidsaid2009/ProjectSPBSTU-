def search_word(dictionary):
    if not dictionary:
        print("Словарь пуст.")
        return

    search = input("Введите слово или перевод для поиска: ").strip().lower()

    for key, data in dictionary.items():

        if search == key or search == data["word"].lower():

            print("\nСлово найдено:")
            print(f"Перевод: {data['translation']}")
            print(f"Слово: {data['word']}")
            print(f"Пример: {data['example']}")

            return

    print("Такого слова нет в словаре.")


def delete_word(dictionary):
    if not dictionary:
        print("Словарь пуст.")
        return

    delete = input("Введите перевод слова для удаления: ").strip().lower()

    if delete in dictionary:

        removed = dictionary.pop(delete)

        print(f"Слово '{removed['word']}' удалено.")

    else:
        print("Такого слова нет в словаре.")


def dictionary_menu(dictionary):

    while True:

        print("\n=== МЕНЮ ===")
        print("1 - Поиск слова")
        print("2 - Удаление слова")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":

            search_word(dictionary)

        elif choice == "2":

            delete_word(dictionary)

        elif choice == "0":

            print("Выход из меню.")
            break

        else:

            print("Неверный пункт меню.")