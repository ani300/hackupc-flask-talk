from flask import Flask, render_template
import json, urllib
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index_final.html')

@app.route('/hackupc')
@app.route('/hackupc/<visitor>')
def hackupc(visitor = ''):
  return render_template('hackupc_final.html', visitor=visitor)

@app.route('/epic')
def epic():
  images_json = urllib.urlopen('http://epic.gsfc.nasa.gov/api/images.php?w=-15&e=30.0')
  images_list = json.loads(images_json.read().decode("utf-8"))
  return render_template('epic_final.html', images=images_list)

if __name__ == "__main__":
  app.run()
