from flask import Flask, request, render_template
import model

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
            <li><a href="/fball"> Men's Football </a></li>
        </ul>
    '''


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
    else:
        firstname = ''
        lastname = ''

    return render_template("hello.html", firstname=firstname, lastname=lastname)


@app.route('/bball', methods=['GET', 'POST'])
def bball():
    model.init_ball('umbball.csv')
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_ball_seasons(sortby, sortorder)
    else:
        seasons = model.get_ball_seasons()

    return render_template("seasons.html", seasons=seasons, ball='bball')


@app.route('/fball', methods=['GET', 'POST'])
def fball():
    model.init_ball('umfootball.csv')
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_ball_seasons(sortby, sortorder)
    else:
        seasons = model.get_ball_seasons()

    return render_template("seasons.html", seasons=seasons, ball='fball')


if __name__ == '__main__':
    app.run(debug=True)
