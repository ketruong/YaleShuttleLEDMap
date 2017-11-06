import thread

from transloc_data import *
from flask import Flask, make_response
app = Flask(__name__)
#lol website to control stuff
def run():
    print "starting web server..."
    app.run(host='0.0.0.0')

toggle_cb = None
brightness_cb = None

def setup(t, b):
    global toggle_cb
    global brightness_cb
    toggle_cb = t
    brightness_cb = b
    #new thread 
    thread.start_new_thread(run, ())

@app.route("/toggle/<state>")
#lower something in the state 
def toggle(state):
    return str(toggle_cb(state)).lower()

@app.route("/brightness/<level>")
#lower brightness when go to some website
def brightness(level):
    return str(brightness_cb(level)).lower()

@app.route("/robots.txt")
def no_robots():
    nope = "User-agent: *\nDisallow: /"
    resp = make_response(nope)
    #lol just learned this but 
    #make_response adds a new response header to the http response 
    #learn more at https://www.tutorialspoint.com/http/http_responses.htm
    resp.headers['Content-type'] = 'text/plain'
    return resp

