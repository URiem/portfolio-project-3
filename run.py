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

    cprint("*** Welcome to the Speed Typing Test! ***\n", "light_yellow")


def return_to_main():
    """
    Return the user to the beginning of the program
    """
    cprint("\nHit enter when you are ready to return to the main menu.\n", "green", attrs=["bold"])
    ent = input()
    if ent == "":
        clear()
        main()
    else:
        clear()
        main()


def main_menu():
    """
    Allows the user several choices to display various information,
    exit or start the game.
    """
    cprint("Main Menu: What would you like to do?\n", attrs=["underline", "bold"])
    print("1. Read the test instructions.\n")
    print("2. Learn more about typical typing speeds.\n")
    print("3. Get tips on how to improve your score.\n")
    print("4. See your old scores and statistics.\n")
    print("5. Create a username to save results.\n")
    print("6. Delete a username and scoresheet.\n")
    print("7. Start the test.\n")
    print("8. Exit the program.\n")

    cprint("Enter the number of your choice here:\n", "green", attrs=["bold"])
    choice = input()

    return choice


def print_instructions():
    """
    Prints the instruction for the Speed Test
    """
    cprint("\nInstructions\n", attrs=["underline", "bold"])
    print("* Read and follow prompts closely as you navigate through the program.\n")
    print("* When you encounter a choice menu, make sure to enter a valid choice.\n")
    print("* When you are ready to take the test, the program generates a paragraph of short random sentences.\n")
    print("* When you are ready, type the provided paragraph as quickly and accurately as possible.\n")
    print("* Hit enter when you are done typing.\n")
    print("* Your scores, including accuracy and speed will then be calculated and displayed.\n")
    print("* You will then be able to choose to save your score or return to the main menu.\n")

    return_to_main()


def print_more_information():
    """
    Print general information on average typing speeds and
    other useful or interesting information
    """
    cprint("\nDid you know?\n", attrs=["underline", "bold"])
    print("The QWERTY keyboard layout is standard on nearly every keyboard")
    print("and phone in the English-speaking world. Currently, the average typing")
    print("speed on a QWERTY layout for an adult who uses typing for their job")
    print("is around 40 WPM. Touch typists using the home-row method are typically")
    print("faster typists because they don’t look down at the keyboard and")
    print("type from muscle memory. Hunt and peck typists typically use two-fingers")
    print("and look at the keys as they type, so it takes them longer to find the letters.\n")
    print("\nOfficially, the fastest typist in the world is Barbara Blackburn,")
    print("who has reached top speeds of 212 wpm on a Dvorak keyboard. She was able")
    print("to maintain a speed of 150 wpm for 50 minutes. Barbara has held this")
    print("record since 2005.\n")

    return_to_main()


def print_tips():
    """
    Print on how to improve typing speed and accuracy
    """
    cprint("\nHow can you improve?\n", attrs=["underline", "bold"])
    print("* Familiarize yourself with the keyboard and proper hand position.\n")
    print("* Learn proper overall positioning of the screen and your body.\n")
    print("* Start by typing slowly to avoid mistakes.\n")
    print("* Practice, practice, practice.\n")
    print("* Go to the internet to find more detailed advice.\n")

    return_to_main()


def see_old_scores_and_statistics():
    """
    Access google sheet with old scores and display scores and statistics
    in the terminal window
    """
    while True:
        try:
            cprint("Enter your username to see your scores and statistics:\n", "green", attrs=["bold"])
            username = input().lower()
            user_scoresheet = SHEET.worksheet(username)
            break
        except gspread.exceptions.WorksheetNotFound:
            while True:
                print(f"\nWorksheet for '{username}' not found\n")
                cprint("Would you like to:\n", attrs=["bold", "underline"])
                print("1. enter a different username or\n")
                print("2. return to the main menu?\n")
                cprint("Please enter your numeric choice:\n", "green", attrs=["bold"])
                choice = input()
                if choice == '1':
                    clear()
                    see_old_scores_and_statistics()
                elif choice == '2':
                    clear()
                    main()
                else:
                    cprint("Your input is invalid. Please try again.\n", "red", attrs=["bold"])
                    continue

    cprint(f"\nThe collective test results for '{username}' are:\n", attrs=["bold", "underline"])
    dataframe = pd.DataFrame(user_scoresheet.get_all_records())
    print(dataframe)
    if dataframe.empty:
        print('\nThere are not data in the worksheet yet.')
        print('\nRun at least one test and save the score.')
        return_to_main()

    try:
        user_speed_cpm_values = user_scoresheet.col_values(1)
        user_speed_wpm_values = user_scoresheet.col_values(2)
        user_accuracy_values = user_scoresheet.col_values(3)

        int_speed_cpm = [eval(i) for i in user_speed_cpm_values[1:]]
        int_speed_wpm = [eval(i) for i in user_speed_wpm_values[1:]]
        int_accuracy = [eval(i) for i in user_accuracy_values[1:]]

        avg_speed_cpm = round(mean(int_speed_cpm))
        avg_speed_wpm = round(mean(int_speed_wpm))
        avg_accuracy = round(mean(int_accuracy), 1)

        cprint(f"\nStatistics for '{username}'\n", attrs=["bold", "underline"])
        print(f"Your average speed is {avg_speed_cpm} characters per minute\n")
        print(f"That is approx. {avg_speed_wpm} words per minute\n")
        print(f"Your average accuracy is {avg_accuracy}%\n")
    except SyntaxError:
        print('\n')
        cprint("A Syntax Error has occured and statistics can not be computed.\n", "red", attrs=["bold"])
        cprint("The data file may be corrupted.\n", "red", attrs=["bold"])
        cprint("From the main menu you can delete the file and create a new one.", "red", attrs=["bold"])

    return_to_main()


def create_user_score_sheet():
    """
    Create a google spread sheet to save scores for a new user
    """
    headings = ["speed in cpm", "speed in wpm", "accuracy"]
    cprint("Enter your username for a new score sheet:\n", "green", attrs=["bold"])
    username = input().lower()
    while True:
        try:
            user_scoresheet = SHEET.worksheet(username)
            cprint(f"\nA sheet with the name {username} already exist.\n", attrs=["bold", "underline"])
            cprint("Do you you want to:\n", attrs=["bold", "underline"])
            print("1. Choose a differnt username?\n")
            print("2. Return to main menu and record data to existing sheet?\n")
            cprint("Enter your numeric choice:\n", "green", attrs=["bold"])
            choice = input()
            if choice == '1':
                clear()
                create_user_score_sheet()
            elif choice == '2':
                clear()
                main()
            else:
                clear()
                cprint("Your input was invalid. Please try again", "red", attrs=["bold"])
                continue
        except gspread.exceptions.WorksheetNotFound:
            user_scoresheet = SHEET.add_worksheet(title=username, rows=100, cols=20)
            user_scoresheet.append_row(headings)
            cprint(f"\nScoresheet for '{username}' has been created.\n", attrs=["bold", "underline"])
            print("It can now be used to save scores of the test.\n")
            return_to_main()


def delete_score_sheet():
    """
    Delete a user score sheet
    """
    while True:
        try:
            cprint("Enter username for the scoresheet you want to delete:\n", "green", attrs=["bold"])
            username = input().lower()
            if username == 'test':
                print(f"The score sheet '{username}' cannot be deleted\n")
                return_to_main()
            user_scoresheet = SHEET.worksheet(username)
            while True:
                cprint(f"\nA sheet with the name '{username}' exist.\n", attrs=["bold", "underline"])
                cprint("Are you sure want to delete it?\n", attrs=["bold", "underline"])
                cprint("Type 'yes' if are ready to delete the sheet,\n", "green", attrs=["bold"])
                cprint("type 'no' if you do not want to delete it and return to main menu.\n", "green", attrs=["bold"])
                choice = input()
                if choice == 'yes':
                    SHEET.del_worksheet(user_scoresheet)
                    cprint(f"\nThe sheet '{username}' has been deleted", attrs=["bold", "underline"])
                    return_to_main()
                elif choice == 'no':
                    clear()
                    main()
                else:
                    clear()
                    cprint("Your input was invalid. Please try again", "red", attrs=["bold"])
                    continue
        except gspread.exceptions.WorksheetNotFound:
            while True:
                cprint(f"A score sheet with the name '{username}' does not exist.\n", attrs=["bold", "underline"])
                print("Do you want to:\n")
                print("1. Enter another username?\n")
                print("2. Return to the main menu?\n")
                cprint("Enter the number of your choice:\n", "green", attrs=["bold"])
                choice = input()
                if choice == '1':
                    clear()
                    delete_score_sheet()
                elif choice == '2':
                    clear()
                    main()
                else:
                    clear()
                    cprint("Your input was invalid. Please try again", "red", attrs=["bold"])
                    continue


def run_test_display_results():
    """
    Run the typing test and display the results
    """
    # cprint("Are you ready to see your paragraph?\n", attrs=["bold", "underline"])
    ent = input(colored("Hit enter when you are ready to see the paragraph.\n", "green", attrs=["bold"]))
    if ent == "":
        paragraph = generate_random_paragraph()
        cprint("\n***********************************************\n", attrs=["bold"])
        cprint(paragraph, "white", attrs=["bold"])
        cprint("\n***********************************************\n", attrs=["bold"])
    else:
        paragraph = generate_random_paragraph()
        cprint("***********************************************\n", attrs=["bold"])
        cprint(paragraph, "white", attrs=["bold"])
        cprint("\n***********************************************\n", attrs=["bold"])

    ent = input(colored("Hit enter when you are ready to start typing.\n", "green", attrs=["bold"]))
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

    cprint("\n******** YOUR SCORE REPORT ********\n", "yellow")
    cprint(f"Typing accuracy is {test_typing_accuracy} % of characters in the paragraph.\n", attrs=["bold"])
    cprint(f"Speed is {test_speed_cpm} characters/minute\n", attrs=["bold"])
    cprint(f"that is approx. {test_speed_wpm} words/minute\n", attrs=["bold"])

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


def post_test_choice(data):
    """
    User gets a choice to save the data or return to the main menu
    """
    cprint("\nWhat next?\n", attrs=["bold", "underline"])
    print("1. Save results.\n")
    print("2. Return to main menu.\n")
    cprint("Please enter your numeric choice:\n", "green", attrs=["bold"])
    now_what = input()
    while True:
        try:
            if now_what == '1':
                save_score(data)
                return_to_main()
            elif now_what == '2':
                clear()
                main()
            else:
                raise ValueError
        except ValueError:
            cprint("\nYour input was invalid. Please try again.\n", "red", attrs=["bold"])
            post_test_choice(data)


def save_score(data):
    """
    Save score to worksheet that matches the username
    """
    while True:
        try:
            cprint("\nEnter your username to save the score:\n", "green", attrs=["bold"])
            username = input().lower()
            user_scoresheet = SHEET.worksheet(username)
            print(f"\nUpdating '{username}' scoresheet ...\n")
            user_scoresheet = SHEET.worksheet(username)
            user_scoresheet.append_row(data)
            cprint(f"'{username}' scoresheet updated successfully.\n", attrs=["bold", "underline"])
            return_to_main()
        except gspread.exceptions.WorksheetNotFound:
            while True:
                cprint(f"\nWorksheet for '{username}' not found\n", attrs=["bold", "underline"])
                cprint("Would you like to:\n", attrs=["bold", "underline"])
                print("1. input a different username?\n")
                print("2. create a worksheet to save your scores?\n")
                print("3. return to the main menu?\n")
                cprint("Please enter your numeric choice:\n", "green", attrs=["bold"])
                choice = input()
                if choice == '1':
                    continue
                elif choice == '2':
                    headings = ["speed in cpm", "speed in wpm", "accuracy"]
                    user_scoresheet = SHEET.add_worksheet(title=username, rows=100, cols=20)
                    user_scoresheet.append_row(headings)
                    user_scoresheet.append_row(data)
                    cprint(f"\nScoresheet for '{username}' has been created and updated.\n", attrs=["bold", "underline"])
                    return_to_main()
                elif choice == '3':
                    clear()
                    main()
                else:
                    cprint(f"\nInvalid data: {choice}, please try again.\n", "red", attrs=["bold"])
                    continue


def main():
    """
    Run all program functions
    """
    clear()

    choice = main_menu()

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
            clear()
            test_scores = run_test_display_results()
            post_test_choice(test_scores)
        elif choice == '8':
            cprint("\nExiting the program.\n", "magenta", attrs=["bold"])
            cprint("Thanks for checking it out!\n", "magenta", attrs=["bold"])
            cprint("Come back soon!\n", "magenta", attrs=["bold"])
            quit()
        else:
            raise ValueError
    except ValueError:
        cprint(f"\nInvalid data: {choice}, please try again.\n", "red", attrs=["bold"])
        return_to_main()


main()
