from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/<username>')
def userpage(username=None):
    return f'hello {username}'


@app.route('/<username>/greet')
def greeting(username):
    return render_template('sample.html',name=username)
  

if __name__ == '__main__':

    app.run(debug=True)
