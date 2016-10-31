import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging


# Our own module
import taco_loc

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.secret_key  # Should allow using session variables

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('karaoke.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("/")
    return flask.render_template('page_not_found.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############


@app.route("/_tacobell_locations")
def _tacobell_locations():
    '''
    Get locations from file and transmit to
    the javascript as a JSON

    If this was to be extended in the future, pass the location of the file here
    '''
    locations = taco_loc.get_locations()
    result={ "locations": locations}
    return jsonify(result=result)




#############

if __name__ == "__main__":
    # Standalone.
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server,
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    #FIXME:  Debug cgi interface
    app.debug=False
