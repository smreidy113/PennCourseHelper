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
	html = "<br>" + "Welcome to PenngineeringCourseHelper!" + "</br>"
	html += startCode()
	html += "\n\t\t<a href=\"complete_schedule\">Complete my schedule</a>"
	html += "\n\t\t<br><a href=\"choose_course\">Decide on a course</a>"
	html += endCode()
	return html

@app.route('/complete_schedule')
def complete_schedule():
	html = ""
	html += startCode()
	html += "\n\t\t<form name=\"myform\" action=\"chooseSchedule\" method=\"POST\">"
	html += "\n\t\tSelect your major:"
	html += "\n\t\t\t<select name=\"major\">"
	for major in Data.majors:
		html += "\n\t\t\t\t<option value=\"" + major + "\">" + major + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\tCourses taken: <input type=\"text\" name = \"coursestaken\">"
	html += "\n\t\t<input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

@app.route('/choose_course')
def choose_course():
	js = req.json()['result']
	html = startCode()
	html += "\n\t\tSelect a department:"
	html += "\n\t\t<form name=\"myform\" action=\"listcourses\" method=\"POST\">"
	html += "\n\t\t\t<select multiple name=\"dept1\">"
	for dept in js['values']:
		html += "\n\t\t\t\t<option value=\"" + dept['id'] + "\">" + dept['id'] + " - " + dept['name'] + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\tSelect your major:"
	html += "\n\t\t\t<select name=\"major\">"
	for major in Data.majors:
		html += "\n\t\t\t\t<option value=\"" + major + "\">" + major + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\tCourses taken: <input type=\"text\" name = \"coursestaken\">"
	html += "\n\t\t\t1st Priority: <select name=\"priority1\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t2nd Priority: <select name=\"priority2\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t3rd Priority: <select name=\"priority3\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	
	html += "\n\t\t<input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

@app.route('/listcourses', methods=['POST'])
def listcourses():
	html = ""
	html += startCode()
	print request.form
	req1 = requests.get('http://api.penncoursereview.com/v1/depts/' + request.form['dept1'] + '/reviews?token=' + api_key)
	p1 = request.form['priority1']
	p2 = request.form['priority2']
	p3 = request.form['priority3']
	revinfo = req1.json()['result']['values']
	s = Methods.rankedCourses(revinfo,p1,p2,p3)
	for course in s:
		html += "<br>" + course[0] + " " + str(course[1])
	#for course in Methods.courseList(request.form['coursestaken']):
	#	html += course[0]
	html += endCode()
	return html

@app.route('/chooseSchedule', methods=['POST'])
def chooseSchedule():
	html = StartCode()
	html += "Nothing here yet"
	html += endCode()
	return html

#req = requests.get('http://api.penncoursereview.com/v1/coursehistories/CIS-110?token=' + api_key)

#print req.text

if __name__ == '__main__':
	app.run(debug=True)