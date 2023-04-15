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
from statistics import mean
import pandas as pd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('typing-tests')


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
    cprint("\nWhat would you like to do?\n", attrs=["underline"])
    print("1. Read the test instructions.\n")
    print("2. Learn more about typical typing speeds.\n")
    print("3. Get tips on how to improve your score.\n")
    print("4. See your old scores and statistics.\n")
    print("5. Exit the game.\n")
    print("6. Start the test.\n")

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
            clear()
            see_old_scores_and_statistics()
        elif choice == '5':
            print("Exiting the game")
            quit()
        elif choice == '6':
            clear()
            cprint("\n*** Welcome to the Speed Typing Test! ***\n", "light_yellow")
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

    return_to_initial_choices()


def print_more_information():
    """
    Print general information on average typing speeds and
    other useful or interesting information
    """
    print("\nInsert text\n")

    return_to_initial_choices()


def print_tips():
    """
    Print on how to improve typing speed and accuracy
    """
    print("\nInsert text\n")

    return_to_initial_choices()


def see_old_scores_and_statistics():
    """
    Access google sheet with old scores and display scores and statistics
    in the terminal window
    """
    while True:
        try:
            print("Enter your username:\n")
            username = input().lower()
            user_scoresheet = SHEET.worksheet(username)
            break
        except gspread.exceptions.WorksheetNotFound as e:
            print(f"Worksheet for {e} not found\n")
            print("Would you like to:\n")
            print("1. enter a different username or\n")
            print("2. return to the previous screen?\n")
            choice = input()
            if choice == '1':
                continue
            if choice == '2':
                clear()
                initial_choices()

    print(f"\nThe collective test results for {username} are:\n")
    dataframe = pd.DataFrame(user_scoresheet.get_all_records())
    print(dataframe)

    user_speed_cpm_values = user_scoresheet.col_values(1)
    user_speed_wpm_values = user_scoresheet.col_values(2)
    user_accuracy_values = user_scoresheet.col_values(3)

    int_speed_cpm = [eval(i) for i in user_speed_cpm_values[1:]]
    int_speed_wpm = [eval(i) for i in user_speed_wpm_values[1:]]
    int_accuracy = [eval(i) for i in user_accuracy_values[1:]]

    avg_speed_cpm = round(mean(int_speed_cpm))
    avg_speed_wpm = round(mean(int_speed_wpm))
    avg_accuracy = round(mean(int_accuracy), 1)

    print(f"\nStatistics for {username}\n")
    print(f"Your average speed is {avg_speed_cpm} characters per minute\n")
    print(f"That is approx. {avg_speed_wpm} words per minute\n")
    print(f"Your average accuracy is {avg_accuracy}%\n")

    return_to_initial_choices()


def return_to_initial_choices():
    ent = input("Hit enter when you are ready to continue\n")
    if ent == "":
        clear()
        initial_choices()
    else:
        clear()
        initial_choices()


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
    speed = round(len(typed_para)/(time_taken/60), 1)

    results = [typed_para, speed]

    return results


def determine_accuracy(sent_para, typed_para):
    """
    Accuracy is determined using SequenceMatcher
    """
    sequence_match = SequenceMatcher(a=sent_para, b=typed_para).ratio()
    result = round(100 * sequence_match, 1)

    return result


def save_score(speed_cpm, speed_wpm, accuracy):
    """
    Save score to worksheet that matches the username
    """

    data = [round(speed_cpm), round(speed_wpm), round(accuracy, 1)]
    print("Enter your username:")
    username = input()
    print(f"Updating {username} scoresheet ...\n")
    user_scoresheet = SHEET.worksheet(username)
    user_scoresheet.append_row(data)
    print(f"{username} scoresheet updated successfully.\n")

    initial_choices()


def main():
    """
    Run all program functions
    """
    clear()

    cprint("\n*** Welcome to the Speed Typing Test! ***\n", "light_yellow")

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
        test_speed_cpm = test_results[1]
        test_speed_wpm = test_speed_cpm / 5
        test_para = test_results[0]
    else:
        print("\n")
        test_results = typed_paragraph()
        test_speed_cpm = test_results[1]
        test_speed_wpm = test_speed_cpm / 5
        test_para = test_results[0]

    test_typing_accuracy = determine_accuracy(paragraph, test_para)

    print("\n******** YOUR SCORE REPORT ********\n")
    print(f"Typing accuracy is {test_typing_accuracy} % of characters in the paragraph.\n")
    print(f"Speed is {round(test_speed_cpm)} characters/minute\n")
    print(f"that is approx. {round(test_speed_wpm)} words/minute\n")

    print("\n **** What next? **** \n")
    print("1. Exit\n")
    print("2. Test again\n")
    print("3. Save results\n")
    now_what = input()
    if now_what == '1':
        print("\nThanks for taking the test! Come back soon!\n")
        quit()
    elif now_what == '2':
        main()
    elif now_what == '3':
        save_score(test_speed_cpm, test_speed_wpm, test_typing_accuracy)
        main()
    else:
        print("Invalid input. Exiting the game")
        quit()


main()
