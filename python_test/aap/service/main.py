from __future__ import division
from flask import Flask,  jsonify,  request
from python_test.aap.service.implementations.main_services import *
from flask.ext.cache import Cache

__author__ = "Aravind"

app = Flask(__name__)

# Check Configuring Flask-Cache section for more details
cache = Cache(app,config={'CACHE_TYPE': 'simple'})


@app.errorhandler(404)
def not_found():
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


# For email address details for GET method
@app.route('/message', methods=["GET", "POST"])
def api_get_email():

    result = get_email_details_service(cache)
    if len(result):
        return jsonify(result)
    elif len(result) == 0:
        return not_found()
    else:
        return email_notification()




#Main Function
if __name__ == '__main__':
    app.run(host="localhost", port=3000)