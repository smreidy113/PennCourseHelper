import re
import json
import requests
from requests.adapters import HTTPAdapter
import random
import Data

api_key = 'q2cm13OPDbZAzvJHGxWgtqcI1ZFp6K'
params = {'count': str(100)}
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))

def courseList(s):
	s = s + ","
	ans = []
	e = r'([A-Za-z]{2,4}).*?([0-9]{3}),'
	for match in re.finditer(e,s):
		ans.append((match.group(1).upper(),match.group(2)))
	return ans

def key(p):
	for k,v in Data.attrs.iteritems():
		if p == v[0]:
			return k

def rankedCourses(revinfo,p1,p2,p3):
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
			if (Data.attrs[key(p1)][1]):
				sumRating1 += float(section['ratings'].get(str('r'+p1),0.0))
			else:
				sumRating1 += float(4 - float(section['ratings'].get(str('r'+p1),0.0)))
			if (Data.attrs[key(p2)][1]):
				sumRating2 += float(section['ratings'].get(str('r'+p2),0.0))
			else:
				sumRating2 += float(4 - float(section['ratings'].get(str('r'+p2),0.0)))
			if (Data.attrs[key(p3)][1]):
				sumRating3 += float(section['ratings'].get(str('r'+p3),0.0))
			else:
				sumRating3 += float(4 - float(section['ratings'].get(str('r'+p3),0.0)))
		avgRating1 = sumRating1/len(courseDict[course])
		avgRating2 = sumRating2/len(courseDict[course])
		avgRating3 = sumRating3/len(courseDict[course])
		overallRank = (3*avgRating1**2 + 2*avgRating2**2 + 1*avgRating3**2) / 96 * 10
		if Data.attrs[key(p1)][1]:
			avgRating1 = 4 - avgRating1
		if Data.attrs[key(p1)][1]:
			avgRating2 = 4 - avgRating2
		if Data.attrs[key(p1)][1]:
			avgRating3 = 4 - avgRating3
		ratingsDict[course] = (overallRank,avgRating1,avgRating2,avgRating3)
	#print ratingsDict.items()
	s = ratingsDict.items()
	s.sort(key=lambda x:x[1][0])
	return s

def getSubset(s,num_needed):
	# return subset
	if num_needed > len(s):
		return [x for x in s]
	else:
		l = []
		for i in range(num_needed):
			l.append(s[i])
		return l

def rankedCoursesMultiple(l,p1,p2,p3, taken):
	s = []
	print taken
	for dept in l:
		revinfo = requests.get('http://api.penncoursereview.com/v1/depts/' + dept + '/reviews?token=' + api_key).json()['result']['values']
		s.extend(rankedCourses(revinfo,p1,p2,p3))
	s.sort(key=lambda x:x[1][0], reverse=True)
	courseNameList = [i[0] for i in s]
	print courseNameList
	for course in taken:
		courseStr = course[0] + "-" + course[1]
		print courseStr
		if courseStr in courseNameList:
			s = [(name,scores) for name,scores in s if name != courseStr]
	#print s
	return s


required = {}
optional = {}

def getMajorCourses(major, taken, p1, p2, p3):
	opt_credits_needed = Data.major_courses[major]["Optional"][0][0]
	level = Data.major_courses[major]["Optional"][0][2]
	needed_in_level = Data.major_courses[major]["Optional"][0][1]
	for course in Data.major_courses[major]["Required"]:
		if course[0] not in taken:
			required[course[0]] = course[1:]
	for opt_course in Data.major_courses[major]["Optional"][1:]:
		if opt_course[0] not in taken:
			optional[opt_course[0]] = opt_course[1:]
		else:
			opt_credits_needed -= opt_course[1]
			if course[0][-3] == level[0]:
				needed_in_level -= opt_course[1]
	ranked_opt = [x[0] for x in rankedCoursesMultiple(optional.keys(), p1, p2, p3, taken)]
	opt_courses = []
	iter = 0
	credits = 0
	level_credits
	while credits < opt_credits_needed and level_credits < needed_in_level:
		course = ranked_opt[iter]
		opt_courses.append[course]
		credits += optional[course[0]]
		if course[-3] == level[0]:
			level_credits += optional[course[0]]
		iter += 1
		if credits > opt_credits_needed:
			for x in opt_courses:
				removed = false
				for prereq in optional[x][1]:
					if not taken.contains(prereq) and not required.keys().contains(prereq) and not opt_courses.contains(prereq):
						opt_courses.remove(x)
						removed = true
						credits -= optional[x[0]]
						break
				if not removed:
					for coreq in optional[x][1]:
						if not taken.contains(coreq) and not required.keys().contains(coreq) and not opt_courses.contains(coreq):
								opt_courses.remove(x)
								optional[x[0]]
								break
		if credits > opt_credits_needed:
			 if needed_in_level > level_credits:
				iter2 = iter - 1
				if opt_courses[iter][-3] != level[0]:
					worst_curr_class = opt_courses[iter]
					opt_courses.remove(worst_curr_class)
					credits -= optional[worst_curr_class][0]
				else:
					iter2 -= 1
	courses = required.keys() + opt_courses
	return courses

def printSchedule(l, year):
	if (year <= 2014):
		html += "You've graduated. You have no more semesters to take classes."
	sorted_courses = l
	num_per_semester = float(len(l)) / (2 * (year - 2014))
	for i in range((year-2014)*2):
		html += "<br> Semester" + str(i) + "</br>"
		sorted_corses = sorted(sorted_courses, key=lambda x: int(x[-3:]))
		credits = 0
		courses = []
		course_iter = 0
		need_prereq = []
		while credits < num_per_semester and course_iter < len(sorted_courses):
			course = sorted_courses[course_iter]
			fulfills_prereq = true
			for prereq in optionalRequiredUnknown(course, 1):
				if not taken.contains(prereq):
					fulfills_prereq = false
					break
			if not fulfills_prereq:
				need_prereq.append[course]
				sorted_courses.remove(course)
				continue
			else:
				classes.append(course)
				credits += optionalRequiredUnknown(course, 0)
				for coreq in optionalRequiredUnknown(course, 2):
					classes.append(coreq)
					credits += optionalRequiredUnknown(coreq, 0)
					try:
						sorted_classes.remove(coreq)
					except:
						pass
			course_iter += 1
		taken.extend(courses)
		for course in courses:
			html += "<br>" + course + "</br>"
			sorted_courses.remove(course)
		for course in need_prereq:
			sorted_courses.append(course)
	html += "<br>" + "Make sure you also fill your sector requirements!" + "</br>"


def optionalRequiredUnknown(course, field):
	try: 
		x = required[course][field]
	except:
		x = optional[course][field]
	return x

