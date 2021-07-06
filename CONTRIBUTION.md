# Contribution Guidelines 
Guidelines for contributing to this project. Must be strictly followed by all team members.  
This will guide you from cloning this repository to pushing your contributions.

## Cloning
To clone project repo to your local machine, open command prompt and run:
```
git clone https://github.com/
```

## Change to project directory
Change to the project directory you just cloned
```
cd 
```

## Checkout Develop Branch
Checkout develop branch by running
```
git checkout develop
```

## Checkout Your Feature Branch
Feature Branching Workflow means you create a new branch for every feature or issue you are working on.
It is goood practice for the branch name to end with the issue id.
So if an issue id is **#5** and issue name is **Signup API** then our branch name would be **signup-api-#5**.
create and checkout feature branch by running:
```
git checkout -b issue-name-id
```

## Setup Development Environment
To setup the development environment to run project run:
```
pipenv install
```

## Migrate Database
Migrate the database by running:
```
python manage.py migrate
```

## Run Project
If you want to test the development environment run:
```
python manage.py runserver
```

# When You Have Fixed The Issue
When you have finished making changes and have commited your changes.

## Pull Update from Remote
Pull latest update from the remote repo by running:
```
git pull origin develop
```

## Push Local Changes to Remote
Push your new fix or feature to the remote branch of your feature.
If your feature branch name is **signup-api-#5** then run:
```
git push origin signup-api-#5
```

## Contact Me for PR
After pushing to the remote branch successfully. Contact me by sending your feature branch name to me on slack.
I will create a PR for you and link it to your assigned issue which i have already linked to the project board.
Once the PR is reviewed, merged and the Issue closed the project board will automatically move your card to done.

## Happy Contributing!!!
