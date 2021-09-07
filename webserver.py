from flask import Flask, redirect, render_template, send_from_directory, url_for
from threading import Thread
import os

app = Flask('EndyBot - Discord', template_folder='templates', static_folder='static')

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/add/')
def add():
  return redirect("https://discord.com/api/oauth2/authorize?client_id=699911346367627374&permissions=8&scope=bot")

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

def run():
  app.run(host = "0.0.0.0", port = 2020)

def execute():
  t = Thread(target=run)
  t.start()