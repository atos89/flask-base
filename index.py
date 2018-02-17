from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    view_params = {}
    view_params['title'] = 'base application.';

    return render_template('index.html', view_params=view_params)


if __name__ == '__main__':
    app.run(debug=True)