"""Models for Melon Scheduler app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A User"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)




class Timeslot(db.Model):
    """A timeslot"""

    __tablename__ = 'timeslots'

    date = db.Column(db.Date, primary_key=True)

    zero = db.Column(db.String(20))
    one = db.Column(db.String(20))
    two = db.Column(db.String(20))
    Three = db.Column(db.String(20))
    Four = db.Column(db.String(20))
    Five = db.Column(db.String(20))
    Six = db.Column(db.String(20))
    seven = db.Column(db.String(20))
    eight = db.Column(db.String(20))
    nine = db.Column(db.String(20))
    ten = db.Column(db.String(20))
    eleven = db.Column(db.String(20))
    twelve = db.Column(db.String(20))
    thirteen = db.Column(db.String(20))
    fourteen = db.Column(db.String(20))
    fifteen	= db.Column(db.String(20))
    sixteen	= db.Column(db.String(20))
    seventeen = db.Column(db.String(20))
    eighteen = db.Column(db.String(20))
    nineteen = db.Column(db.String(20))
    twenty = db.Column(db.String(20))
    twentyone = db.Column(db.String(20))
    twentytwo = db.Column(db.String(20))
    twentythree = db.Column(db.String(20))
    twentyfour = db.Column(db.String(20))
    twentyfive = db.Column(db.String(20))
    twentysix = db.Column(db.String(20))
    twentyseven	= db.Column(db.String(20))
    twentyeight	= db.Column(db.String(20))
    twentynine = db.Column(db.String(20))
    thirty = db.Column(db.String(20))
    thirtyone = db.Column(db.String(20))
    thirtytwo = db.Column(db.String(20))
    thirtythree	= db.Column(db.String(20))
    thirtyfour = db.Column(db.String(20))
    thirtyfive = db.Column(db.String(20))
    thirtysix = db.Column(db.String(20))
    thirtyseven	= db.Column(db.String(20))
    thirtyeight	= db.Column(db.String(20))
    thirtynine = db.Column(db.String(20))
    fourty = db.Column(db.String(20))
    fourtyone = db.Column(db.String(20))
    fourtytwo = db.Column(db.String(20))
    fourtythree	= db.Column(db.String(20))
    fourtyfour = db.Column(db.String(20))
    fourtyfive = db.Column(db.String(20))
    fourtysix = db.Column(db.String(20))
    fourtyseven	= db.Column(db.String(20))
    fourtyeight	= db.Column(db.String(20))




def connect_to_db(flask_app, db_uri="postgresql:///cal", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

def seed_data():
    date

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)