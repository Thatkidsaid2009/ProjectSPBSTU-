from modules.dictionary import create_dictionary
from modules.dictionary import add_word
from modules.training import get_word_count
from modules.training import start_training
from modules.vocabulary_view import view_vocabulary
def search_word(dictionary):
    if not dictionary:
        print("Словарь пуст.")
        return

    search = input("Введите слово или перевод для поиска: ").strip().lower()

    for key in dictionary.keys():
        wrd = str(key).split(',')[0].strip().lower()
        if search == wrd or search == dictionary[key].lower().strip():

            print("\nСлово найдено:")
            print(f"Перевод: {wrd}")
            print(f"Слово: {dictionary[key]}")

            return

    print("Такого слова нет в словаре.")


def delete_word(dictionary):
    if not dictionary:
        print("Словарь пуст.")
        return

    delete = input("Введите перевод слова для удаления: ").strip().lower()
    for key in dictionary.keys():
            if key.split(',')[0].strip().lower() == delete:
                delete = key

    if delete in dictionary:
        dictionary_new = {k: v for k, v in dictionary.items() if k != delete}
        #for key, mean in dictionary.items():
            #if key == delete:
                #removed = dictionary.pop(delete)

        print(f"'{delete.capitalize()}' удалено.")
        return dictionary_new

    else:
        print("Такого слова нет в словаре.")


def dictionary_menu(dictionary):

    while True:

        print("\n=== МЕНЮ ===")
        print("1 - Поиск слова")
        print("2 - Удаление слова")
        print("3 - Добавление слова")
        print("4 - Количество слов")
        print("5 - Тренировка")
        print("6 - Просмотреть словарь")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":

            search_word(dictionary)

        elif choice == "2":

            dictionary = delete_word(dictionary)

        elif choice == "3":

            add_word(dictionary)
        
        elif choice == "4":

            get_word_count(dictionary)

        elif choice == "5":

            start_training(dictionary)

        elif choice == "6":
            
            view_vocabulary(dictionary)

        elif choice == "0":

            print("Выход из меню.")
            break

        else:

            print("Неверный пункт меню.")