from flask import Flask, request, jsonify
from autocomplete_api.redis_db import ac
from autocomplete_api.populate_db import init_db
import click

app = Flask(__name__)


@app.route("/")
def index():
    search_text = request.args.get("username")
    term = request.args.get("term")
    if not search_text:
        search_text = term
    if not search_text:    
        return "use it like ?username=ned"
    
    return jsonify(list(ac.search(search_text, limit=10)))


@app.cli.command()
def initdb():
    click.echo('Initializing database')
    init_db()

