# Speed Typing Test
(Developer: Ulrike Riemenschneider)

![Mockup image](docs/iamresponsive.png)

[Live webpage](https://speed-typing-test.herokuapp.com/)

## Table of Content

1. [Introduction](#introduction)
2. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
    1. [Strategy](#strategy)
        * [Target Audience](#target-audience)
        * [User Requirements & Expectations](#user-requirements-and-expectations)
        * [User Stories](#user-stories)
    2. [Scope](#scope)
        * [Initial Stage](#intial-stage)
        * [Future Additions](#future-additions)
    3. [Structure](#structure)
    4. [Flowchart](#flowchart)
    5. [Surface](#surface)
        * [Color Scheme](#color-scheme)
        * [Font](#font)
    5. [Features](#features)
        * [Main Menu](#main-menu)
        * [Information Sections](#information-sections)
        * [Scoresheet Sections](#score-sheet-sections)
        * [Testing Section](#testing-section)
        * [Exit Test](#exit-test)
        * [Future Additions](#future-additions)
4. [Technologies Used](#technologies-used)
    1. [Language](#languages)
    2. [Frameworks & Tools](#frameworks--tools)
    3. [Helpful Sites](#helpful-sites)
5. [Testing and Validation](#testing-and-validation)
    1. [PEP8 Python Linter](#pep8-ci-python-linter)
    2. [HTML Validation](#html)
    3. [CSS Validation](#css)
    4. [Lighthouse Testing](#lighthouse)
    5. [User Stories](#user-stories)
    6. [Manual Testing](#manual-testing)
6. [Bugs & Fixes](#bugs--fixes)
7. [Deployment & Development](#deployment--development)
8. [Google Sheet Access](#google-sheet-access)
9. [Credits](#credits)


## Introduction

The Speed and Accuracy Typing Test is designed to give users a chance to test their typing skills in terms of speed and accuracy. It also gives users the opportunity to access information on what constitues a good average score and how to improve their skills and score. Users can create a score sheet to save their results, they can access past data and calculate averages. The can also delete their score sheet. The program is designed in Python and is run through a terminal window.

## Project Goals

### User Goals
- The site's user wants to test their typing skills in terms of speed and accuracy.
- The user wants to save results and track their progress.

### Site Owner Goals
- The site owner's goal is to provided an intuitive and easy to use application that allows a user to test their typing skills.
- The owner's goal is to encourage the user to return to the test in the future to retest their skill and review previous results.

## User Experience

### Strategy

#### Target Audience
- Users interested in testing and monitoring their typing skills.
- Users entering a field of work where typing is important and who are trying to improve this skill.

#### User Requirements and Expectations
- Simple and intuitive navigation system.
- Clear instructions and process flow.
- Immediate feedback on results.

#### User Stories

##### First-time User
As a first time user, I want to ...
1. ... read instructions.
2. ... easily and intuitively move through the test.
3. ... get easily understandable results.
4. ... understand how my score fits in with standard averages.
5. ... learn how I can improve my score.
6. ... save my results.

##### Returning Users
As a returning user, I want to ...
1. ... retake the test to see if my score has improved.
2. ... access previous results.
3. ... delete a scoresheet.

##### Site owner
As the site owner, I want to ...
1. ... develop an application that is easy to use.
2. ... provide clear instructions of the application.
3. ... provide the user with additional information on how to improve.
4. ... provide the user with background information on speed typing.
5. ... allow the user to save their scores and return to retest and improve their scores.

### Scope

#### Intial Stage

At the initial stage the application will include a main menu where the user can choose from a few option to obtain information, such as instructions, information on average typing speeds, and information on how to improve their typing skills. The user can also opt to create a username and score sheet to record results, they can review old results and delete a previously created and populated score sheet. Then the user will be able to run the test and see immediate feedback in the form of a typing speed in characters/mintues and words/minute as well as a percentage accuracy. 

#### Future Additions

Currently a python library called 'Wonderwords' is used to create a short string of sentences for the user to copy into the terminal window. The sentences are, for the most part, nonsensical and simply serve the purpose of testing the users ability to type text by copying it from the terminal window. In a future edition of the application the developer would like to integrate ChatGPT so the user has the option to create custom text with meaning and context, which can then be used in the typing test.

### Structure

The structure of the site itself consists of a one page website display that contains a terminal window. The Speed Typing Test is run in the terminal window. Above the terminal window a heading 'Speed Typing Test' is displayed, as well as a button that allows the user to restart the program as many times as desired.

### Flowchart/Skeleton

The following flow chart illustrates the approximate flow of the program and choices the user can make.

![Flowchart](docs/flowchart.png)


### Surface

To add visual appeal to the site, the surface has been modified slightly from the provided CI template. The terminal window is centered in the browser and a background picture featuring an image of a keyboard was choosen to fit with the theme of the application. 

#### Color Scheme

The background picture has light grey shades to maintain contrast between the background and the terminal window.

The button above the terminal window is a bright green color so that it lifts out from the page and calls for action. 

The text in the terminal window is colored depending on the type of information displayed or action called for. Menu options are generally displayed in plain white text. User input is requested in green text. Errors are displayed in red. The welcome and score headings are yellow. Important information and subheadings are in white, bold and underlined. 

#### Font

The font of the heading is Special Elite, which emulates the look of a classic type writer font.

### Features

#### Main Menu

- A welcome message is displayed and the user can choose from a main menu of 8 option how to proceed.

![Main Menu](docs/mainmenu.png)

#### Information Sections

- Instructions: Here the user can read the instructions for the test.

![Instruction](docs/instructions.png)

- General Information: Here the user can optain information on typical typing speeds and the world record in speed typing.

![General Information](docs/generalinformation.png)

- How to improve: Here the user can get a few pointers on how to improve accuracy and speed of typing.

![How To Improve](docs/howtoimprove.png)

#### Score Sheet Sections

- Access past scores: Here the user can access a previously saved scoresheet and see individual results and averages. 

![Access Scoresheet](docs/accessscoresheettop.png)

- Create a scoresheet: Here the user can enter a username and create a scoresheet.

![Create A Scoresheet](docs/createscoresheet.png)

- Delete a scoresheet: Here the user can enter a username and delete a scoresheet with that name if it exists.

![Delete A Scoresheet](docs/deletescoresheet.png)

#### Testing Section

- Here the test is run. The user will be prompted to hit enter while moving through several steps until he/she is prompted to start typing and hit enter to complete the test.

- The score is then displayed. Accuracy is given as a percentage. Speed is displayed in characters per minute and words per minute.

- The user can then choose to exit the test, save the scores or test again.

![Test Section](docs/testandresults.png)

![Post Test Options](docs/endoftestoptions.png)

#### Exit Test

- The final choice in the main  menu is for the user to exit the program.

![Exit Program](docs/exitprogram.png)


#### Future Additions

At this time the paragraph of random sentences created using 'wonderwords' is fairly nonsensical. In the future the developer would like to implement a simply routine that allows the user to request a short paragraph of text using ChatGPT on a topic of their choice. 

Because the only purpose of the paragraph is to test speed and accuracy of typing, the developer does not feel that it detracts from the purpose of the test to have meaningless text as the current test material. 

**Preliminary research on integrating ChatGPT.**

A repository has been created with a simple python program derived from online resources, to test the basic functionality of ChatGPT within a phython structure. Further development is needed in order to adapt this structure and integrate it into the Speed Typing Test.

[ChatGPT Repository](https://github.com/URiem/chatgpt-trial)

**ChatGPT Resources**

- [Geeks for Geeks](https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/)
- [Rollbar](https://rollbar.com/blog/how-to-integrate-chatgpt-into-your-python-script/)


## Technologies Used

### Languages
- Python

#### Python Libraries

The following libraries are standard in python and come preinstalled to deal with a variety of contextual issues:

- Time
- OS
- Difflib
- Statistics
- Ast

The following libraries where specifically installed to fascilitate various processes specific to this application:

- Gspread: Fascilitates the access to and manipulation of a Google Speadsheet to save and manipulate data.
- Wonderwords: Fascilitates the generation of a random paragraph used in the typing test.
- Termcolor: Helps in making the program  more visually appealing and easier to navigate.
- Pandas: Was used to display a data table in the terminal for easier readability.

### Frameworks & Tools
- Git
- GitHub
- Gitpod
- Heroku
- Google Spreadsheets
- Lucidchart
- CI Python Linter
- W3C HTML and CSS Validation Service

### Helpful sites

Several sites came in handy while developing the code to help with problem solving:

- [W3 Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com)
- [mdn web docs](https://developer.mozilla.org/)
- [Geekflare](https://geekflare.com/python-remove-last-character/)

## Testing and Validation

### PEP8 CI Python Linter

- No errors found when testing the python code from run.py in the PEP8 CI Python Linter.

![Python Testing](docs/cipythonlinter.png)

### HTML

- No errors or warnings found during HTML validation using W3C Markup Validation Service.

![HTML Validation](docs/htmltesting.png)

### CSS

- No errors found when validating the CSS using the W3C CSS Validation Service.

![CSS Validation](docs/csstesting.png)

### Lighthouse

- Excellent scores for Performance, Accessiblity and Best Practises in Lighthouse.

![Lighthouse Testing](docs/lighthousetesting.png)

### Testing User Stories

**As a first time user, I want to ...**
1. ... read instructions.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 1 | Instructions display in the terminal window | Works as expected |

2. ... easily and intuitively move through the test.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 7 | Test begins | Works as expected |
| Test | Follow clear instructions to navigate the test | Test completed step by step | Works as expected |
| End of Test | Make a choice how to proceed | Choice executed | Works as expected |

3. ... get easily understandable results.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| End of test | Finish test | Scores are automatically displayed in terms of speed in characters per minute and words per minute as well as accuracy as a percentage | Works as expected |

4. ... understand how my score fits in with standard averages.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 2 | General information about typing speeds is displayed | Works as expected |

5. ... learn how I can improve my score.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 3 | Information on how to improve the score is displayed | Works as expected |

6. ... save my results.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 5 | Create a username to save results | Works as expected |
| End of Test | Save results | Results can be saved to a new or existing score sheet | Works as expected |


**As a returning user, I want to ...**
1. ... retake the test to see if my score has improved.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 7 | Test begins | Works as expected |
| End of test | Save results to existing score sheet | Results are saved to a previously populated score sheet | Works as expected |
| Main Menu | Choose option 4 and input saved scoresheet name | Previous results and averages are displayed | Works as expected | 

2. ... access previous results.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 4 and input saved scoresheet name | Previous results and averages are displayed | Works as expected | 

3. ... delete a score sheet.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 6 and input saved scoresheet name to be deleted follow prompts | Scoresheet will be deleted | Works as expected | 


**As the site owner, I want to ...**
1. ... develop an application that is easy to use.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose an option | Option is executed | Works as expected |
| Return to Main Menu | At the end of each option return to menu is an option | User is taken back to the main menu | Works as expected |

2. ... provide clear instructions of the application.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 1 | Instructions display in the terminal window | Works as expected |

3. ... provide the user with additional information on how to improve.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 3 | Information on how to improve the score is displayed | Works as expected |

4. ... provide the user with background information on speed typing.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Choose option 2 | General information about typing speeds is displayed | Works as expected |

5. ... allow the user to save their scores and return to retest and improve their scores.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| End of test | Save results to existing or new score sheet | Results are saved to a score sheet | Works as expected |
| Return to main menu | At the end of test, save results and return to main menu | Main menu is displayed | Works as expected |
| Main Menu | Choose option 7 | Test begins again | Works as expected |
| Main Menu | Choose option 4 and input saved scoresheet name | Previous results and averages are displayed | Works as expected | 

### Manual Testing

The flow of the program was tested extensively using valid and invalid input data at every stage. All errors that did occur during this testing phase were fixed. No more errors should occur. 


### Outstanding Issues

There are currently no outstanding issues that the developer is aware of.


## Bugs & Fixes

| **Bug** | **Fix** |
| ----------- | ----------- |
| It was seemingly impossible to get a 100% score on the test. This was due to a whitespace at the end of the random string created. | Stripping the whitespace from the end of the string fixed the problem.|
| By chance a 'corrupted' worksheet was being read, which created an error. | Data validation was added to prevent an error in reading the data off the spreadsheet. |


## Deployment & Development

The website was deployed on Heroku. The following steps were followed in order for a commplete and functional deployment:

1. The requirements.txt file was populated using the command "pip3 freeze > requirements.txt'
2. Any text inside the 'input()' function in the run.py file had a 'new line' command (\n) added in order to work properly with the Code Institute template.
3. Once loged into the Heroku dashboard, a new app was created by clicking on the button 'New' and select 'Create New App'.
5. The app was named 'speed-typing-test' and region 'Europe' selected.
6. Under 'Setting' in the newly created app, 'Reveal Config Vars' was clicked in order to set environment variables such as sensitive information.
7. For in the input field labled 'KEY' the word 'CREDS' was entered, all capitals.
8. The entire contents of the projects creds.json file was pasted into the 'VALUE' field.
9. A second config var was added with the KEY set to 'PORT' and the VALUE set to '8000'.
10. Each time 'ADD' was clicked in order to add the config var.
11. Next, still under the settings tab, Buildpacks were added.
12. 'Add Buildpack' was clicked and python was selected, then 'Save Changes'.
13. Next nodejs was added and 'Save Changes' clicked. 
14. In the list of Buildpacks, python needs to be listed above nodejs, if this is not the case drag the buildpacks into the correct order.
15. This concluded the 'Settings' of the project.
16. Next, the 'Deploy' section was accessed by clicking on the 'Deploy' tab.
17. In the 'Deploy' section GitHub was selected and then the project on GitHub was searched for, it has the name 'portfolio-project-3'. 
18. The project was then connected to Heroku by clicking 'connect'.
19. Next, 'Enable Automatic Deploys' was selected so that the app would be updated automatically every time changes are pushed to GitHub.
20. Then, 'Deploy Branch' was clicked and the app was built.
21. The link to the deployed page is: https://speed-typing-test.herokuapp.com/

The website repository can be forked by the following steps:

1. Go to the GitHub repository.
2. Click on the Fork button in the upper right hand corner.

The repository can be cloned by the following steps:

1. Got to the GitHub repository.
2. Locade the Code button above the list of files and click on it.
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash.
5. Change the current working directory to the one where you want the cloned directory.
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

## Google Sheet Access 

The following information is for the assessors of this project. A link to the Googlesheet that is used to store, retrieve and delete data as part of the Speed Typing Test can be found here: [Google Sheet](https://docs.google.com/spreadsheets/d/1v-5AT1lGhn5DdTJ2SSQxviafFVwBQmiwdsMQ1t6k-LA/edit?usp=sharing).

Please note that there is a prepopulated worksheet named **'test'** which the assessors can use to test the functionality of the program. Additional results can be written to this worksheet, but it cannot be deleted. 

## Credits

### Media

- The background image is by [Sergi Kabrera](https://unsplash.com/photos/2xU7rYxsTiM).

### Code

Resources and inspiration came from a few sources:

- The initial idea to develop a speed typing test and parts of the code came from [Bharath K](https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b). It was subsequently heavily developed and extended. Much of the code changed significantly.
- Research on ideas how to compare two string lead the developer to the following page of ideas: [How to Compare Two Strings in Python](https://miguendes.me/python-compare-strings)
- Ideas for how to adjust the styling of the CI template came from [Ivette McDermot](https://github.com/IvetteMcDermott/PP3-Python) and [Iasmina Pal](https://github.com/useriasminna/american_pizza_order_system).

### Typing resources

General information on speed typing and how to improve were found on the following websites:

- [Ratatype](https://www.ratatype.com/learn/average-typing-speed/)
- [Das Keyboard Blog](https://www.daskeyboard.com/blog/average-typing-speed-and-words-per-minute-explained/)
- [Typing Pal](https://www.typingpal.com/en/blog/which-unit-of-speed-to-choose)
- [Pitman Training](https://www.pitman-training.ie/advice-hub/pitman-blog/fun-typing-facts-qwerty-keyboard-history-typing-speed/)
- [Indeed](https://www.indeed.com/career-advice/career-development/improve-typing-skills)


### Acknowledgements

I would like to thank:
- My mentor Brian O'Hare for his feedback, advice, guidance and support.
- Cohort fascilitator Paul Thomas O'Rirodan, for his general advice on the management of the course and pointing us to a plethora of resources to help with the projects.
- My husband, Matt, for his encouragement and support along the way.