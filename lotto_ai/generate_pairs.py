from db import select_phones, insert_predicted_numbers, connection, select_predicted
from message import send_message
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


def insert_pairs(lotto_type):
    phones = select_phones()
    current_date = datetime.date.today().strftime('%d-%b-%y')
    for phone in phones:
        pair = generate_pairs(lotto_type)
        string = f"'{current_date}', '{phone}', {pair}"
        insert_predicted_numbers(lotto_type, string)

    connection.commit()


def send_text(lotto_type):
    send_list = select_predicted(lotto_type)
    for row in send_list:
        phone = row[0]
        pair = ','.join(str(a) for a in row[1:7])
        send_message(
            f'This is your predicted winning number for {lotto_type} is {pair}', phone)


send_text(argv[1])
