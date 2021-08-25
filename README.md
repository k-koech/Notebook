# Pitch
#### The app is about posting and reading pitches, 23/08/2021
#### **By Kelvin Kipchumba**
## Project Description
    The application  allows users to use that one minute wisely. 
    The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## Setup/Installation Requirements
    - Download a file in the code section to the desired folder
    - Extract the files
    - Open the folder with vs code.
    - Run "chmod a+x start.sh" to make it exwcutable.
    - Run the project in terminal using "./start.sh" command.
    - Create database and add its URI in config file.
    - Run migrations using 'python3 manage.py db migrate -m "Initial Migration" '.
    - Then use 'heroku run python3 manage.py db upgrade' to create tables in the database.
    - And you are all done

## BDD
    As a user should;
    - I would like to see the pitches other people have posted.
    - I would like to vote on the pitch they liked and give it a downvote or upvote.
    - I would like to be signed in for me to leave a comment
    - I would like to receive a welcoming email once I sign up.
    - I would like to view the pitches I have created in my profile page.
    - I would like to comment on the different pitches and leave feedback.
    - I would like to submit a pitch in any category.
    - I would like to view the different categories.
    
## Live link
Deployed project can be accessed here [Pitches](https://pitches-flask.herokuapp.com/)   

## Known Bugs
    The application works perfectly well, no bugs.

## Technologies used
    - HTML
    - CSS
    - Bootstrap
    - Python

## Support and contact details
    - email :: koechkelvin97@gmail.com
    - phone :: +254725801772

### License
*Licenced under the [MT-licence](https://github.com/k-koech/pitches_flask/blob/master/LICENSE.md)*
Copyright (c) 2021 **Kelvin Kipchumba
