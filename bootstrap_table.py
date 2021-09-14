from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def index():
    users = User.query
    return render_template('bootstrap_table.html', title='Bootstrap Table',
                           users=users)


if __name__ == '__main__':
	app.run(debug=True)
