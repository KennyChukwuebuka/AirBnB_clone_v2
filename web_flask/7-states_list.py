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

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    from models import storage
    storage.close()


@app.route('/states_list')
def states_list():
    """display an HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
    LI tag: description of one State: <state.id>: <B><state.name></B>
    You must use the option strict_slashes=False in your route definition
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
