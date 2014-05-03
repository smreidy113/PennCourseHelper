import re
import json
import requests
from requests.adapters import HTTPAdapter
import random

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

def rankedCourses(revinfo,p1,p2,p3, num_needed):
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
			if (Data.attrs[p1][1]):
				sumRating1 += float(section['ratings'].get(str('r'+p1),0.0))
			else:
				sumRating1 += float(4 - section['ratings'].get(str('r'+p1),0.0))
			if (Data.attrs[p2][1]):
				sumRating2 += float(section['ratings'].get(str('r'+p2),0.0))
			else:
				sumRating2 += float(4 - section['ratings'].get(str('r'+p2),0.0))
			if (Data.attrs[p3][1]):
				sumRating3 += float(section['ratings'].get(str('r'+p3),0.0))
			else:
				sumRating3 += float(4 - section['ratings'].get(str('r'+p3),0.0))
		avgRating1 = sumRating1/len(courseDict[course])
		avgRating2 = sumRating2/len(courseDict[course])
		avgRating3 = sumRating3/len(courseDict[course])
		ratingsDict[course] = (3*avgRating1**2 + 2*avgRating2**2 + 1*avgRating3**2) / 96 * 10
	#print ratingsDict.items()
	s = ratingsDict.items()
	s.sort(key=lambda x:x[1])
	return s

def getSubset(s):
	# return subset
	if num_needed < len(s):
		return [x[0] for x in s]
	else:
		l = []
		for _ in range(num_needed):
			i = random.randint(0, num_needed)
			l.append(s[i][0])
			s.remove(s[i])
		return l

def rankedCoursesMultiple(l,p1,p2,p3):
	s = []
	for dept in l:
		revinfo = requests.get('http://api.penncoursereview.com/v1/depts/' + dept + '/reviews?token=' + api_key).json()['result']['values']
		s.extend(rankedCourses(revinfo,p1,p2,p3))
	s.sort(key=lambda x:x[1])
	print s
	return s
def schedule(sectors, optional_major_courses, required):
	l = []
	l += required
	sorted_sectors = [] 
	for x in sectors:
		sorted_sectors.append(sorted(x, key=lambda x: x[1]))
	sorted_optional_major_courses = sorted(optional_major_courses, key=lambda x: x[1])






