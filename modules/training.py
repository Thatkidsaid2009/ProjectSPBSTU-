"""
Модуль тренировки и статистики для проекта "Личный словарь"
"""
import random

def get_word_count(dictionary: dict):
    """Функция 5: возвращает количество слов в словаре"""
    print(f'Слов в словаре: {len(dictionary)}')

def start_training(dictionary):
    """
    Функция 4: режим тренировки.
    Показывает слова по очереди из словаря, пользователь вводит перевод.
    Выход по команде 'выход'.
    В конце выводит процент правильных ответов.
    """
    if not dictionary:
        print("Словарь пуст. Сначала добавьте слова!")
        return

    print("=== РЕЖИМ ТРЕНИРОВКИ ===")
    print("Чтобы выйти, напишите 'выход'")

    correct = 0
    total = 0

    for word in dictionary:
        answer = input(f"Переведите слово '{word}': ")
        
        if answer == "выход":
            break
        
        total = total + 1
        
        if answer.lower() == dictionary[word].lower():
            print("Правильно!")
            correct = correct + 1
        else:
            print(f"Неправильно. Правильный перевод: {dictionary[word]}")

    if total > 0:
        percent = (correct / total) * 100
        print(f"Результат: {correct} из {total} правильных ({percent:.0f}%)")
    else:
        print("Тренировка не проведена")