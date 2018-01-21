import string
import random


NUMBER_OF_PAIRS = 20
FILENAME = 'generated_data.txt'
generated_data = {}


def key_generate(max_length=5):
    key = ''
    key_length = random.randint(1, max_length)
    for _ in range(key_length):
        key += random.choice(string.ascii_letters + string.digits)
    if key not in generated_data:
        return key
    else:
        print('рекурсия')
        return key_generate()


def value_generate(max_length=10):
    length = random.randint(1, max_length)
    return ''.join([random.choice(string.ascii_letters + string.digits) for char in range(length)])

for _ in range(NUMBER_OF_PAIRS):
    new_key = key_generate()
    generated_data[new_key] = value_generate()

with open(FILENAME, 'w') as file:
    for key, value in sorted(generated_data.items()):
        file.write(key + '\t' + value + '\x0A')

