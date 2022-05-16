import os
import cx_Oracle

from dotenv import load_dotenv
from os_util import is_linux

load_dotenv()

oracle_home = os.getenv('linux_oracle_home') if is_linux() else os.environ.get(
    'HOME') + os.getenv('mac_oracle_home')
cx_Oracle.init_oracle_client(oracle_home)
connection = cx_Oracle.connect(user=os.getenv('oracle_user'), password=os.getenv(
    'oracle_password'), dsn=os.getenv('oracle_dsn'))
cursor = connection.cursor()


def insert_winning_pairs(lotto_type, data):
    insert = ''
    if lotto_type == 'megamillion':
        insert = f"insert into HISTORY_MEGA_MILLION (DRAW_DATE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, MULTIPLIER) values ({data})"
    else:
        insert = f"insert into HISTORY_POWERBALL (DRAW_DATE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, MULTIPLIER) values ({data})"
    cursor.execute(insert)


def insert_predicted_numbers(lotto_type, data):
    insert = ''
    if lotto_type == 'megamillion':
        insert = f"insert into PREDICTION_MEGA_MILLION (PREDICTED_DATE, PHONE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6) values ({data})"
    else:
        insert = f"insert into PREDICTION_POWERBALL (PREDICTED_DATE, PHONE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6) values ({data})"
    cursor.execute(insert)


def select_phones():
    select = "select phone from USERS"
    phones = [entry[0] for entry in cursor.execute(select)]

    return phones


def select_predicted(lotto_type):
    if lotto_type == 'megamillion':
        select = "select PHONE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6 from PREDICTION_MEGA_MILLION"
        entries = [entry[0:7] for entry in cursor.execute(select)]
        return entries
    else:
        select = "select PHONE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6 from PREDICTION_POWERBALL"
        entries = [entry[0:7] for entry in cursor.execute(select)]
        return entries
