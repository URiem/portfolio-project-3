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


def return_to_main():
    """
    Return the user to the beginning of the program
    """
    ent = input("\nHit enter when you are ready to return to the main menu.\n")
    if ent == "":
        clear()
        main()
    else:
        clear()
        main()


def initial_choices():
    """
    Allows the user several choices to display various information,
    exit or start the game.
    """
    cprint("\nMain Menu: What would you like to do?\n", attrs=["underline"])
    print("1. Read the test instructions.\n")
    print("2. Learn more about typical typing speeds.\n")
    print("3. Get tips on how to improve your score.\n")
    print("4. See your old scores and statistics.\n")
    print("5. Create a username to save results.\n")
    print("6. Delete a username and scoresheet.\n")
    print("7. Exit the game.\n")
    print("8. Start the test.\n")

    cprint("Enter the number of your choice here:\n", attrs=["bold"])
    choice = input()
    
    return choice


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

    return_to_main()


def print_more_information():
    """
    Print general information on average typing speeds and
    other useful or interesting information
    """
    print("\nInsert text\n")

    return_to_main()


def print_tips():
    """
    Print on how to improve typing speed and accuracy
    """
    print("\nInsert text\n")

    return_to_main()


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
                main()

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

    return_to_main()


def create_user_score_sheet():
    """
    Create a google spread sheet to save scores for a new user
    """
    headings = ["speed in cpm", "speed in wpm", "accuracy"]
    print("Enter your username:\n")
    username = input().lower()
    try:
        user_scoresheet = SHEET.worksheet(username)
        print("A sheet with this username already exist.\n")
        print("Do you you want to:\n")
        print("1. Choose a differnt username?\n")
        print("2. Return to main menu and record data to existing sheet?\n")
        print("Enter the number of your choice:\n")
        choice = input()
        if choice == '1':
            clear()
            create_user_score_sheet()
        elif choice == '2':
            clear()
            main()
    except gspread.exceptions.WorksheetNotFound:
        user_scoresheet = SHEET.add_worksheet(title=username, rows=100, cols=20)
        user_scoresheet.append_row(headings)
        print(f"Scoresheet for {username} has been created.\n")
        print("It can now be used to save scores of the test.\n")
        print("Returning to main menu")
        return_to_main()


def delete_score_sheet():
    """
    Delete a user score sheet
    """
    while True:
        try:
            print("Enter your username:\n")
            username = input().lower()
            user_scoresheet = SHEET.worksheet(username)
            print(f"\nA sheet with the name {username} exist.\n")
            print("Are you sure want to delete is?\n")
            print("Type 'yes' if are ready to delete the sheet,\n")
            print("type 'no' if you do not want to delete it and return to main menu.")
            choice = input()
            if choice == 'yes':
                SHEET.del_worksheet(user_scoresheet)
                print("The sheet has been deleted")
                return_to_main()
            elif choice == 'no':
                return_to_main()
            else:
                clear()
                print("Your input was invalid. Please try again")
                continue
        except gspread.exceptions.WorksheetNotFound:
            while True:
                print(f"A score sheet with the name {username} does not exist.\n")
                print("Do you want to:\n")
                print("1. Enter another username?\n")
                print("2. Return to the main menu?\n")
                print("Enter the number of your choice:\n")
                choice = input()
                if choice == '1':
                    clear()
                    delete_score_sheet()
                elif choice == '2':
                    return_to_main()
                else:
                    clear()
                    print("Your input was invalid. Please try again")
                    continue


def run_test_display_results():
    """
    Run the typing test and display the results
    """
    cprint("  *** Welcome to the Speed Typing Test! ***\n", "light_yellow")
    print("Are you ready to see your paragraph?\n")
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
        test_speed_cpm = round(test_results[1])
        test_speed_wpm = round(test_speed_cpm / 5)
        test_para = test_results[0]
    else:
        print("\n")
        test_results = typed_paragraph()
        test_speed_cpm = round(test_results[1])
        test_speed_wpm = round(test_speed_cpm / 5)
        test_para = test_results[0]

    test_typing_accuracy = determine_accuracy(paragraph, test_para)

    print("\n******** YOUR SCORE REPORT ********\n")
    print(f"Typing accuracy is {test_typing_accuracy} % of characters in the paragraph.\n")
    print(f"Speed is {test_speed_cpm} characters/minute\n")
    print(f"that is approx. {test_speed_wpm} words/minute\n")

    results = [test_speed_cpm, test_speed_wpm, test_typing_accuracy]

    return results


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


def determine_accuracy(sent_para, typed_para):
    """
    Accuracy is determined using SequenceMatcher
    """
    sequence_match = SequenceMatcher(a=sent_para, b=typed_para).ratio()
    result = round(100 * sequence_match, 1)

    return result


def save_score(data):
    """
    Save score to worksheet that matches the username
    """
    while True:
        try:
            print("Enter your username:\n")
            username = input().lower()
            user_scoresheet = SHEET.worksheet(username)
            print(f"Updating {username} scoresheet ...\n")
            user_scoresheet = SHEET.worksheet(username)
            user_scoresheet.append_row(data)
            print(f"{username} scoresheet updated successfully.\n")
            print("Returning to the starting page\n")
            time.sleep(3)
            main()
        except gspread.exceptions.WorksheetNotFound as e:
            print(f"Worksheet for {e} not found\n")
            print("Would you like to:\n")
            print("1. input a different username?\n")
            print("2. create a worksheet to save your scores?\n")
            print("3. return to the main menu?\n")
            choice = input()
            if choice == '1':
                continue
            elif choice == '2':
                headings = ["speed in cpm", "speed in wpm", "accuracy"]
                print("Enter your username:\n")
                username = input()
                user_scoresheet = SHEET.add_worksheet(title=username, rows=100, cols=20)
                user_scoresheet.append_row(headings)
                user_scoresheet.append_row(data)
                print(f"Scoresheet for {username} has been created and updated.\n")
                print("Returning to main menu")
                return_to_main()
            elif choice == '3':
                return_to_main()


def main():
    """
    Run all program functions
    """
    clear()
    cprint("  *** Welcome to the Speed Typing Test! ***\n", "light_yellow")

    choice = initial_choices()

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
            clear()
            create_user_score_sheet()
        elif choice == '6':
            clear()
            delete_score_sheet()
        elif choice == '7':
            print("Exiting the game")
            quit()
        elif choice == '8':
            clear()
            test_scores = run_test_display_results()
        else:
            raise ValueError
    except ValueError:
        clear()
        print(f"Invalid data: {choice}, please try again.\n")
        print("Returning to the starting page\n")
        time.sleep(3)
        main()

    print("\n **** What next? **** \n")
    print("1. Exit the program.\n")
    print("2. Return to main menu.\n")
    print("3. Save results.\n")
    now_what = input()
    if now_what == '1':
        print("\nThanks for taking the test! Come back soon!\n")
        quit()
    elif now_what == '2':
        main()
    elif now_what == '3':
        save_score(test_scores)
        main()
    else:
        print("Invalid input. Exiting the game")
        quit()


main()
