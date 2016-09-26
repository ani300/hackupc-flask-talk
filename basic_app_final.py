from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hackupc/<visitor>')
def hackupc(visitor):
  return render_template('hackupc.html', visitor=visitor)

if __name__ == "__main__":
  app.run()
