My Recipes is a recipe site is a hub of user's  favourite receipes. The recipes are added by users in order to have a single point of reference. The site is designed to be easy to navigate, promoting a simple layout with minimal but effective and purposeful features.

**Project Requirements:**

Build an interactive front-end website that responds to user actions and alters the way the site displays data/information.

Required Technologies : HTML, CSS, JavaScript, Python+Flask, MongoDB. Optional: Include use of JQuery, other Javascript libraries and external APIs.

A live version of the site is available  [here.]()

**Contents**

1.  [UX Development](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#ux-development)
    
2.  [Project Goals](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#project-goals)
    
3.  [UX Requirements](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#ux-requirements)
    
4.  [Developer's goal](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#developers-goals)
    
5.  [Users](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#users)
    
6.  [User Goals](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#user-goals)
    
7.  [User Stories](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#user-stories)
    
8.  [Design Choices](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#design-choices)
    
    -   [Fonts](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#fonts)
    -   [Icons](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#icons)
    -   [Colours](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#colours)
    -   [Features and Future Releases](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#features-and-future-releases)
    -   [Technologies used](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#technologies-used)
9.  [Testing](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#testing)
    
10.  [Testing User Stories from UX Section](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#testing-user-stories-from-ux-section)
    
11.  [Bugs and De-bugging](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#bugs-and-debugging)
    
12.  [Version Control](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#version-control)
    
13.  [Project Deployment](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#project-deployment)
    
14.  [Credits](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#credits)
    
15.  [Acknowledgements](https://github.com/alexeykuz-sys/LinguaGames-Project-MS2#acknowledgements)

# Testing

All-testing has been documented  [testing.md](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/testing.md)

# [](https://github.com/jamie120/ms3-eat-vegan-recipes#deployment)Deployment

-   The site was developed in GitPod and pushed to the following remote GitHub repository -  [REPO](https://github.com/jamie120/ms3-eat-eat_vegan_recipes)
    -   The following GIT commands were used throughout deployment:
        -   **git status**  ------ used to check the status of files and any changes made / untracked.
        -   **git add**  ------ to stage files ready to commit.
        -   **git commit -m " "**  ------ to commit the files.
        -   **git push**  ------ to push the files to the master branch of the GitHub repo.

### [](https://github.com/jamie120/ms3-eat-vegan-recipes#hosting-on-heroku)Hosting on Heroku

-   This site is hosted using Heroku, deployed directly from the master branch via GitHub. -  [LIVE SITE](https://ms3-eat-vegan-recipes.herokuapp.com/)
    
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
    
    -   The deployed site on Heroku will update automatically upon new commits to the master branch in the GitHub Repo :  [REPO](https://github.com/jamie120/ms3-eat-eat_vegan_recipes).

### [](https://github.com/jamie120/ms3-eat-vegan-recipes#cloning)Cloning

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

-   Avacado Pitta -  [https://unsplash.com/photos/MAbhhj3QCXQ](https://unsplash.com/photos/MAbhhj3QCXQ)  - @atasteofwellbeing
    
-   Vegan Burger -  [https://unsplash.com/photos/kPLccIMtS8E](https://unsplash.com/photos/kPLccIMtS8E)  - @runningonrealfood
    
-   Buddah Bowl -  [https://unsplash.com/photos/IGfIGP5ONV0](https://unsplash.com/photos/IGfIGP5ONV0)  - @annapelzer
    
-   Tofu Curry -  [https://unsplash.com/photos/PqsImnjuElM](https://unsplash.com/photos/PqsImnjuElM)  - @charlesdeluvio
    
-   Red Lentil Dahl -  [https://unsplash.com/photos/gVOvZFcYBMY](https://unsplash.com/photos/gVOvZFcYBMY)  - @edgarraw
    
-   Pistaccio Ice-cream -  [https://unsplash.com/photos/alEZLDPPRBU](https://unsplash.com/photos/alEZLDPPRBU)  - @aribes
    
-   Landing Page - Unsplash -  [https://unsplash.com/photos/Ww8eQWjMJWk](https://unsplash.com/photos/Ww8eQWjMJWk)  - @hermez777
    
-   Fish and chips -  [https://unsplash.com/photos/hfK401V_NXk](https://unsplash.com/photos/hfK401V_NXk)  - @jannerboy62
    

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
eyJoaXN0b3J5IjpbMTU0NzExOTEyNiwtOTQ4NjQxNTYwXX0=
-->