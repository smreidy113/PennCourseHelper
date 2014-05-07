import requests
import base64
import json
import Methods
import Data
from flask import Flask
from flask import jsonify
from flask import request
from requests.adapters import HTTPAdapter
import os

api_key = 'q2cm13OPDbZAzvJHGxWgtqcI1ZFp6K'
params = {'count': str(100)}
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))

app = Flask(__name__)

req = requests.get('http://api.penncoursereview.com/v1/depts?token=' + api_key)

# Starter HTML Code - Display on every page
def startCode():
	ans = ""
	ans = "<html>"
	ans += "\n\t<head>"
	ans += "\n\t\t<title>Penn Course Helper</title>"
	ans += "\n\t\t<link href=\"style\" rel=\"stylesheet\" type=\"text/css\">"
	ans += "\n\t</head>"
	ans += "\n\t<body>"
	ans += "\n\t\t<div id=\"wrapper\">"
	ans += "\n\t\t\t<div id=\"menu\">"
	ans += "\n\t\t\t\t<div class=\"menubar\">"
	ans += "\n\t\t\t\t\t<ul>"
	ans += "\n\t\t\t\t\t\t<div class=\"name\"><a href=\"/\">"
	ans += "<li>Penn Course Helper</li></a></div>"
	ans += "\n\t\t\t\t\t\t<li><a href=\"complete_schedule\">"
	ans += "Complete My Schedule</a></li>"
	ans += "\n\t\t\t\t\t\t<li><a href=\"choose_course\">Choose a Course</a></li>"
	ans += "\n\t\t\t\t\t</ul>"
	ans += "\n\t\t\t\t</div>"
	ans += "\n\t\t\t</div>"
	ans += "\n\t\t\t<div id=\"content\">"
	return ans

# Ending HTML Code - Display on every page
def endCode():
	ans = ""
	ans += "\n\t\t\t</div>"
	ans += "\n\t\t<div id=\"bottom\">"
	ans += "\n\t\t\t<br>Made in 2014 by Sean Reidy and Steven Jaffe."
	ans += " All rights reserved."
	ans == "\n\t\t</div>"
	ans += "\n\t\t</div>"
	ans += "\n\t</body>"
	ans += "\n</html>"
	return ans

# Home page
@app.route('/')
def start():	
	html = startCode()
	html += "\n\t\t\t"
	html += open("intro.txt").read()
	html += endCode()
	return html

# Interface display for the building your schedule app
@app.route('/complete_schedule')
def complete_schedule():
	html = ""
	html += startCode()
	html += "\n\t\t<br><br><form name=\"myform\" action=\"chooseSchedule\""
	html += " method=\"POST\">"
	html += "\n\t\tSelect your major (required):"
	html += "\n\t\t\t<select name=\"major\">"
	for major in Data.majors:
		html += "\n\t\t\t\t<option value=\"" + major + "\">" + major 
		html += "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t<br><br>Courses taken (e.g. PSYC101, HIST070...): <input type=\"text\" "
	html += "name = \"coursestaken\">"
	html += "\n\t\t\t<br><br>Year (required; enter 2015 or above): "
	html += "<input type=\"text\" name = \"year\">"
	html += "\n\t\t\t<br><br>1st Priority (required): <select name=\"priority1\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" 
		html += prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t<br>2nd Priority: <select name=\"priority2\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">"
		html += prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t<br>3rd Priority: <select name=\"priority3\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">"
		html += prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t<br><br><input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

# Interface display for the choose a course app
@app.route('/choose_course')
def choose_course():
	js = req.json()['result']
	html = startCode()
	html += "<br><br>"
	html += "\n\t\tSelect departments you want to choose a course from:"
	html += "\n\t\t<form name=\"myform\" action=\"listcourses\" method=\"POST\">"
	html += "\n\t\t\t<select multiple name=\"dept1\">"
	for dept in js['values']:
		html += "\n\t\t\t\t<option value=\"" + dept['id'] + "\">" + dept['id']
		html += " - " + dept['name'] + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t<br><br>Courses taken (e.g. PSYC101, HIST070...): <input type=\"text\" name = "
	html += "\"coursestaken\">"
	html += "\n\t\t\t<br><br>1st Priority (required): <select name=\"priority1\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" 
		html += prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t<br>2nd Priority: <select name=\"priority2\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" 
		html += prior + "</option>"
	html += "\n\t\t\t</select>"
	html += "\n\t\t\t<br>3rd Priority: <select name=\"priority3\">"
	for prior in Data.attrs.keys():
		html += "\n\t\t\t\t<option value=\"" + Data.attrs[prior][0] + "\">" 
		html += prior + "</option>"
	html += "\n\t\t\t</select>"
	
	html += "\n\t\t<br><br><input type=\"submit\" value=\"Submit\">"
	html += "\n\t\t</form>"
	html += endCode()
	return html

# When the user submits a request to choose a course, a list of up to 
# 10 recommendations are returned,
# in a table, along with the overall (normalized) score, and the scores 
# for attributes the user chose.
# This call make take several seconds to complete.
@app.route('/listcourses', methods=['POST'])
def listcourses():
	html = ""
	html += startCode()
	p1 = request.form['priority1']
	p2 = request.form['priority2']
	p3 = request.form['priority3']
	if p1 == None:
		html += "Please select a 1st priority"
		return html
	courses_taken = Methods.courseList(request.form['coursestaken'])
	s = Methods.rankedCoursesMultiple(request.form.getlist('dept1'), \
		p1,p2,p3,courses_taken)
	top_courses = Methods.getSubset(s, 10)
	html += "Here are your top " + str(len(top_courses)) + " recommendations:"
	html += "\n\t\t<br><br>"
	html += "\n\t\t<center><table>"
	html += "\n\t\t\t<tr>"
	html += "\n\t\t\t\t<td width=200><b>Course Name</b></td>"
	html += "\n\t\t\t\t<td width=200><b>Overall Score</b></td>"
	html += "\n\t\t\t\t<td width=200><b>" + Methods.key(p1) + "</b></td>"
	if p2 != "None":
		html += "\n\t\t\t\t<td width=200><b>" + Methods.key(p2) + "</b></td>"
	if p3 != "None":
		html += "\n\t\t\t\t<td width=200><b>" + Methods.key(p3) + "</b></td>"
	html += "\n\t\t\t</tr>"
	for course in top_courses:
		html += "\n\t\t\t<tr>"
		html += "\n\t\t\t\t<td>"
		for i in range(0,len(course[0])-1):
			html += Methods.link(course[0][i]) + ", "
		html += course[0][len(course[0])-1] + "</td>"
		html += "\n\t\t\t\t<td>" + str(course[1][0]) + "</td>"
		html += "\n\t\t\t\t<td>" + str(course[1][1]) + "</td>"
		if p2 != "None":
			html += "\n\t\t\t\t<td>" + str(course[1][2]) + "</td>"
		if p3 != "None":
			html += "\n\t\t\t\t<td>" + str(course[1][3]) + "</td>"
		html += "\n\t\t\t</tr>"
	html += "\n\t\t</table></center>"
	html += endCode()
	return html

# When the user makes a request to complete her schedule, this returns a 
# semester-by-semester
# list of courses to take. This may take several seconds to return the list.
@app.route('/chooseSchedule', methods=['POST'])
def chooseSchedule():
	html = startCode()
	taken = [i[0]+i[1] for i in Methods.courseList(request.form['coursestaken'])]
	year = int(request.form['year'])
	schedule = Methods.getMajorCourses(request.form['major'],taken, \
		request.form['priority1'],request.form['priority2'], \
		request.form['priority3'],year)
	#schedule = Methods.printSchedule(courses, taken, year)
	if schedule == "graduated":
		html += "You've graduated. You have no more semesters to take classes."
	elif schedule == "Not enough time":
		html += "Your schedule has too many prequesites to take in " 
		html += str((year - 2014) * 2) + " semesters"
	else:
		html += "\n\t\tLet's see what we came up with for you...<br><br>"
		html += "\n\t\t<center><table width=300>"
		overloaded = False
		# Print courses for each semester
		for i in range(0,len(schedule)/2):
			if len(schedule[2*i]) > 6 or len(schedule[2*i+1]) > 6:
				overloaded = True
			html += "\n\t\t\t<tr>"
			for j in range(2):
				html += "\n\t\t\t\t<td>"
				html += "\n\t\t\t\t\t<center><table>"
				html += "<b>Semester " + str(schedule.index(schedule[2*i+j]) + 1)
				html += "</b>"
				for course in schedule[2*i+j]:
					html += "\n\t\t\t<tr>"
					html += "\n\t\t\t\t<td>"
					html += Methods.link(str(course))
					html += "\n\t\t\t\t</td>"
					html += "\n\t\t\t</tr>"
				html += "\n\t\t\t\t\t</table></center>"
				html += "\n\t\t\t\t\t<br>"
				html += "\n\t\t\t\t</td>"
			html += "\n\t\t\t</tr>"
		html += "\n\t\t</table></center>"
		html += "<br>" + "Don't forget to allot time for sector requirements: "
		html += "Our decide on a course module can help!" + "</br>"
		if overloaded:
			html += "<br>" + "Even without sectors, you're overloaded. You "
			html += "may need more years" + "</br>"
	html += endCode()
	return html

# Load CSS stylesheet
@app.route('/style')
def getStyle():
	return open("style.css").read()

if __name__ == '__main__':
	#port = int(os.environ.get('PORT',5000))
	#app.run(host='0.0.0.0', port=port, debug=True)
	pass