import re

def courseList(s):
	s = s + ","
	ans = []
	e = r'([A-Z]{2,4}).*?([0-9]{3}),'
	for match in re.finditer(e,s):
		ans.append((match.group(1),match.group(2)))
	return ans