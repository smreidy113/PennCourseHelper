import requests
import base64
import json
import Methods
import Data
from flask import Flask
from flask import jsonify
from flask import request
from requests.adapters import HTTPAdapter

api_key = 'q2cm13OPDbZAzvJHGxWgtqcI1ZFp6K'
params = {'count': str(100)}
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))

app = Flask(__name__)

req = requests.get('http://api.penncoursereview.com/v1/depts?token=' + api_key)



def startCode():
	ans = ""
	ans = "<html>"
	ans += "\n\t<head>"
	ans += "\n\t\t<title>Penn Course Helper</title>"
	ans += "\n\t</head>"
	ans += "\n\t<body>"
	return ans

def endCode():
	ans = ""
	ans += "\n\t</body>"
	ans += "\n</html>"
	return ans


@app.route('/')
def start():	
	js = req.json()['result']
	html = ""
	html += startCode()
	html += "\n\t\tSelect a department:"
	html += "\n\t\t<form name=\"myform\" action=\"listcourses\" method=\"POST\">"
	html += "\n\t\t\t<select name=\"dept1\">"
	for dept in js['values']:
		html += "\n\t\t\t\t<option value=\"" + dept['id'] + "\">" + dept['id'] + " - " + dept['name'] + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\tCourses taken: <input type=\"text\" name = \"coursestaken\">"
	html += "\n\t\t\t1st Priority: <select name=\"priority1\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t2nd Priority: <select name=\"priority2\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t3rd Priority: <select name=\"priority3\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\tSelect your major:"
	html += "\n\t\t\t<select name=\"major\">"
	for major in majors:
		html += "\n\t\t\t\t<option value=\"" + Attribute.majors[major] + "\">" + major + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t</select>"
	html += "\n\t\tSelect your minor:"
	html += "\n\t\t\t<select name=\"minor\">"
	for minor in minors:
		html += "\n\t\t\t\t<option value=\"" + Attribute.minors[minor] + "\">" + minor + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t<input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

@app.route('/listcourses', methods=['POST'])
def listcourses():
	html = ""
	html += startCode()
	html += request.form['dept1']
	for course in Methods.courseList(request.form['coursestaken']):
		html += course[0]
	html += endCode()
	return html


#req = requests.get('http://api.penncoursereview.com/v1/coursehistories/CIS-110?token=' + api_key)

#print req.text

if __name__ == '__main__':
	app.run(debug=True)