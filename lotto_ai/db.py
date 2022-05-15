import os
import cx_Oracle

from dotenv import load_dotenv

load_dotenv()

cx_Oracle.init_oracle_client(os.environ.get('HOME') + '/Downloads/instantclient_19_8')
connection = cx_Oracle.connect(user=os.getenv('oracle_user'), password=os.getenv('oracle_password'), dsn=os.getenv('oracle_dsn'))
cursor = connection.cursor()

def insert_winning_pairs(lotto_type, data):
    insert = ''
    if lotto_type == 'megamillion':
        insert = "insert into HISTORY_MEGA_MILLION(DRAW_DATE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, MULTIPLIER) values(" + data + ')'
    else:
        insert = "insert into HISTORY_POWERBALL(DRAW_DATE, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, MULTIPLIER) values(" + data + ')'
    cursor.execute(insert)

def insert_predicted_numbers(lotto_type, data):
    insert = ''
    if lotto_type == 'megamillion':
        insert = "insert into HISTORY_MEGA_MILLION(PREDECTED_DATE, EMAIL, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6) values(" + data + ')'
    else:
        insert = "insert into HISTORY_POWERBALL(PREDECTED_DATE, EMAIL, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, MULTIPLIER) values(" + data + ')'
    cursor.execute(insert)