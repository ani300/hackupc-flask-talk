from flask import Flask, render_template
app = Flask(__name__)

def hackupc(visitor):
  return render_template('hackupc.html')

if __name__ == "__main__":
  app.run()
