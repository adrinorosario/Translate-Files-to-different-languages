""" A python translator that can translate files into different languages"""
from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('./input.txt', mode='r', encoding='utf-8') as file:
        text = file.read()
        translation = translator.translate(text)
        with open('./translated.txt', mode='w', encoding='utf-8') as file2:
            file2.write(translation)
except FileNotFoundError as err:
    print("File not found")
