import gspread
from google.oauth2.service_account import Credentials

from wonderwords import RandomSentence
import random
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('typing-tests')

# tests = SHEET.worksheet('tests')

# data = tests.get_all_values()
# print(data)

sent_list = []
sent_para = ""


for i in range(5):
    sent = RandomSentence()
    random_sent = sent.sentence()
    sent_list.append(random_sent)
    sent_para += random_sent + " "

print(sent_list)
print(sent_para)

