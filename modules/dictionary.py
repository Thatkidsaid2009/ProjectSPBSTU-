def create_dictionary():
    answer = input("Хотите создать словарь (да/нет): ").strip().lower()
    
    if answer == "да":
        return {}
    elif answer == "нет":
        return {}
    else:
        print("Введите 'да' или 'нет'.")
        return create_dictionary()

def add_word(dictionary):
    while True:
        translation = input("Введите перевод (или 'стоп' для выхода): ").strip()
        
        if translation.lower() == 'стоп':
            return False
        
        if not translation:
            print("Перевод не может быть пустым.")
            continue
        
        if translation.lower() in dictionary:
            print(f"Ошибка: перевод '{translation}' уже есть в словаре!")
            print(f"Текущее слово: {dictionary[translation.lower()]['word']}")
            continue
        
        word = input(f"Слово для перевода '{translation}': ").strip()
        if not word:
            print("Слово не может быть пустым.")
            continue
        
        example = input(f"Пример предложения с '{word}': ").strip()
        if not example:
            print("Пример не может быть пустым.")
            continue
        
        dictionary[translation.lower()] = {
            "translation": translation,
            "word": word,
            "example": example
        }
        
        print(f"Перевод '{translation}' добавлен для слова '{word}'!")
        return True

def main():
    dictionary = create_dictionary()
    
    print("Начинаем запись переводов. Введите 'стоп' для завершения.")
    
    added = 0
    while True:
        result = add_word(dictionary)
        if not result:
            break
        added += 1
        print(f"Добавлено переводов: {added}")
    
    if dictionary:
        print(f"\nИтоговый словарь (всего переводов: {len(dictionary)}):")
        for key, data in dictionary.items():
            print(f"{data['translation']} - {data['word']}: {data['example']}")
    else:
        print("Словарь пуст.")

if __name__ == "__main__":
    main()