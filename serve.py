from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__, static_url_path='')
from flask import request


#@app.errorhandler(404)
#def page_not_found(e):
#    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/fb_friendsort.css')
def serve_css():
    return app.send_static_file('fb_friendsort.css')

@app.route('/fb_friendsort.js')
def serve_js():
    return app.send_static_file('fb_friendsort.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
