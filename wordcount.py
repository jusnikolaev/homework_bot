import re


# Count whitespaces in string
def wordcount(message):
    user_message = re.findall('\"(.*)\"', message)
    if user_message:
        words = user_message[0].split()
        len_words = str(len(words))
        len_words = 'Число слов: ' + str(len(words))
        return len_words
    elif len(message) == 0:
        return 'Вы ввели пустую строку'
    else:
        return 'В строке отсуствуют ковычки'


