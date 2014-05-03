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
	e = r'([A-Z]{2,4}).*?([0-9]{3}),'
	for match in re.finditer(e,s):
		ans.append((match.group(1),match.group(2)))
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
		if not Data.attrs[key(p1)][1]:
			avgRating1 = 4 - avgRating1
		if not Data.attrs[key(p1)][1]:
			avgRating2 = 4 - avgRating2
		if not Data.attrs[key(p1)][1]:
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
	for dept in l:
		revinfo = requests.get('http://api.penncoursereview.com/v1/depts/' + dept + '/reviews?token=' + api_key).json()['result']['values']
		s.extend(rankedCourses(revinfo,p1,p2,p3))
	s.sort(key=lambda x:x[1][0], reverse=True)
	for course in taken:
		try:
			s.remove(course)
		except:
			continue
	#print s
	return s

def printSchedule(l, year):
	if (year <= 2014):
		html += "You've graduated. You have no more semesters to take classes."
	sorted_classes = sorted(l, key=lambda x: int(x[-3:]))
	num_per_semester = len(l) / (2 * (year - 2014))
	for i in range(year*2):
		html += "<br> Semester" + str(i) + "</br>"
		for j in range(num_per_semester):
			html += "<br>" + sorted_classes[i * num_per_semester + j] + "</br>"
	






