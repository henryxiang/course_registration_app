from flask import Flask

app = Flask('Flask Demo')


@app.route('/', methods=['GET'])
def demo():
    return '<h1>Hello, world!</h1>'


@app.route('/user')
def user():
    pass


if __name__ == '__main__':
    app.run(debug=True)
