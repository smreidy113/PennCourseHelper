import re
import json
import requests
from requests.adapters import HTTPAdapter
import random
import Data
import math

api_key = 'q2cm13OPDbZAzvJHGxWgtqcI1ZFp6K'
params = {'count': str(100)}
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))

def eliminateCrossListings(l,d):
	ans = []
	for i in l:
		for j in i:
			if j in [x[0] for x in d['Required']] or j in [x[0] for x in d['Optional']]:
				ans.append(j)
	return ans

def courseList(s):
	s = s + ","
	ans = []
	e = r'([A-Za-z]{2,4}).*?([0-9]{3}),'
	for match in re.finditer(e,s):
		ans.append((match.group(1).upper(),match.group(2)))
	return ans

def findInClass(major,code):
	for course in Data.major_courses[major]["Required"]:
		if code == course[0]:
			return course
	for course in Data.major_courses[major]["Optional"]:
		if code == course[0]:
			return course

def key(p):
	for k,v in Data.attrs.iteritems():
		if p == v[0]:
			return k

def removeDash(s):
	e = r'([A-Za-z]{2,4}).*?([0-9]{3})'
	for match in re.finditer(e,s):
		return match.group(1) + match.group(2)

def rankedCourses(revinfo,p1,p2,p3):
	courseDict = {}
	ratingsDict = {}
	altNamesDict = {}
	for course in revinfo:
		courseName = course['section']['primary_alias']
		if courseName[0:-4] in courseDict.keys():
			courseDict[courseName[0:-4]].append(course)
		else:
			courseDict[courseName[0:-4]] = [course]
			ratingsDict[courseName[0:-4]] = 0.0
			altNamesDict[courseName[0:-4]] = [removeDash(s[0:-4]) for s in course['section']['aliases']]
	for course in courseDict.keys():
		sumRating1, sumRating2, sumRating3 = 0.0, 0.0, 0.0
		for section in courseDict[course]:
			if (Data.attrs[key(p1)]) != "None":
				if (Data.attrs[key(p1)][1]):
					sumRating1 += float(section['ratings'].get(str('r'+p1),0.0))
				else:
					sumRating1 += float(4 - float(section['ratings'].get(str('r'+p1),0.0)))
			if (Data.attrs[key(p2)]) != "None":
				if (Data.attrs[key(p2)][1]):
					sumRating2 += float(section['ratings'].get(str('r'+p2),0.0))
				else:
					sumRating2 += float(4 - float(section['ratings'].get(str('r'+p2),0.0)))
			if (Data.attrs[key(p3)]) != "None":
				if (Data.attrs[key(p3)][1]):
					sumRating3 += float(section['ratings'].get(str('r'+p3),0.0))
				else:
					sumRating3 += float(4 - float(section['ratings'].get(str('r'+p3),0.0)))
		avgRating1 = sumRating1/len(courseDict[course])
		avgRating2 = sumRating2/len(courseDict[course])
		avgRating3 = sumRating3/len(courseDict[course])
		overallRank = (3*avgRating1**2 + 2*avgRating2**2 + 1*avgRating3**2) / 96 * 10
		if not Data.attrs[key(p1)][1]:
			avgRating1 = 4 - avgRating1
		if not Data.attrs[key(p1)][1]:
			avgRating2 = 4 - avgRating2
		if not Data.attrs[key(p1)][1]:
			avgRating3 = 4 - avgRating3
		ratingsDict[course] = (overallRank,avgRating1,avgRating2,avgRating3)
	s = ratingsDict.items()
	for i in range(0,len(s)):
		s[i] = (altNamesDict[s[i][0]],s[i][1])
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

def isIn(a,b):
	for i in a:
		if i in b:
			return True
	return False

def rankedCoursesMultiple(l,p1,p2,p3, taken):
	s = []
	ind_courses_temp = []
	depts = True
	if len(l[0]) > 4:
		depts = False
		ind_courses = l
		l = []
		ind_courses_temp = []
		e = r'([A-Z]{2,4}).*?([0-9]{3})'
		for ind_course in ind_courses:
			for match in re.finditer(e,ind_course):
				if match.group(1) not in l:
					l.append(match.group(1))
				ind_courses_temp.append(match.group(1) + match.group(2))
	ind_coures = ind_courses_temp
	for dept in l:
		revinfo = requests.get('http://api.penncoursereview.com/v1/depts/' + dept + '/reviews?token=' + api_key).json()['result']['values']
		s.extend(rankedCourses(revinfo,p1,p2,p3))
	s.sort(key=lambda x:x[1][0], reverse=True)
	courseNameList = [i[0] for i in s]
	for course in taken:
		courseStr = course[0] + "-" + course[1]
		if courseStr in courseNameList:
			s = [(name,scores) for name,scores in s if courseStr not in name]
	if depts == False:
		s = [(name,scores) for name,scores in s if isIn(name, ind_courses_temp)]
	return s

# Dictionaries of required and optional major course.
# Maps course IDs to tuple (credits, prereqs, coreqs)
# Filled by getMajorCourses, referenced in printSchedule (via optionalRequiredUnknown)
required = {}
optional = {}

def getMajorCourses(major, taken, p1, p2, p3):
	# Find certain requirements for major
	opt_credits_needed = Data.major_courses[major]["Optional"][0][0]
	level = Data.major_courses[major]["Optional"][0][2]
	needed_in_level = Data.major_courses[major]["Optional"][0][1]
	# Fill required dictionary
	for course in Data.major_courses[major]["Required"]:
		if course[0] not in taken:
			required[course[0]] = course[1:]
	# Fill optional dictionary
	for opt_course in Data.major_courses[major]["Optional"][1:]:
		if opt_course[0] not in taken:
			optional[opt_course[0]] = opt_course[1:]
		else:
			opt_credits_needed -= opt_course[1]
			if course[0][-3] == level[0]:
				needed_in_level -= opt_course[1]
	# order optional courses according to user preferences
	ranked_opt = [x[0] for x in rankedCoursesMultiple(optional.keys(), p1, p2, p3, taken)]
	ranked_opt = eliminateCrossListings(ranked_opt,Data.major_courses[major])
	opt_courses = []
	i = 0
	credits = 0
	level_credits = 0
	# From (sorted) list of optional courses, choose courses user should take
	while credits < opt_credits_needed or level_credits < needed_in_level:
		course = ranked_opt[i]
		add_course = True
		this_credit = optional[course][0]
		# Ensure courses returned will not have unfulfilled prerequisites
		for prereq in optional[course][1]:
			# The last part allows us to take a course if the prereq will be added later (i.e. it is in the set of courses in opt_ranked we know we will add)
			if not prereq in taken and not prereq in required.keys() and not prereq in ranked_opt[i:int(i+opt_credits_needed-credits-this_credit)]:
				add_course = False
				break
		#Ensure courses returned will not have unfulfilled corequisites
		if add_course:
			for coreq in optional[course][1]:
				if not coreq in taken and not coreq in required.keys() and not coreq in ranked_opt[i:int(i+opt_credits_needed-credits-this_credit)]:
					add_course = False
					break
		if add_course:
			opt_courses.append(course)
			credits += this_credit
			if int(course[-3]) >= int(level[0]):
				level_credits += this_credit
		i += 1
		# Make sure the list of courses we return fulfills the requirement that so many courses are above a certain level
	 	if credits >= opt_credits_needed and needed_in_level > level_credits:
			i2 = i - 1
			# Do not take extra classes. Remove the lowest ranked class not above the needed level
			if int(opt_courses[i][-3]) < int(level[0]):
				worst_curr_class = opt_courses[i]
				opt_courses.remove(worst_curr_class)
				credits -= optional[worst_curr_class][0]
			else:
				i2 -= 1
	courses = required.keys() + opt_courses
	return courses

def printSchedule(l, taken, year):
	if (year <= 2014):
		return "graduated"
	sorted_courses = l
	num_per_semester = math.ceil(float(len(l)) / (2 * (year - 2014)))
	print num_per_semester
	# A list of lists (each list is courses for a particular semester)
	semester_schedules = []
	# Each semester
	for i in range((year-2014)*2):
		# Sort by course number. In general, students take lower numbered courses first
		sorted_courses = sorted(sorted_courses, key=lambda x: int(x[-3:]))
		credits = 0
		courses = []
		course_i = 0
		need_prereq = []
		# Fill each semester. Ensure an upper bound on courses taken per semester
		while credits < num_per_semester and course_i < len(sorted_courses):
			course = sorted_courses[course_i]
			print "semester " + str(i) + ": looking at " + course
			fulfills_prereq = True
			# Only add if prereqs are met, else hold until next semester
			for prereq in optionalRequiredUnknown(course, 1):
				if not prereq in taken:
					print prereq + " not in taken courses (" + course + ")"
					print taken
					fulfills_prereq = False
			if fulfillis_prereq:
				course_and_coreqs = [course]
				for coreq in optionalRequiredUnknown(course, 2):
					for prereq in optionalRequiredUnknown(coreq, 1):
						if not prereq in taken:
							fulfills_prereq = False
							break
					elif not coreq in taken and not coreq in courses:
						course_and_coreqs.append(coreq)
				if fulfills_prereq:
					for c in course_and_coreqs:
						courses.append(c)
						credits += optionalRequiredUnknown(course, 0)
						try:
							sorted_courses.remove(c)
						except:
							pass
			if not fulfills_prereq:
				need_prereq.append(course)
				sorted_courses.remove(course)
				continue
		taken.extend(courses)
		semester_schedules.append(courses)
		for course in need_prereq:
			sorted_courses.append(course)
	if sorted_courses:
		return "Not enough time"
	return semester_schedules

# Called on a course when it is unknown whether the course lies in the optional or required dictionary
def optionalRequiredUnknown(course, field):
	try: 
		x = required[course][field]
	except:
		x = optional[course][field]
	return x

