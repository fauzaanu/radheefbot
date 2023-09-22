from googletrans import Translator

def translate(word: str):
    translator = Translator()
    return translator.translate(word, dest='dv').text
