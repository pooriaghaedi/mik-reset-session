from flask import Flask, flash, redirect, render_template, request, session, abort, render_template
from Domain import Domain
from mikssh import Mikssh

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def session():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['passwd']
        if Domain.authenticate(Domain, user=user, passwd=password):
            Mikssh.connect(Mikssh)
            print("changed user is %s " % user)
            Mikssh.send_command(Mikssh, "ip hotspot active remove [find user=%s]" % user)
            Mikssh.send_command(Mikssh, "ip hotspot cookie remove [find user=%s]" % user)
            return render_template('index.html', success="success")
        else:
            return render_template('index.html', error="error")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
