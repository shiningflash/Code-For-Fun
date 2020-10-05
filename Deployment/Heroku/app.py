""" Deploying Flask with Heroku """

""" install those packages
    $ pip3 install pipenv
    $ pip3 install gunicorn
"""

""" create and activate virtual environment
    $ virtualenv venv
    $ source vnev/bin/activate
"""

""" see all requirements
    $ pip3 freeze
    $ pip3 freeze > requirements.txt
"""

""" create a Procfile and add this line
    $ touch Procfile
    $ web: gunicorn <app_name>:app
"""

""" install heruko in mac
    $ brew tap heroku/brew && brew install heroku
"""

""" initiate git
    $ git init
"""

""" create an app heroku (in our case 'fapp12345')
    $ heroku create <app-name>
"""

""" check remote repo
    $ git remote -v

    git add and commit
    $ git add .
    $ git commit -m "<some-messages>"

    push the app into heroku
    $ git push heroku master

    open heroku app
    $ heroku open
"""

""" our new generated heroku app is on online >> yayyy...
    https://fapp12345.herokuapp.com/
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello! World'

if __name__ == '__main__':
    app.run()