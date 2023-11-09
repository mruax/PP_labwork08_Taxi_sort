import inflect
from translate import Translator


def num_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword=",", zero="ноль")


def translate_text(text, target_language='ru'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation
