from flask import Flask, render_template

app = Flask(__name__)
print(__name__)
@app.route('/<username>/<int:post_id>')
def index(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route('/favicon.ico')
def favicon():
    return render_template('index.html')


@app.route('/about')
def blog():
    return render_template('about.html')
