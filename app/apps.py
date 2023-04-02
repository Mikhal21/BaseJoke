from django.apps import AppConfig

import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/quote/<int:quote_id>')
def quote(quote_id):
    with open('quotes.json') as f:
        quotes = json.load(f)
    for quote in quotes:
        if quote['id'] == quote_id:
            return jsonify(quote)
    return jsonify({'error': 'Quote not found'})



class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

