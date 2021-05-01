# REC!PE-DESK

Recipes Desk is a recipes app where you can update your own recipes and see other's users recipes, save them and add to libraries.
 
## UX

As a cook I'd like to share healthy recipes and discover other users ideas and creative recipes.

As a food lover I'd like to find recipes and save them to build a weekly schedule and be able to organise my meals. 

## Features

**NEW USER**

NAV-INDEX:

- HOME
- LOG IN
- SIGN UP

If the user has never signed up to recipe desk will see:

MAIN PAGE
With all users recipes but no functionality

LOG/IN - SIGN UP
Log in and sign up option to see more functionalities. 

**REGISTERED USER**

NAV - INDEX

 - HOME
    - EDIT
    - REMOVE
    - ADD TO FAVORITES
    - ADD TO LIBRARY
 - MY RECIPES
    - EDIT
    - REMOVE
    - ADD TO FAVORITES
    - ADD TO LIBRARY
 - ADD RECIPE
 - FAVORITES RECIPES
 - LIBRARIES
 - LOG OUT

HOME
The main page will contain all user recipes, the idea is to have a home page with last updated recipes.

If the user is subscribed and logged in will also have the chance of do the following functionalities with just one click, I used classic and common icons to avoid confusions.
- Editing recipes
- Removing recipes
- Adding to favorites
- Adding to libraries created by users. 

Additionaly the user will be able to log out the session at any time when logged in from the menu above. 


MY RECIPES
This section will show only recipes created by the user logged in, with same functionalities as the recipe card from main page, the only functionality is different from Recipes home page is that other users recipes won't be visible here. 


ADD RECIPE
This section contains a form where user can input the recipe information and submit to create the recipe.


FAVORITES
This section will contain all recipes marked as favorite by user. 


In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea is to be able to see other users profile. 
- Another feature idea is to request for image to user and have them displayed. 
- Validation in forms
- Add to more than one Library

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- Materialize: For this project I'm using the front-end framework Materialise to keep a fixed structure within all pages and give a clear APP image. 

- Python Flask framework: I will user flask framework to display the data accross URLS by using routing and python functions to display templates extending content from a base template.

- MongoDB: Since the project requires database to save the data of any user registered so they can log in and log out as many times without losing any sved updates on their profiles. 

    - COLLECTION FOR THIS PROJECT:
        - USERS, with username, password and saved recipes for displaying later
        - RECIPES, all recipe info to display for user
        - LIBRARIES, libraries created by user

- Heroku: I have connected the github to heroku to deploy and displpay the page. 


## Testing

**NEW USER**


1. Home page:
From home page there are not functionalities active if you are not a registered user, so you can see recipes but not intereact with them, if any of this functionalities are clicked the log in page is displayed. 

- Log In: I logged in into the page with no problem, redirected to home page with all recipes.
- Sign up: I tried to sign up and the user has been registered in mongoDB correctly.

**REGISTERED USER**

1. Home Page:
I see the recipes if are made by me in the home page, and the recipes made by other I can see but I can't modify, buttons don't appear.
Added to favorites is working.
Added to library is not, will be a feature to add in the future
Edit recipe working
Remove recipe working

2. My recipes:
Only diesplays the recipes made by user and has same funcitonalities as in Home page. 

3. Add recipe:
Validation still need to activate. When user add the recipe is correctly updated to mongoDB although the validation should be useful to avoid weird recipes as empty values. 

4. Favorites:
The favorites page will show all recipes marked as favorites, although a nice feature to implement is to be abel to remove from favorites. This hasn't been implemented yet.

5. Libraries
Feature to be implemented.

It works and looks fine in big screens and small screens. When adding the recipe there is a small bug with the label that doesn't show a nice design for mobile options but will also be a feature to fix. 


## Deployment

I used heroku to deploy the project. 
The deployed project looks the same but in the working environment there are delicate files that cannot be share, although the file that can't be share are environment variables that are correectly configured at Heroku Config Vars,

The only branch used is the master branch. 


## Credits
