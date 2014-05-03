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
	html += "\n\t\t\t<select name=\"dept1\">"
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
	
	html += "\n\t\t<input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

@app.route('/listcourses', methods=['POST'])
def listcourses():
	html = ""
	html += startCode()
	req1 = requests.get('http://api.penncoursereview.com/v1/depts/' + request.form['dept1'] + '/reviews?token=' + api_key)
	p1 = request.form['priority1']
	p2 = request.form['priority2']
	p3 = request.form['priority3']
	revinfo = req1.json()['result']['values']
	courseDict = {}
	ratingsDict = {}
	for course in revinfo:
		courseName = course['section']['primary_alias']
		if courseName[0:-4] in courseDict.keys():
			courseDict[courseName[0:-4]].append(course)
		else:
			courseDict[courseName[0:-4]] = [course]
			ratingsDict[courseName[0:-4]] = 0.0
	for course in courseDict.keys():
		sumRating1, sumRating2, sumRating3 = 0.0, 0.0, 0.0
		for section in courseDict[course]:
			sumRating1 += float(section['ratings'].get(str('r'+p1),0.0))
			sumRating2 += float(section['ratings'].get(str('r'+p2),0.0))
			sumRating3 += float(section['ratings'].get(str('r'+p3),0.0))
		avgRating1 = sumRating1/len(courseDict[course])
		avgRating2 = sumRating2/len(courseDict[course])
		avgRating3 = sumRating3/len(courseDict[course])
		ratingsDict[course] = (3*avgRating1**2 + 2*avgRating2**2 + 1*avgRating3**2) / 96 * 10
	print ratingsDict.items()
	s = ratingsDict.items()
	s.sort(key=lambda x:x[1])
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