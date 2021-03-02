My Recipes is a recipe site is a hub of user's  favourite receipes. The recipes are added by users in order to have a single point of reference. The site is designed to be easy to navigate, promoting a simple layout with minimal but effective and purposeful features.

**Project Requirements:**

Build an interactive front-end website that responds to user actions and alters the way the site displays data/information.

Required Technologies : HTML, CSS, JavaScript, Python+Flask, MongoDB. Optional: Include use of JQuery, other Javascript libraries and external APIs.

A live version of the site is available  [here.]()

**Contents**

1.  [UX Development](https://github.com/alexeykuz-sys/myRecipe-MS3#ux-development)
    
2.  [Project Goals](https://github.com/alexeykuz-sys/myRecipe-MS3#project-goals)
    
3.  [UX Requirements](https://github.com/alexeykuz-sys/myRecipe-MS3#ux-requirements)
    
4.  [Developer's goal](https://github.com/alexeykuz-sys/myRecipe-MS3#developers-goals)
    
5.  [Users](https://github.com/alexeykuz-sys/myRecipe-MS3#users)
    
6.  [User Goals](https://github.com/alexeykuz-sys/myRecipe-MS3#user-goals)
    
7.  [User Stories](https://github.com/alexeykuz-sys/myRecipe-MS3#user-stories)
    
8.  [Design Choices](https://github.com/alexeykuz-sys/myRecipe-MS3#design-choices)
    
    -   [Fonts](https://github.com/alexeykuz-sys/myRecipe-MS3#fonts)
    -   [Icons](https://github.com/alexeykuz-sys/myRecipe-MS3#icons)
    -   [Colours](https://github.com/alexeykuz-sys/myRecipe-MS3#colours)
    -   [Features and Future Releases](https://github.com/alexeykuz-sys/myRecipe-MS3#features-and-future-releases)
    -   [Technologies used](https://github.com/alexeykuz-sys/myRecipe-MS3#technologies-used)
9.  [Testing](https://github.com/alexeykuz-sys/myRecipe-MS3#testing)
    
10.  [Testing User Stories from UX Section](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#testing-user-stories-from-ux-section)
    
11.  [Bugs and De-bugging](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#bugs-and-debugging)
    
12.  [Version Control](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#version-control)
    
13.  [Project Deployment](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#project-deployment)
    
14.  [Credits](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#credits)
    
15.  [Acknowledgements](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#acknowledgements)

====

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#ux-development)UX Development

My Recipe website will help users to have all their recipes  in one place, easily accessible.
As user, I have always wanted to have a single point of access to all recipes my family has collected throuout the years, which are written on pieces of paper.

The primary goal of the website is to have easy access to recipes and preservance for the future.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#project-goals)Project goals

The purpose of this project to create website to enable consumers to have fun interactive experience in learning of the new words. The website has to be easy to navigate with clear purpose of the buttons and screen space. The game has to provide the clear and safe framework for clients and to make the experience casual rather than requirement.

# [](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#ux-requirements)UX requirements

The website targets the individuals interested to learn or improve the knowledge of the foreign languages in the casual way, through the game experience. Present level of development offers only fail/win notification. Please see future implementations plan for more details of users progress measurement.

# [](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#developers-goals)Developer's Goals

The site owner has the following goals:

-   To provide users with interactive and easy navigation learning process.
-   To encourage users to learn more
-   To provide platform with colours and fonts stimulating users experience.
-   To give users control over the game, by choosing of the language, initiating and resetting the game and timer.

# [](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#users)Users:

Individuals interested to learn a new language with no age limitation.

# [](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#user-goals)User goals:

Person interested to learn basics of the new language has to learn 300-600 words to be to travel and 1000 words to be able to converse; the users goals is to identify application allowing them to have access to the application teaching them the most common words used in any language. Therefore, i have used the most common words used in English language



# Testing

All-testing has been documented  [testing.md](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/testing.md)

Deployment

-   The site was developed in GitPod and pushed to the following remote GitHub repository -  []()
    -   The following GIT commands were used throughout deployment:
        -   **git status**  ------ used to check the status of files and any changes made / untracked.
        -   **git add**  ------ to stage files ready to commit.
        -   **git commit -m " "**  ------ to commit the files.
        -   **git push**  ------ to push the files to the master branch of the GitHub repo.

Hosting on Heroku

-   This site is hosted using Heroku, deployed directly from the master branch via GitHub. -  [LIVE SITE]
    
    -   The following steps were taken to complete the hosting process.
    
    1.  Set  **_debug=False_**  in the app.py file.
    2.  Created a requirements.txt file from the terminal, using  **_pip3 freeze --local > requirements.txt_**, to allow Heroku to detect this project as a python app and any required package dependencies.
    3.  Created a Procfile using  **_echo web: python app.py > Procfile_**  from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project.
    4.  Created a new Heroku app,  **_ms3_eat-vegan-recipes**  and set its region to Europe.
    5.  Automatic deployment was set up on Heroku - On the app dashboard, in the deploy menu. Connect to GitHub section. The GitHub repository was searched for and connected to the app.
    6.  In the settings tab on the app dashboard, 'Reveal Config Vars' was used to tell Heroku which variableS are required to run the app. The following config vars were added:
        -   **_IP_**
        -   **_PORT_**
        -   **_SECRET_KEY_**
        -   **_MONGO_URI_**
    7.  In GitPod, a check was completed to ensure the master branch was up to date and all commits had been pushed to GitHub, ready for Heroku to deploy.
    8.  Clicked the  **_Enable Automatic Deploys_**  button located in the  **_Deploy_**  section of Heroku to allow for automatic deploys.
    9.  Clicked the  **_Deploy Branch_**  button located in the  **_Deploy_**  section of Heroku to finally deploy this project.
    10.  Clicked the  **_View_**  button to launch this project's app.
    
    -   The deployed site on Heroku will update automatically upon new commits to the master branch in the GitHub Repo :  [REPO]
    
Cloning

To run this code locally, you can clone this repository directly into the editor of your choice by following the steps below:

1.  Open Terminal.
2.  Change the current working directory to the location when you want the cloned directory.
3.  Type the following into your Terminal:  
    git clone  [https://github.com/jamie120/ms3-eat-vegan-recipes.git](https://github.com/jamie120/ms3-eat-vegan-recipes.git)
4.  Press Enter to create a local clone.

-   To cut ties with this GitHub repository, type git remote rm origin into the terminal.

##### [](https://github.com/jamie120/ms3-eat-vegan-recipes#for-more-information-regarding-cloning-of-a-repository-click-here)For more information regarding cloning of a repository click  [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

# [](https://github.com/jamie120/ms3-eat-vegan-recipes#credits)Credits

## [](https://github.com/jamie120/ms3-eat-vegan-recipes#content)Content

All the written content of the website has been written by myself.

## [](https://github.com/jamie120/ms3-eat-vegan-recipes#media)Media

### [](https://github.com/jamie120/ms3-eat-vegan-recipes#images)Images

The following images used for this app/website were taken from Unsplash:

Recipes - Unsplash:


All other images were contributed from personal sources, of which no acknowledgement is required.

## [](https://github.com/jamie120/ms3-eat-vegan-recipes#acknowledgements)Acknowledgements

### [](https://github.com/jamie120/ms3-eat-vegan-recipes#sites-used-for-information-and-support)Sites used for information and support

-   [W3C](https://www.w3.org/)
-   [Stack overflow](https://stackoverflow.com/)
-   [W3schools](https://www.w3schools.com/)
-   CSS Tricks
-   [JQuery Documentation](https://api.jquery.com/)
-   Start Bootstrap
-   [Bootstrap Documentation](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
-   [JS Commenting](https://jsdoc.app/about-getting-started.html)
-   [MongoDB Documentation](https://docs.atlas.mongodb.com/)
-   [Python Documentation](https://docs.python.org/3/)
-   [Reading for Pagination](https://www.thatsoftwaredude.com/content/6125/how-to-paginate-through-a-collection-in-javascript)

#### [](https://github.com/jamie120/ms3-eat-vegan-recipes#i-received-advice-and-support-from)I received advice and support from

-   Oluwafemi Medale (mentor)
-   Code Institute - Slack Community (various students, tutors and mentors)


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1MDg5NTg3MCwyMDY4OTQwMDkyLC05ND
g2NDE1NjBdfQ==
-->