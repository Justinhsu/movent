from __future__ import print_function
from flask import Flask, jsonify, send_from_directory, request, url_for
import glob
import os
from os.path import join
from stat import S_ISREG, ST_CTIME, ST_MODE
import sys, time
import csv
import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
# from werkzeug.security import safe_join

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def staticPage():
	return app.send_static_file('index.html')

@app.route('/generateChart', methods=['GET', 'POST'])
def generateGraphs():
	if request.method == 'POST':
		data = request.get_json();
		print(data);

		store = oauth_file.Storage('token.json');
		creds = store.get()
		if not creds or creds.invalid:
			flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
			creds = tools.run_flow(flow, store)
		service = build('calendar', 'v3', http=creds.authorize(Http()))	

		#call the calendar api
		now = datetime.datetime.utcnow().isoformat() + 'Z' # Z indicates UTC time
		# print('Getting the upcoming 10 events')
		# events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
		# events = events_result.get('items', [])

		# if not events:
		# 	print('no upcoming events found.')
		# for event in events:
		# 	start = event['start'].get('datetime', event['start'].get('date'))
		# 	print(start, event['summary'])
	    # creds = store.get()
		data = service.events().insert(calendarId='primary',body=data).execute()
	return app.send_static_file('index.html')

##################### ERROR HANDLING ###########################################
@app.errorhandler(500)
def internal_error(error):

    return "500 error"


if __name__ == '__main__':
	app.run(debug=True)

