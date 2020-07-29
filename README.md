# One Byte of a bakers dozen
## Overview
The name came from the idea that its to do with cooking and its a pun on bite.
For this application you will need to register and login to create or edit recipes.
Please use the email "user@gmail.com" and the password "abc"
## UX
In this project I wish to achieve a UX that is easy and very straight forward
and lets the user interact in a easy way.
## Features
### Existing Functionality
* Ability to log in and register logout
* Ability to add, edit and remove recipes when logged in
* Only users who created the recipe can edit it
* The ability to view my recipes
* Storing users and recipes on mongodb
* Encrypted passwords
* Ability to view more details about a recipe
* A recipe has a list of ingredients, preparation step and vegetarian option
* I created a script to input my test data. I used this to quickly repopulate the database when testing

### Future Enhancements
* I would like to make a "My Recipes" page that showcase one persons recipes
* Search/filter functionality would be a good addition
* More options like preparation time, gluten free etc
## Technologies Used
1. [HTML5](https://en.wikipedia.org/wiki/HTML5 )
    1. I used HTML for the basic structure of the website.
2. [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets )
    1. CSS was used to style the HTML.
    2. The style sheet was mostly kept separate from the html.
3. [Bootstrap Version 4.4.1](https://getbootstrap.com/ )
    1. Bootstrap components such as grid, card, button, table, navbar where used in my project to simplify creating responsive web application.
4. [MongoDB](https://www.mongodb.com)
    1. MongoDB was used to store all my recipes and users information.
    2. I used Pymongo to help connect to mongoDB Atlas cluster
5. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    1. I used Blueprints to help structure my project well
    2. I used URL_FOR to connect everything togeather
    3. I used session to help track my user
    4. I used render_template to render my HTML
    5. I used redirect to get to my home page alot
    6. I used request to access my forms data
6. [Werkzeug security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
    1. I used Werkzeug security to encrypt my passwords and to check the passwords
7. [VSCODE](https://code.visualstudio.com/) 
    1. VSCODE was used as the development environment.
8. [Github](https://github.com/)
    1. Github was used for my version control in the project. 
9. [Font-awesome Version 5.11.1](https://fontawesome.com/) 
    1. Font-awesome was used to get some icons.
10. [Heroku](https://www.heroku.com/home)
    1. I used heroku to host my application

## Testing
1. I used Chrome Dev Tools for debug Testing.
    1. I used the inspect feature to check different elements on my page.
    2. I used the coverage tab to check my css was being used on the given page.
    3. I used the network tab to see what was taking a long time to load and what wasn't loading.
    4. I used the computed tab to see the final state of a given element.
    5. I used the device toolbar to check that my website was rendered in a responsive manner on all device's.
    6. I installed the chrome [Lighthouse](https://developers.google.com/web/tools/lighthouse) plugin to use the audit feature to check Performance, progressive web app, Best practices, accessibility and SEO.
2. Application Testing
    1. I tested that everything worked okay when resizing the browser.
    2. I ran all my tests on localhost (root website) then pushed it onto github (where ran off the subdomain). Checked that all resources loaded properly off the root and subdomain.
    3. I checked on mobile to see that everything was working correctly.
    4. I ran into some problems trying to get blueprints to work and i solved this problem by changing how I initialised my DB.
    5. I ran into some problems with basic html i solved them by googling.
    6. for some reason i couldnt add a margin to some of the buttons so thats why they are a bit cluttered
## Deployment
I used [Live Server](https://github.com/ritwickdey/vscode-live-server) on my windows PC and once I was happy I committed to github to check that everything ran smoothly there as well. 

## Credits
### Content
I used [Bootstrap Version 4.4.1](https://getbootstrap.com/) grid system.
I used [StackOverflow](https://stackoverflow.com/) to solve problems that I couldn't figure out
I used [Favicon](https://favicon.io/) for my favicon
### Media
My recipes where founds from various recipe websites such as [Retrobite](https://www.retrobite.com/)
### Acknowledgements



