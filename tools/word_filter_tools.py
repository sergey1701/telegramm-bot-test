import re
import string


def read_data_from_txt(path):
    with open(path, 'r') as file:
        data = file.read()
        data = data.split(',')
        data = [i.replace(' ', '').lower() for i in data]
    return data


def if_text_have_shit_words(message_text, gramar):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message_text.split(" ")} \
            .intersection(set(gramar)) != set():
        return True
    return False


if __name__ == "__main__":
    pass