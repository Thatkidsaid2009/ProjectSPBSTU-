import json
import os

DICTIONARY_FILE = "my_dictionary.json"

def load_dictionary():
    if os.path.exists(DICTIONARY_FILE):
        with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_dictionary(dictionary):
    with open(DICTIONARY_FILE, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

def create_dictionary():
    answer = input("Хотите создать словарь (да/нет): ").strip().lower()
    
    if answer == "да":
        return {}
    elif answer == "нет":
        dictionary = load_dictionary()
        if dictionary:
            print(f"Загружено {len(dictionary)} слов(а).")
        else:
            print("Сохранённого словаря не найдено. Начинаем с пустого.")
        return dictionary
    else:
        print("Введите 'да' или 'нет'.")
        return create_dictionary()

def add_word(dictionary):
    while True:
        word = input("Введите слово (или 'стоп' для выхода): ").strip()
        
        if word.lower() == 'стоп':
            return False
        
        if not word:
            print("Слово не может быть пустым.")
            continue
        
        if word.lower() in dictionary:
            print(f"Ошибка: слово '{word}' уже есть в словаре!")
            print(f"Текущий перевод: {dictionary[word.lower()]['translation']}")
            continue
        
        translation = input(f"Перевод слова '{word}': ").strip()
        if not translation:
            print("Перевод не может быть пустым.")
            continue
        
        example = input(f"Пример предложения с '{word}': ").strip()
        if not example:
            print("Пример не может быть пустым.")
            continue
        
        dictionary[word.lower()] = {
            "word": word,
            "translation": translation,
            "example": example
        }
        
        print(f"Слово '{word}' добавлено!")
        return True

def main():
    dictionary = create_dictionary()
    
    print("Начинаем запись слов. Введите 'стоп' для завершения.")
    
    added = 0
    while True:
        result = add_word(dictionary)
        if not result:
            break
        added += 1
        print(f"Добавлено слов: {added}")
    
    save_dictionary(dictionary)
    print(f"Словарь сохранён в файл '{DICTIONARY_FILE}'")
    
    if dictionary:
        print(f"\nИтоговый словарь (всего слов: {len(dictionary)}):")
        for key, data in dictionary.items():
            print(f"{data['word']} - {data['translation']}: {data['example']}")
    else:
        print("Словарь пуст.")

if __name__ == "__main__":
    main()