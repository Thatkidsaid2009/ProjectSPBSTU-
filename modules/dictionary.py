import sys
def create_dictionary():
    answer = input("Хотите создать словарь (да/нет): ").strip().lower()
    
    if answer == "да":
        print('Словарь создан!')
        return {}
    elif answer == "нет":
         print('До свидания!')
         sys.exit(1)
    else:
        while True:
            print("Введите 'да' или 'нет'.")
            answer = input()
            if answer == "да":
                print('Словарь создан!')
                return {}
                break
            elif answer == "нет":
                print('До свидания!')
                sys.exit(1)
            else:
                continue

def add_word(dictionary):
    while True:
        translation = input("Введите перевод и пример предложения через запятую (или 'стоп' для выхода): ").strip()
        
        if translation.lower() == 'стоп':
            return False
        
        if not translation:
            print("Перевод не может быть пустым.")
            continue
        
        if translation.lower() in dictionary:
            print(f"Ошибка: перевод '{translation}' уже есть в словаре!")
            print(f"Текущее слово: {dictionary[translation.lower()]['word']}")
            continue
        
        word = input(f"Перевод слова '{translation}' ").strip()
        if not word:
            print("Слово не может быть пустым.")
            continue
        
        
        dictionary[translation] = word
        
        print(f"Перевод '{translation}' добавлен для слова '{word}'!")
        return True
    return dictionary

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