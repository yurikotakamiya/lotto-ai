from db import select_phones, insert_predicted_numbers, connection
from sys import argv
import random
import datetime


def generate_pairs(lotto_type):
    pairs = set()
    if lotto_type == 'megamillion':
        while len(pairs) < 6:
            number = random.randint(1, 70)
            pairs.add(number)

    elif lotto_type == 'powerball':
        while len(pairs) < 5:
            number = random.randint(1, 69)
            pairs.add(number)
        number = random.randint(1, 26)
        pairs.add(number)
    return ', '.join([str(num) for num in sorted(pairs)])


def send_message(lotto_type):
    phones = select_phones()
    current_date = datetime.date.today().strftime('%d-%b-%y')
    for phone in phones:
        pair = generate_pairs(lotto_type)
        string = f"'{current_date}', '{phone}', {pair}"
        insert_predicted_numbers(lotto_type, string)

    connection.commit()


send_message(argv[1])
