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

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- Materialize: For this project I'm using the front-end framework Materialise to keep a fixed structure within all pages and give a clear APP image. 

- Python Flask framework: I will user flask framework to display the data accross URLS by using routing and python functions to display templates extending content from a base template.

- MongoDB: Since the project requires database to save the data of any user registered so they can log in and log out as many times without losing any sved updates on their profiles. 

- Heroku: I have connected the github to heroku to deploy and displpay the page. 


## Testing

**NEW USER**


1. Home page:



In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X





javascript in put fields
https://jsfiddle.net/Spokey/XHpXy/
