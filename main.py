import sys
from modules.delete_find import search_word
from modules.delete_find import delete_word
from modules.delete_find import dictionary_menu
from modules.dictionary import create_dictionary
from modules.dictionary import add_word
from modules.training import get_word_count
from modules.training import start_training
from modules.vocabulary_view import view_vocabulary

D = create_dictionary()
dictionary_menu(D)
print('До свидания! Ждем вас снова!')
print(D)

