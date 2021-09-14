# -*- encoding: utf-8 -*-

# Imports
from   flask import Flask                     # manage the app
from   sqlalchemy       import create_engine  # used to detect if table exists
from   flask_sqlalchemy import SQLAlchemy     # manage the database
import click                                  # used to load the data
import pandas            as pd                # process pandas

# Invoke Flask magic
app = Flask(__name__)
# App Configuration
app.config['SECRET_KEY'] = 'S_U_perS3crEt_KEY#9999'
# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB Object = SQLAlchemy interface
db = SQLAlchemy(app)


# Define the storage
class User(db.Model):

    Id = db.Column(db.Integer, primary_key=True )
    comment  = db.Column(db.TEXT)
    live_or_die = db.Column(db.Integer, index=True)
    atk_or_def = db.Column(db.Integer, index=True)
    good_or_bad = db.Column(db.Integer, index=True)
    Enclosure = db.Column(db.Integer, index=True)
    
    def __init__(self, Id,comment, live_or_die, atk_or_def, good_or_bad, Enclosure):
        self.Id = Id
        self.comment = comment
        self.live_or_die = live_or_die 
        self.atk_or_def =  atk_or_def
        self.good_or_bad = good_or_bad
        self.Enclosure = Enclosure
    
    def __repr__(self):
        return str(self.comment) 

    def to_dict(self):
        return {
            'Id': self.Id,
            'comment': self.comment,
            'live_or_die': self.live_or_die,
            'atk_or_def': self.atk_or_def,
            'good_or_bad': self.good_or_bad,
            'Enclosure': self.Enclosure
        }    

db.create_all()


# Define the custom command
@app.cli.command("load-data")
@click.argument("fname")
def load_data(fname):
    ''' Load data from a CSV file '''
    print ('*** Load from file: ' + fname)

    # Build the Dataframe from pandas
    df = pd.read_csv(fname)

    # Iterate and load the data     
    for row in df.itertuples(index=True):

        print ( '************************************************' )

        Id = row[1]
        comment    = row[2]
        live_or_die = row[3]
        atk_or_def = row[4]
        good_or_bad = row[5]
        Enclosure = row[6]
        
        print ( 'comment = ' + str( comment ) )
        obj = User(Id, comment, live_or_die, atk_or_def, good_or_bad, Enclosure)       
        db.session.add(obj)

    db.session.commit( )
