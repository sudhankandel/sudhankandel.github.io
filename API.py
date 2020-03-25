import flask,requests
from flask import request, jsonify
from TimeSeries import Extract_TimeSeries
from Detail import Yesterday,Today
from Nepal import Get_row
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


daily_data=Extract_TimeSeries()
yesterday_data=Yesterday()
today_data=Today()
nepal=Get_row()


app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return '''<h1>corona Data</h1>'''
@app.route('/api/daily', methods=['GET'])
def api_Daily():
    return jsonify(daily_data)
@app.route('/api/yesterday', methods=['GET'])
def api_yesterday():
    return jsonify(yesterday_data)
@app.route('/api/today', methods=['GET'])
def api_Today():
    return jsonify(today_data)
@app.route('/api/nepal', methods=['GET'])
def api_nepal():
    return jsonify(nepal)

app.run()
