from flask import Flask, jsonify, send_from_directory, request, url_for
import glob
import os
from os.path import join
from stat import S_ISREG, ST_CTIME, ST_MODE
import sys, time
import csv
# from werkzeug.security import safe_join

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def staticPage():
	return app.send_static_file('index.html')

@app.route('/generateChart', methods=['GET', 'POST'])
def generateGraphs():
	if request.method == 'POST':
		data = request.get_json();
		print(data);
	return app.send_static_file('index.html')


##################### ERROR HANDLING ###########################################
@app.errorhandler(500)
def internal_error(error):

    return "500 error"


if __name__ == '__main__':
	app.run(debug=True)

