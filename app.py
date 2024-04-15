#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, session, jsonify, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.secret_key = 'your_secret_key'  # Change this to a secure key for security

YOUR_DOMAIN = 'http://localhost:4242'

# Sample product catalog with price_ids


@app.route('/')
def HOME():
    return render_template('index.html')

@app.route('//creation-site-web')
def web():
    return render_template('site-web.html')

@app.route('/expertises')
def expertises():
    return render_template('expertises.html')

@app.route('/projets')
def projets():
    return render_template('projets.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/mentions-legales')
def mentions():
    return render_template('mentions-legales.html')
@app.route('/cgu')
def cgu():
    return render_template('cgu.html')
@app.route('/cgv')
def cgv():
    return render_template('cgv.html')

if __name__ == '__main__':
    app.run(port=4242)

