# https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b

import gspread
from google.oauth2.service_account import Credentials

from wonderwords import RandomSentence
import random
import time

from difflib import SequenceMatcher

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

def print_instructions():
    """
    Prints the instruction for the Speed Test
    """
    print("\n -- Instructions -- \n")
    print("1. The program generates a paragraph of short random sentences.\n")
    print("2. You will have to type the sentence as fast and as accurate as you can.\n")
    print("3. When you are ready to start enter y below and the paragraph will be generated.\n")
    print("4. You can then take time to look it over and enter y again when you are ready to start typing.\n")

def print_more_information():
    print("Insert text")

def generate_random_paragraph():
    """
    Create a paragraph of random sentences using wonderwords
    """
    sent_list = []
    sent_para = ""

    for i in range(3):
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
    speed = len(typed_para)/(time_taken/60)
    
    results = [typed_para, speed]

    return results

def error_rate(sent_para, typed_para):
    """
    Error rate is computed as a percentage of the length of the paragraph
    """
    error_count = 0
    print(sent_para)
    length = len(sent_para) - 1

    for character in range(length):
        try:
            if sent_para[character] != typed_para[character]:
                print(f"Try Error {sent_para[character]} vs {typed_para[character]}")
                error_count += 1
            else:
                continue   
        except:
            error_count += 1

    error_percent = error_count/length * 100
    typing_accuracy = 100 - error_percent

    sequence_match = 100 * SequenceMatcher(a=sent_para, b=typed_para).ratio()
    print(sequence_match)

    accuracy = [typing_accuracy, sequence_match]
    
    return accuracy

def main():

    # print("\n*** Welcome to the Speed Typing Test! ***\n")
    # print("What would you like to do?\n")
    # print("1. Read the instructions - enter 'i' below.\n")
    # print("2. Learn more about typical typing speeds - enter 'm' below.\n")
    # print("3. Start the test - enter 's' below.\n")

    # choice = input()
    # if choice == 'i':
    #     print_instructions()
    # elif choice == 'm':
    #     print_more_information()
    # elif choice == 's':
        
    # else:
    #     print('Your input is invalid. Exiting the game.')
    #     quit()

    print("Are you ready to see your paragraph? Enter y for yes and n for no")
    ready_para = input()
    if ready_para == 'y':
        paragraph = generate_random_paragraph()
    elif ready_para == 'n':
        print("Exiting the program")
        quit()
    else:
        print("your input is invalid, exiting the program")
        quit()
    
    print("\n---------------------------------------\n")
    print(paragraph)
    print("\n---------------------------------------\n")

    print("Are you ready to start typing? Enter y for yes and n for no")
    ready_type = input()
    if ready_type == 'y':
        print("\nStart Typing\n")
        test_results = typed_paragraph()
        test_speed = test_results[1]
        test_para = test_results[0]
    elif ready_type == 'n':
        print("Exiting the program")
        quit()
    else:
        print("your input is invalid, exiting the program")
        quit()    
    
    test_typing_accuracy = error_rate(paragraph, test_para)
    
    print("\n******** YOUR SCORE REPORT ********\n")
    print(f"Typing accuracy is {round(test_typing_accuracy[0],1)} % of characters in the paragraph.\n")
    print(f"Typing accuracy is {round(test_typing_accuracy[1],1)} % using SequenceMatch.\n")
    print(f"Speed is {round(test_speed,1)} characters/minute\n")
    print(f"that is approx. {round(test_speed/5,1)} words/minute\n")

main()
