from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('ajax_table.html', title='Ajax Table')

@app.route('/api/data')
def data():
    return {'data': [user.to_dict() for user in User.query]}


if __name__ == '__main__':
    app.run(debug=True)
