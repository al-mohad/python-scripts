# pip3 install translate
from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('translator.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('test-ja.txt', mode='r') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Error: Check your file path')
