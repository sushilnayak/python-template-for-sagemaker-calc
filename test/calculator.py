import flask

import handler as CalcClass

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():

    status = 200
    return flask.Response(response='\n', status=status, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():

    try:
        calculation = CalcClass.calc_method(flask.request)
    except:
        return flask.Response(response='There was issue with the calculator, Please make sure you have tested it before deploying', status=415, mimetype='text/plain')

    return flask.Response(response=calculation["response"] , status=calculation["statusCode"], mimetype=calculation["mimetype"])

app.run(port=5000)