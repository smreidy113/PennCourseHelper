attrs = {"Course Quality": r'CourseQuality', "Instructor Quality": r'InstructorQuality', "Difficulty": r'Difficulty', "Communication Ability": r'CommAbility', "Amount Learned": r'AmountLearned', "Work Required": r'WorkRequired'}
majors = ["Bioengineering", "CBE", "Computer Engineering", "Computer Science", "Digital Media Design", "Electrical Engineering", "Materials Science and Engineering", "MEAM", "Networked & Social Systems Engineering", "Systems Science and Engineering"] 
minors = [x for x in majors]

major_courses = {"Bioengineering" : [{ "Required" : [("Math104", 1, 0), ("MATH114", 1, 1), ("MATH240", 1, 2), ("MATH241", 1, 3), ("ENM321", 1, 0), ] ]}