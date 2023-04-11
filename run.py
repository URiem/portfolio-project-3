# https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b

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

def generate_random_paragraph():
    """
    Create a paragraph of random sentences using wonderwords
    """
    sent_list = []
    sent_para = ""

    for i in range(1):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent + " "

    return sent_para

def typed_paragraph():
    """
    This function captures the typed paragraph from the user and
    measures the time taken to type the paragraphy
    """
    
    start_time = time.time()
    typed_para = input()
    end_time = time.time()

    time_taken = end_time - start_time
    speed = len(typed_para)/time_taken
    
    results = [typed_para, speed]

    return results

def error_rate(sent_para, typed_para):
    """
    Error rate is computed as a percentage of the length of the paragraph
    """
    error_count = 0

    length = len(sent_para)

    for character in range(length):
        try:
            if sent_para[character] != typed_para[character]:
                error_count += 1
            
        except:
            error_count += 1
        
    error_percent = error_count/length * 100
    return error_percent

def main():

    print("\nWelcome to the Speed Typing Test!\n")
    print("\n -- The Rules -- \n")
    print("1. The program generates a paragraph of short random sentences.\n")
    print("2. You will have to type the sentence as fast and as accurate as you can.\n")
    print("3. When you are ready to start enter y below and the paragraph will be generated.\n")
    print("4. You can then take time to look it over and enter y again when you are ready to start typing.\n")

    print("Are you ready to see your paragraph? Enter y for yes and n for no")
    ready_para = input()
    if ready_para == 'y':
        paragraph = generate_random_paragraph()
    elif ready_para == 'n':
        print("Exiting the program")
        quit()
    else:
        print("your input is invalid, try again")
        main()
    
    print("Type the paragraphy below as quickly as possible with as few mistakes to get the highest score: \n")
    print("\n---------------------------------------\n")
    print(paragraph)
    print("\n---------------------------------------\n")

    print("Are you ready to start typing? Enter y for yes and n for no")
    ready_type = input()
    if ready_type == 'y':
        print("\nStart Typing\n")
        test_results = typed_paragraph()
        test_speed = test_results[1]
        print(f"\nTime speed in characters/seconds: {test_speed}")
        test_para = test_results[0]
    elif ready_type == 'n':
        print("Exiting the program")
        quit()
    else:
        print("your input is invalid, exiting the program")
        quit()    
    
    test_error_rate = error_rate(paragraph, test_para)
    print(f"\nError rates as a percentage of the length of the paragraph: {test_error_rate}")


main()
