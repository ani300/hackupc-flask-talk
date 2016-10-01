from flask import Flask, render_template
import json, urllib
app = Flask(__name__)

def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()