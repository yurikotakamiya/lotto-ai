from db import select_predicted
from message import send_message
from sys import argv


def send_text(lotto_type):
    send_list = select_predicted(lotto_type)
    for row in send_list:
        phone = row[0]
        pair = ','.join(str(a) for a in row[1:7])
        send_message(
            f'This is your predicted winning number for {lotto_type} is {pair}', phone)


send_text(argv[1])
