# Boolean refers to whether it's a ositive attribute
attrs = {"Course Quality": (r'CourseQuality', True), 
    "Instructor Quality": (r'InstructorQuality', True), 
    "Difficulty": (r'Difficulty', False), 
    "Amount Learned": (r'AmountLearned', True), 
    "Work Required": (r'WorkRequired', False)}

majors = ["Bioengineering", "CBE", "Computer Engineering", "Computer Science",
     "Digital Media Design", "Electrical Engineering", 
     "Materials Science and Engineering", "MEAM", 
     "Networked & Social Systems Engineering", 
     "Systems Science and Engineering"] 

# Each major ordered according to: {Major : [{Required : [required courses]}, {Optional: [(total optional credits need, total needed beyond a certain level, level), optional courses]}]}
# Class written as: (ID, credits, [prereqs], [coreqs])
major_courses = {"Bioengineering" : [{ "Required" : [("Math104", 1, [], []), 
    ("MATH114", 1, ["MATH104"], []), ("MATH240", 1, ["MATH114", "MATH104"], []), 
    ("MATH241", 1, ["MATH240", "MATH114", "MATH104"], []), ("ENM321", 1, [], []), 
    ("BIOL121", 1, ["CHEM101"], ["BIOL123"]), ("BIOL123", .5, [], ["BIOL121"]), 
    ("BIOL202", 1, ["BIOL121"], []), ("CHEM101", 1, [], ["CHEM053"]), 
    ("CHEM053", .5, [], ["CHEM101"]), ("CHEM102", 1, ["CHEM101"], ["CHEM054"]), 
    ("CHEM054", .5, [], ["CHEM102"]), ("PHYS140", 1, [], ["MATH104"]), 
    ("PHYS141", 1, ["PHYS140"], ["MATH114"]), ("BE100", .5, [], ["MATH104", "PHYS140"]), 
    ("BE101", .5, [], []), ("ENGR105", 1, [], []), 
    ("BE200", 1, ["MATH104", "MATH114", "PHYS140"], ["MATH240"]), 
    ("BE220", 1, ["BE200", "CHEM101", "CHEM102"], []), 
    ("BE301", 1, ["MATH241"], []), ("BE305", 1, ["MATH241"], []), 
    ("BE309", 1, [], ["BE301","BE324"]), ("BE310", 1, [], ["BE350"]), 
    ("BE324", 1, ["PHYS140", "PHYS141", "MATH240", "CHEM101", "CHEM102"], []), 
    ("BE350", 1, ["MATH241", "PHYS140"], []), ("BE495", 1, [], []), 
    ("BE496", 1, [], [])]}, 

    {"Optional" : [(5, 2, 400), ("BE099", 1, [], []), 
    ("BE225", 1, ["PHYS140"], []), ("BE303", 1, [], []), ("BE330", 1, ["CHEM102"], []), 
    ("BE400", 1, [], []), ("BE540", 1, [], []), ("BE441", 1, ["BIOL121"], []), 
    ("BE555", 1, [], []), ("BE445", 1, [], []), ("BE455", 1, ["MATH241"], []), 
    ("BE470", 1, [], []), ("BE480", 1, ["BE301"], []), ("BE583", 1, ["BE305"], []), 
    ("BE486", 1, ["BE301"], []), ("BE490", 1, [], [])]}]}