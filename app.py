# import necessary modules
from flask import Flask, render_template


# creare a flask instance
app = Flask(__name__)


# define the route
@app.route('/')
def index_html():
    return render_template('index.html')


# entery point and run the "app"
if __name__ == '__main__':
    app.run()
