import sqlite3

from flask import Flask, render_template

sqlite3.connect('database/database.db')

app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/connProf')
def connProf():
    return render_template('connP.html')




if __name__ == '__main__':
    
    app.run(debug=True)






