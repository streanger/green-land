import subprocess

# 3rd party
from rich import print
from flask import Flask
from flask import request
from flask import render_template

# my modules
from active_code_page import get_active_code_page

"""
useful:
    https://flask.palletsprojects.com/en/1.1.x/cli/
    Unix Bash (Linux, Mac, etc.):
        $ export FLASK_APP=hello
        $ flask run
    Windows CMD:
        > set FLASK_APP=app
        > flask run
    Windows PowerShell:
        > $env:FLASK_APP = "app"
        > flask run

links:
    https://stackoverflow.com/questions/30011170/flask-application-how-to-link-a-javascript-file-to-website
    https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
    https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application

"""

CODE_PAGE = get_active_code_page()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def run_command(command):
    """run local system command and return output
    https://stackoverflow.com/questions/49150550/python-subprocess-encoding
    """
    try:
        response = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as err:
        print(f'[red]{err}[/red]')
        return err
    decoded = response.decode(CODE_PAGE)
    return decoded


@app.route('/', methods = ['GET', 'POST'])
def command():
    if request.method == "GET":
        return render_template('index.html')

    command = request.form['command']
    print('command: [red]{}[/red]'.format(command))
    output = run_command(command)
    print('output: [blue]{}[/blue]'.format(output))
    return render_template('index.html', message=output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
