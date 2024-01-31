#!/usr/bin/python3
"""Write a script that starts a Flask web application
-Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from
models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
Routes:
    /states_list: display an HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
        LI tag: description of one State: <state.id>: <B><state.name></B>
        You must use the option strict_slashes=False in your route definition

"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays a HTML page with a list of states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
