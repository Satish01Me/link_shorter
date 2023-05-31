from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def short():
    link=request.form['link']
    short_url = pyshorteners.Shortener().tinyurl.short(link)

    return render_template("index.html",res=short_url)

    


if __name__ == '__main__':
    app.run(debug=True)
