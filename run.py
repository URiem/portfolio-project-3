# https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b
# to test code use: pycodestyle run.py
import gspread
from google.oauth2.service_account import Credentials

from wonderwords import RandomSentence
import random
import time
import os 
from os import system, name
from difflib import SequenceMatcher
from termcolor import colored, cprint

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

def clear():
    """
    Clear the terminal window when new text section is displayed
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def initial_choices():
    """
    Allows the user several choices to display various information,
    exit or start the game.
    """
    cprint("\nWhat would you like to do?\n",attrs=["underline"])
    print("1. Read the test instructions.\n")
    print("2. Learn more about typical typing speeds.\n")
    print("3. Get tips on how to improve your score.\n")
    print("4. Exit the game.\n")
    print("5. Start the test.\n")

    cprint("Enter the number of your choice here:\n", attrs=["bold"])
    choice = input()
    try:
        if choice == '1':
            clear()
            print_instructions()
        elif choice == '2':
            clear()
            print_more_information()
        elif choice == '3':
            clear()
            print_tips()
        elif choice == '4':
            print("Exiting the game")
            quit()
        elif choice == '5':
            clear()
            cprint("\n*** Welcome to the Speed Typing Test! ***\n","light_yellow")
        else:
            raise ValueError
    except ValueError:
        clear()
        print(f"Invalid data: {choice}, please try again.\n")
        initial_choices()


def print_instructions():
    """
    Prints the instruction for the Speed Test
    """
    print("\n -- Instructions -- \n")
    print("1. Read and follow prompts closely as you navigate through the program.\n")
    print("2. When you are ready the program generates a paragraph of short random sentences.\n")
    print("3. When you are ready type the provided paragraph as quickly and accurately as possible.\n")
    print("4. Hit enter when you are done typing.\n")
    print("5. Your score of accuracy and speed will then be calculated and displayed.\n")
    print("6. You will then be able to choose to exit the program or play again.\n")
    ent = input("Hit enter when you are ready to continue\n")
    if ent == "":
        clear()
        choice = initial_choices()
    else:
        clear()
        choice = initial_choices()


def print_more_information():
    """
    Print general information on average typing speeds and
    other useful or interesting information
    """
    print("\nInsert text\n")

    ent = input("Hit enter when you are ready to continue\n")
    if ent == "":
        clear()
        choice = initial_choices()
    else:
        clear()
        choice = initial_choices()


def print_tips():
    """
    Print on how to improve typing speed and accuracy
    """
    print("\nInsert text\n")

    ent = input("Hit enter when you are ready to continue\n")
    if ent == "":
        clear()
        choice = initial_choices()
    else:
        clear()
        choice = initial_choices()


def generate_random_paragraph():
    """
    Create a paragraph of random sentences using wonderwords
    """
    sent_list = []
    sent_para = ""

    for i in range(2):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent + " "

    test_para = sent_para[:-1]

    return test_para


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
    # error_count = 0
    # print(sent_para)
    # length = len(sent_para) - 1

   
    sequence_match = 100 * SequenceMatcher(a=sent_para, b=typed_para).ratio()

    # for character in range(length):
    #     try:
    #         if sent_para[character] != typed_para[character]:
    #             error_count += 1
    #         else:
    #             continue
    #     except:
    #         error_count += 1

    # error_percent = error_count/length * 100
    # typing_accuracy = 100 - error_percent

    # accuracy = [typing_accuracy, sequence_match]

    return sequence_match

def save_score(speed, accuracy):

    data = [speed, accuracy]
    print("Enter your username:")
    username = input()
    print(f"Updating {username} scoresheet ...\n")
    scoresheet_to_update = SHEET.worksheet(username)
    scoresheet_to_update.append_row(data)
    print(f"{username} scoresheet updated successfully.\n")


def main():
    clear()

    cprint("\n*** Welcome to the Speed Typing Test! ***\n","light_yellow")

    initial_choices()

    print("\nAre you ready to see your paragraph?\n")
    ent = input("Hit enter when you are ready to continue")
    if ent == "":
        paragraph = generate_random_paragraph()
        print("\n---------------------------------------\n")
        print(paragraph)
        print("\n---------------------------------------\n")
    else:
        paragraph = generate_random_paragraph()
        print("\n---------------------------------------\n")
        print(paragraph)
        print("\n---------------------------------------\n")

    ent = input("Hit enter when you are ready to start typing")
    if ent == "":
        print("\n")
        test_results = typed_paragraph()
        test_speed = test_results[1]
        test_para = test_results[0]
    else:
        print("\n")
        test_results = typed_paragraph()
        test_speed = test_results[1]
        test_para = test_results[0]

    test_typing_accuracy = error_rate(paragraph, test_para)

    print("\n******** YOUR SCORE REPORT ********\n")
    # print(f"Typing accuracy is {round(test_typing_accuracy[0],1)} % of characters in the paragraph.\n")
    print(f"Typing accuracy is {round(test_typing_accuracy,1)} % of characters in the paragraph.\n")
    print(f"Speed is {round(test_speed,1)} characters/minute\n")
    print(f"that is approx. {round(test_speed/5,1)} words/minute\n")

    print("\n **** What next? **** \n")
    print("1. Exit (e)\n")
    print("2. Test again (t)\n")
    print("3. Save results (s)\n")
    now_what = input()
    if now_what == 'e':
        print("\nThanks for taking the test! Come back soon!\n")
        quit()
    elif now_what == 't':
        main()
    elif now_what == 's':
        save_score(test_speed,test_typing_accuracy)
        initial_choices()
    else:
        print("Invalid input. Exiting the game")
        quit()


main()
