![(https://github.com/alexeykuz-sys/myRecipe-MS3/blob/4d6cf60f46b4eb9918d0ab862aa6cf49c61e59a3/static/images/amiresponsive.PNG)
](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/4d6cf60f46b4eb9918d0ab862aa6cf49c61e59a3/static/images/amiresponsive.PNG)


My Recipes is a recipe site of user's  favourite receipes. The recipes are added by users to have a single digitised point of reference for user's favorite recipes. The site is designed to be easy to navigate and use, promoting a simple layout with minimal but effective and purposeful features.

**Project Requirements:**

Build an interactive front-end website that responds to user actions and alters the way the site displays data/information.

Required Technologies : HTML, CSS, JavaScript, Python+Flask, MongoDB. 
A live version of the site is available [LIVE SITE](https://my-recipe-ms3.herokuapp.com/)  

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
    - [Database design](https://github.com/alexeykuz-sys/myRecipe-MS3#database-design)
    -   [Features and Future Releases](https://github.com/alexeykuz-sys/myRecipe-MS3#features-and-future-releases)
    -   [Technologies used](https://github.com/alexeykuz-sys/myRecipe-MS3#technologies-used)
9.  [Manual Testing](https://github.com/alexeykuz-sys/myRecipe-MS3#manual-testing)

 1    
10.  [Testing User Stories](https://github.com/alexeykuz-sys/myRecipe-MS3#testing-user-stories)
    
11.  [Bugs and De-bugging](https://github.com/alexeykuz-sys/myRecipe-MS3#bugs-and-debugging)

 12.  [Project Deployment](https://github.com/alexeykuz-sys/myRecipe-MS3#project-deployment)
    
1.  [Credits](https://github.com/alexeykuz-sys/myRecipe-MS3#credits)
    
1.  [Acknowledgements](https://github.com/alexeykuz-sys/myRecipe-MS3#acknowledgements)

====

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#ux-development)UX Development

My Recipe website will help users to have all their recipes  in one place, easily accessible.
As user, I have always wanted to have a single point of access to all recipes my family has collected throuout the years, which until now were written on pieces of paper.

The primary goal of the website is to have easy access to recipes, digitise and save for the future.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#project-goals)Project goals

The purpose of this project is to create website that allow users to create, use, read, edit and delete their favourite recipes. The website has to be easy to navigate and use, with clear purpose of the buttons and screen space.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#ux-requirements)UX requirements

The website targets the individuals interested to transfer their paper recorded recipes into digital form and copy recipes availalbe on other websites to one single hub.
# [](https://github.com/alexeykuz-sys/myRecipe-MS3#developers-goals)Developer's Goals

The site owner has the following goals:

-   To provide users with clean and easy way to create recipes
-   To give users control over the ingredients and methods of cooking.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#users)Users:

Individuals interested to keep their recipes in digital form

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#user-goals)User goals:
The users goal is to identify application allowing them to have access to the recipe any time anywhere.


	# [](https://github.com/alexeykuz-sys/myRecipe-MS3#user-stories)User Stories

	**- First Time Visitor Goals:**

	1.  As a visitor to the website, I want to easily understand the main purpose of the website.
	2.  As a visitor easy to register and login/out
	3.  As a visitor I want to see recipes on my frontpage
	4.  As a visitor i want an easy to add,edit and delete recipes.

	**- Returning Visitor Goals:**

	1.  Returning Visitor I would like to be able to add ingredients to the shopping list
	2.  Returning Visitor I would like to share recipe by email or via social media.

	# [](https://github.com/alexeykuz-sys/myRecipe-MS3#design-choices)Design Choices

	When designing website I took inspiration from various recipe websites like BBCGoodFood and AllRecipes. The website was adapted to fit user requirements. 
	The webpages consist of :
	1. Navbar and Footbar - simple layout. Navbar gives mobile and desktop menu views with options for user to see all recipes, register and login. Once loged in user can add,edit and delete recipes.
	2. Recipe Page - single page devided in two parts. Upper parts represents the hero image with a search bar.
	The bottom part is the section where all recipes are seen and can be separate into Breakfast, Lunch and Dinner categories.
	3. Add Recipe page - simple page with recipe catgories, linked to MongoDB database.
	4. Register Page  - user has to input username  password that are restricted to min and max number of characters.
	5. Profile Page - user profile page, basic card, which will be expanded in later versions.
# [](https://github.com/alexeykuz-sys/myRecipe-MS3#fonts)Fonts

I have used Google Fonts to determine the best fonts suitable for each part of the website, I.e. Logo, Menu and Body information.

I opted to use Lato font for my website, which is one of the most popular fonts used by major internet companies.

[Top 10 Best Google Fonts](https://nestify.io/blog/top-10-best-google-fonts/)

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#icons)Icons

Icons used where provided by  [icons8](https://icons8.com/), used in moderation and are self explanatory.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#colours)Colours

The colours were determined by the pallet of Cooler website:

-   For navbar #212121  [![navbar](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/static/colors/blackColor.png?raw=true)](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/static/colors/blackColor.png?raw=true)

-   For body background #effafa.  [![Background](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/static/colors/bgColor.png)](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/static/colors/bgColor.png?raw=true)

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#database-design)Database design
The database consist of three collections. Compiled and hosted using  [MongoDB](https://www.mongodb.com/) 

#### Recipes
1.  _id - ObjectId - (generated by mongoDB)
2.  category_name - string
3.  recipe_img_URL - url
4.  recipe_ingredients - string
5.  recipe_name - string
6.  recipe_description - string
7.  recipe_time - string
8.  recipe_serving - string
9.  created_by - string

### Categories Structure

1.  _id - ObjectId - (generated by mongoDB)
2.  category_name - string

### Users

1.  _id - ObjectId - (generated by mongoDB)
2.  username - string
3.  password - string - (password hash generated by werkzeug.security)

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#features-and-future-releases)Features and Future Releases

View my wireframes  [here](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/wireframes.md). It's website with a landing page, register, log in/out and recipe editing page.  

Features to implement:

-   To add favourite option
-   To add shopping list option
-	To add fully functional profile page.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#technologies-used)Technologies Used

**UX/UI design**

-   [Figma](https://figma.com/)

**Languages**

-   [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
-   [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)  
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

**Tools & Libraries**

-   [Git](https://git-scm.com/)
-   [Materialize](https://materializecss.com/)
-   [Icons8](https://icons8.com/)
-   [Google fonts](https://fonts.google.com/)
-   [Figma](https://figma.com/)
-   [Canva](https://canva.com/)
-   [Flask](https://flask.palletsprojects.com/en/1.1.x/)
-   [MongoDB](https://www.mongodb.com/)
-  [Heroku](https://www.heroku.com/)

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#manual-testing)Manual Testing
All functions were tested for different screen sizes.
- **Landing Page**

Once website loaded, user sees the hero image, underneath which there is search section and then all recipes section.
Search section allow user to search recipes. I input a word in search and pressed search. If such word exist in recipes, the recipe will be shown n the ceen underneath. The search word remains seen in search form. I have to press reset button to reset page to all recipes.
I can also sort recipes by Breakfast, Lunch and Dinner. I pressed each button and achieved desired results 
 Each recipe card has imae, recipe name, people served and time to cook. Each recipe card is clickable and give access to full recipe page with detailed cooking instructions.
 
-**Single Recipe Page(Get_Recipe)**

The single recipe page gives all user access to the recipe ingredients and method of cooking. In addition, access to Edit and Delete functions.
I checked that these functions appear only for logged in users.  
 I checked that Edit buttons opens the edit page, where user can edit all recipe fields and save recipe.
 I checked that delete button, triggers modal with delete or cancel options. Cancel button hides modal and Delete button reconfirms deletion and delete recipe from the database.
 
-**Log In**

I checked that log in button redirects to log in page.
I created own account that complied with min requirements and successfully logged in and received corresponding flash notification.
I also checked if the log in form gives visual and text warning if i input wrong information or less symbols than required.

-**Log Out**

I checked that log out buttons redirects you back to log in page.

-**Register**

I checked that register button is visible to all guest, not logged in users. I checked that user gets relevant notifications if user tries to register with less symbols or wrond symbols.
I checked that user get notification if he tries to register with username that already exists in database.
I checked that user get notification and redirected to profile page.

-**New Recipe**

I checked that user can input all information to all fields in new recipe form. I checked if user get warning notifications if he omits any field in the form. I also checked that nce user presses the button Add Recipe, he redirected to all recipes page and gets flash message tht recipe was added successfully.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#testing-user-stories)Testing User Stories

User story testing:

1. Landing page.
- The page layout is simple and easy to navigate. It consists of basic colors, which do not distract visitor's attention.
- Navbar - The lLogo is clear and describes the purpose of the website. It has a link to the home page. 
Navbar menu has three options: Recipes, Register, and Log in. Each of them leads aing user to the relevantspecifi ages. The rRecipe page shows all recipes published by users. It is available for logged- in and guest users. 
Once a user has logged in, a user sees  new enu options:  Profile and Edit tis ge. The pProfile page is a simple card with user details. In the future, it will be developed into more detailed information with extra features allowing users to see their own recipes.
- Footer - simple footer that has links to social media and website slogan. All links open correct pages.
2. Log In and Log Out pages allow the user to log in/out. Log In page has required fields and check if the user inserted the correct username and password. The uUser receives screen notifications in the case user puts a wrong username or password.
3. Register page - allows users to register with a username and password. It has a requirement to put min number of symbols and a-z and 0-9.  if users insert fewer symbols, they get a warning notification. If the username already exists, the user gets a warning notification.
4. Profile page -once the user has successfully logged in, the user is redirected to the profile page. The pProfile page will be set up in the future development of the app.
5. New Recipe page -  Logged in users have access to this page. The page contains the form which the user has to be filled in. Once the user has finished and pressed the add button, the user receives a flash message of success and the screen redirected to the recipe page.
6. Logged in users also gain access to Edit and Delete buttons on thein get recipe page. Once the user decides to delete a recipe, the user receives a modal warning if he wants to delete the recipe to reconfirm the user's decision.

#### As a first-time guest visitor:

-   Upon visiting the website, I want to see the recipes available with the latest recipes at the top.
-   The navbar should be easy to find and contain links to show all recipes.
-   I should easily search recipes either by specific keywords or category: breakfast, lunch, or dinner.
-   I should expect results to show underneath the search field.
-   I should expect to be able to open each recipe and see ingredients and cooking instructionsshotsreie.

#### As a returning visitor:

-   As a returning user, interested in using the website regularly. I want to see clearly, where I can register as a user or log in.
-   Upon signing up, I am redirected to my profile page.
-   The navbar is now showing new menu options to add a new recipe.
-   Now, I can start adding my favorite recipes to the website. I should expect the add new recipe form to be comprehensive but easy to use.
-   I expect to be able to edit and delete recipes I have added to the website. Edit and Delete buttons appear on the recipe page for recipes added by the user.
-   Upon pressing the edit button, I expect to be redirected to the edit page, which is similar to add recipe button and allows edit all recipe fields.
-   Upon pressing the delete button, I expect to have the warning appear on my screen, asking if I m sure I want to delete the recipe. I expect to have it if I pressed delete mistakenlyreally wants to delete recipe to reconfirm user's decisision.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#bugs-and-debugging)Bugs and Debugging

Tthere is a bug in line 37 of javascript function, provided by code institute in task app, which i used for my project. Ii couldn't debug it to resolve the issue.
I have also noticed that error pops up for line 77, refering to modalBtnRef in line 69. It appears only when console checked on any page other than get_recipe. This code applies to button DELETE on get_recipe page and error disappears once get_recipe page is open.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#project-deployment)Project Deployment

Hosting on Heroku

-   This site is hosted using Heroku, deployed directly from the master branch via GitHub. -  [LIVE SITE](https://my-recipe-ms3.herokuapp.com/)
    
    -   The following steps were taken to complete the hosting process.
    
    1.  Set  **_debug=False_**  in the app.py file.
    2.  Created a requirements.txt file from the terminal, using  **_pip3 freeze --local > requirements.txt_**, to allow Heroku to detect this project as a python app and any required package dependencies.
    3.  Created a Procfile using  **_echo web: python app.py > Procfile_**  from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project.
    4.  Created a new Heroku app,  **my-recipe-m3**  and set its region to Europe.
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
    
    -   The deployed site on Heroku will update automatically upon new commits to the master branch in the GitHub Repo :  [REPO](https://github.com/alexeykuz-sys/myRecipe-MS3)
    
Cloning

To run this code locally, you can clone this repository directly into the editor of your choice by following the steps below:

1.  Open Terminal.
2.  Change the current working directory to the location when you want the cloned directory.
3.  Type the following into your Terminal:  
    git clone  [insert link](https://github.com/alexeykuz-sys/myRecipe-MS3)
4.  Press Enter to create a local clone.

-   To cut ties with this GitHub repository, type git remote rm origin into the terminal.

##### [](https://github.com/alexeykuz-sys#for-more-information-regarding-cloning-of-a-repository-click-here)For more information regarding cloning of a repository click  [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#credits)Credits

### [](https://github.com/alexeykuz-sys/myRecipe-MS3#images)Images

The images for this app/website were taken from Unsplash:

[Unsplash](https://unsplash.com/s/photos/recipe)

The recipes were taken from:
[BBC Good Food](https://www.bbcgoodfood.com/)

I used Code Institute Task Follow up project as a reference and guidance in building this website
All other images were contributed from personal sources, of which no acknowledgement is required.

## [](https://github.com/alexeykuz-sys/myRecipe-MS3#acknowledgements)Acknowledgements

Sites used for information and support

-   [W3C](https://www.w3.org/)
-   [Stack overflow](https://stackoverflow.com/)
-   [W3schools](https://www.w3schools.com/)
-   [CSS Tricks](https://css-tricks.com/)
-   [JS Commenting](https://jsdoc.app/about-getting-started.html)
-   [MongoDB Documentation](https://docs.atlas.mongodb.com/)
-   [Python Documentation](https://docs.python.org/3/)
-   [Reading for Pagination](https://www.thatsoftwaredude.com/content/6125/how-to-paginate-through-a-collection-in-javascript)

#### [](https://github.com/alexeykuz-sys/myRecipe-MS3#I-received-advice-and-support-from)I received advice and support from

-   Oluwafemi Medale (mentor)
-   Code Institute - Slack Community. (various students, tutors and mentors)


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUyNDI5OTA3NCwtMTk1NDg1MDQ5NCwtMz
Y0MjM4MzM0LDE5MjMzNzIwNDEsNDIwODAwMjcsLTE5NTg3ODkw
MjMsNTcwMTg5MjQxLDExODYzOTkwMTMsLTQ3NzEzNTg4MSw4Nj
c3NDYzNzAsMTg1NDg3ODM3LDEzNzYxNjgxMzEsLTExMDQyNzIx
MTQsMTYxNzM5MzEyMiwxOTI5OTYyMTU2LDM1Mjc0OTMzNywxMD
g2NTM2NjA1LDE4MjgxNDc0OTYsMjQ1NTAyNDQyLC01Njc3NjY5
OTVdfQ==
-->