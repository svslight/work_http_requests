import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(arg_text, to_lang, from_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    params = {
        'key': API_KEY,
        'text': arg_text,
        'lang': '{}-{}'.format(to_lang, from_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ' '.join(json_['text'])


def translate(path_in, to_lang, from_lang='ru'):
    with open(path_in) as file_t:
        name = f'{path_in}'
        translate_file = translate_it(file_t, to_lang, from_lang)
        with open(os.path.join(r'd:', '\Projects', 'Netology', 'work_http_requests', 'translated', 'name'), 'w', encoding='utf8') as f:
            print('Запись перевода в файл:', name)
            f.write(translate_file)


translate('DE.txt', 'de', 'en')
translate('ES.txt', 'es')
translate('FR.txt', 'fr', 'zh')