import json
from difflib import get_close_matches

data = json.load(open('data.json', 'r'))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        list_word_need_find = get_close_matches(word, data.keys())

        word_need_select =  input("[Q/A]Did you mean %s instead? Enter word which you need, or N if No.\n" % \
            [word_need_find for word_need_find in list_word_need_find])

        if word_need_select.lower() == 'n':
            return "We didn't understand your entry."
        elif word_need_select.lower() in list_word_need_find:
            return data[word_need_select]

    else:
        return "[WARNING] The word doesn't exist. Please double check it."

word = input("[INPUT] Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print("[OUTPUT]", item)
else:
    print('[OUTPUT]', output)