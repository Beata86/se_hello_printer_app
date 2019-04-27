from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Grażyna"
msg = "Hello World!"


@app.route('/')
def index():
    name = request.args.get('name')
    output = request.args.get('output')
    if not output:
        output = PLAIN
    if not name:
        name = moje_imie
    return get_formatted(msg, name, output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
