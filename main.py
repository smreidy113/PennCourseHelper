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
	ans += "\n\t\t<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\">"
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
	html += "\n\t\tSelect your major (required):"
	html += "\n\t\t\t<select name=\"major\">"
	for major in Data.majors:
		html += "\n\t\t\t\t<option value=\"" + major + "\">" + major + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\tCourses taken: <input type=\"text\" name = \"coursestaken\">"
	html += "\n\t\t\tYear (required; enter 2015 or above): <input type=\"text\" name = \"year\">"
	html += "\n\t\t\t1st Priority (required): <select name=\"priority1\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t2nd Priority (required): <select name=\"priority2\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t3rd Priority (required): <select name=\"priority3\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" + prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t<input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

@app.route('/choose_course')
def choose_course():
	js = req.json()['result']
	html = startCode()
	html += "\n\t\tSelect departments you want to choose a course from:"
	html += "\n\t\t<form name=\"myform\" action=\"listcourses\" method=\"POST\">"
	html += "\n\t\t\t<select multiple name=\"dept1\">"
	for dept in js['values']:
		html += "\n\t\t\t\t<option value=\"" + dept['id'] + "\">" + dept['id'] + " - " + dept['name'] + "</option>"
	html += "\n\t\t\t</select>"
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
	#print request.form.getlist('dept1')
	p1 = request.form['priority1']
	p2 = request.form['priority2']
	p3 = request.form['priority3']
	courses_taken = Methods.courseList(request.form['coursestaken'])
	print courses_taken
	s = Methods.rankedCoursesMultiple(request.form.getlist('dept1'),p1,p2,p3,courses_taken)
	top_courses = Methods.getSubset(s, 5)
	html += "<br>" + "Here are your top " + str(len(top_courses)) + " recommendations"
	html += "\n\t\t<table>"
	html += "\n\t\t\t<tr>"
	html += "\n\t\t\t\t<td>Course Name</td>"
	html += "\n\t\t\t\t<td>Overall Score</td>"
	html += "\n\t\t\t\t<td>" + Methods.key(p1) + "</td>"
	html += "\n\t\t\t\t<td>" + Methods.key(p2) + "</td>"
	html += "\n\t\t\t\t<td>" + Methods.key(p3) + "</td>"
	html += "\n\t\t\t</tr>"
	for course in top_courses:
		html += "\n\t\t\t<tr>"
		html += "\n\t\t\t\t<td>"
		for i in range(0,len(course[0])-1):
			html += course[0][i] + ", "
		html += course[0][len(course[0])-1] + "</td>"
		html += "\n\t\t\t\t<td>" + str(course[1][0]) + "</td>"
		html += "\n\t\t\t\t<td>" + str(course[1][1]) + "</td>"
		html += "\n\t\t\t\t<td>" + str(course[1][2]) + "</td>"
		html += "\n\t\t\t\t<td>" + str(course[1][3]) + "</td>"
		html += "\n\t\t\t</tr>"
		#html += "<br>" + course[0] + " " + str(course[1])
	html += "\n\t\t</table>"
	#for course in Methods.courseList(request.form['coursestaken']):
	#	html += course[0]
	html += endCode()
	return html

@app.route('/chooseSchedule', methods=['POST'])
def chooseSchedule():
	taken = [i[0]+i[1] for i in Methods.courseList(request.form['coursestaken'])]
	year = int(request.form['year'])
	print taken
	courses = Methods.getMajorCourses(request.form['major'],taken,request.form['priority1'],request.form['priority2'],request.form['priority3'])
	schedule = Methods.printSchedule(courses, taken, year)
	print schedule
	if schedule == "graduated":
		html = "You've graduated. You have no more semesters to take classes."
	elif schedule == "Not enough time":
		html = "Your schedule has too many prequesites to take in " + str((year - 2014) * 2) + " semesters"
	else:
		html = startCode()
		overloaded = False
		for semester_schedule in schedule:
			if len(semester_schedule) > 6:
				overloaded = True
			html += "<br>" + "Semester" + str(schedule.index(semester_schedule) + 1) + "</br>"
			for course in semester_schedule:
				html += "<br>" + str(course) + "</br>"
		html += "<br>" + "Don't forget to allot time for sector requirements: Our decide on a course module can help!" + "</br>"
		if overloaded:
			html += "<br>" + "Even without sectors, you're overloaded. You may need more years!" + "</br>"
	html += endCode()
	return html

#req = requests.get('http://api.penncoursereview.com/v1/coursehistories/CIS-110?token=' + api_key)

#print req.text

if __name__ == '__main__':
	app.run(debug=True)