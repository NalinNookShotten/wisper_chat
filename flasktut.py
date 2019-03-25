from flask import Flask, render_template
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'dashfsadfafgsdfdhfgdshf'

@app.route("/")
def index():
    return render_template('./home.html')

@app.route("/about")
def about():
    return "<h1>about page<h1>"

if __name__ == '__main__':
    app.run(debug=True)
