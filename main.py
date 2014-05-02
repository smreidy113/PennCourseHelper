import requests
import base64
import json
import CourseList
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

majors = ['Accounting', 'Business Economic and Public Policy']


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
	html += "\n\t\t<input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += "\n\t\tSelect your major:"
	html += "\n\t\t\t<select name=\"major\">"
	for major in majors:
		html += "\n\t\t\t\t<option value=\"" + major + "</option>"
	html += "\n\t\t\t</select>"
	html += endCode()
	return html

@app.route('/listcourses', methods=['POST'])
def listcourses():
	print request
	html = ""
	html += startCode()
	html += request.form['dept1']
	for course in CourseList.courseList(request.form['coursestaken']):
		html += course[0]
	html += endCode()
	return html


#req = requests.get('http://api.penncoursereview.com/v1/coursehistories/CIS-110?token=' + api_key)

#print req.text

if __name__ == '__main__':
	app.run(debug=True)