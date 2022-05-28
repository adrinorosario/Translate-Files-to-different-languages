import sys
import os
from translate import Translator

translator = Translator(to_lang="ja")

path = sys.argv[1]
translated = sys.argv[2]

if not os.path.exists(translated):
    os.makedirs(translated)

for filename in os.listdir(path):
    with open(f'{path}/{filename}', mode='r', encoding='utf-8') as file:
        text = file.read()
        translation = translator.translate(text)
        with open(f'{translated}/{filename}', mode='w', encoding='utf-8') as file2:
            file2.write(translation)
