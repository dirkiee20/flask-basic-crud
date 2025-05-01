from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

# def Index():
#     return "<h1>Hello, World!</h1>"

def Index():
    return render_template('index.html')

@app.route('/user/<name>')
def User(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
