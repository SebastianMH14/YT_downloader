from flask import Flask, render_template, request
from convert_yt import ConvertYt
""" api to download"""


app = Flask(__name__)

@app.route('/')
def index():
    """ index page"""
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_url():
    url = request.form['url']
    file = ConvertYt(url)
    title = file.get_title()
    img = file.get_tumbnails()
    size = file.get_size()
   # return "<h2>Fail</h2>"
    return render_template('index.html', url=url, title=title, img=img, size=size)


if __name__ == '__main__':
    app.run(debug=True)