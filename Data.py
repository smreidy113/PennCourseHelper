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

# Each major ordered according to: {Major : [{Required : [required courses]}, 
# {Optional: [(total optional credits need, total needed beyond a certain level, level), 
# optional courses]}]}
# Class written as: (ID, credits, [prereqs], [coreqs])
major_courses = {"Bioengineering" : [{ "Required" : [("MATH104", 1, [], []), 
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

    {"Optional" : [(5, 2, "400"), ("BE099", 1, [], []), 
    ("BE225", 1, ["PHYS140"], []), ("BE303", 1, [], []), ("BE330", 1, ["CHEM102"], []), 
    ("BE400", 1, [], []), ("BE540", 1, [], []), ("BE441", 1, ["BIOL121"], []), 
    ("BE555", 1, [], []), ("BE445", 1, [], []), ("BE455", 1, ["MATH241"], []), 
    ("BE470", 1, [], []), ("BE480", 1, ["BE301"], []), ("BE583", 1, ["BE305"], []), 
    ("BE486", 1, ["BE301"], []), ("BE490", 1, [], [])]}],


    "Chemical and Biomolecular Engineering" : [{ "Required" : 
    [("MATH104", 1, [], []), ("CHEM101", 1, [], ["CHEM053"]), 
    ("CHEM053", .5, [], ["CHEM101"]), ("CBE150", 1, [], []), 
    ("PHYS140", 1, [], ["MATH104"]), ("CBE160", 1, [], []),
    ("MATH114", 1, ["MATH104"], []), 
    ("CHEM102", 1, ["CHEM101"], ["CHEM054"]), 
    ("CHEM054", .5, [], ["CHEM102"]), ("PHYS141", 1, ["PHYS140"], ["MATH114"]),
    ("CBE230", 1, ["CBE160"], []), ("MATH240", 1, ["MATH114", "MATH104"], []),
    ("CHEM241", 1, ["CHEM102"], []), ("CBE231", 1, ["CBE160", "CBE230"], []),
    ("CHEM242", 1, ["CHEM241"], []), ("EAS105", 1, [], []),
    ("CBE350", 1, ["CBE231"], []), ("CBE353", 1, ["CBE231"], []),
    ("MSE221", 1, ["MATH240"], ["PHYS140", "PHYS141"]),
    ("CBE351", 1, ["CBE350"], []), ("CBE371", 1, ["CBE231"], []),
    ("CBE480", 1, [], []), ("CBE400", 1, ["CBE371"], []),
    ("CBE410", 1, ["CBE351", "CBE371"], []),
    ("CBE451", 1, ["CBE231", "CBE351"], []), 
    ("CBE459", 1, ["CBE400"], []), ("CBE460", 1, ["CBE353"], [])]},

    {"Optional" : [(2, 0, "000"), ("CBE099", 1, [], []),
    ("CBE111", 1, [], []), ("CBE375", 1, [], []),
    ("CBE510", 1, ["CBE231"], []), ("CBE479", 1, [], []),
    ("CBE508", 1, [], []), ("CBE511", 1, [], []),
    ("CBE525", 1, ["CBE231"], []), ("CBE535", 1, [], []),
    ("CBE540", 1, [], []), ("CBE543", 1, [], []),
    ("CBE545", 1, ["CBE231", "CHEM102"], []),
    ("CBE546", 1, [], []), ("CBE552", 1, [], []),
    ("CBE554", 1, [], []), ("CBE555", 1, [], []),
    ("CBE557", 1, [], []), ("CBE562", 1, [], []),
    ("CBE563", 1, [], []), ("CBE564", 1, [], []),
    ("CBE582", 1, [], [])]}],


    "Computer Engineering" : [{"Required" :
    [("MATH104", 1, [], []), ("MATH114", 1, ["MATH104"], []), 
    ("MATH240", 1, ["MATH114", "MATH104"], []), ("CIS261", 1, ["CIS160"], []),
    ("CIS160", 1, [], []), ("PHYS150", 1.5, [], ["MATH104"]), 
    ("PHYS151", 1.5, ["PHYS150"], ["MATH114"]), 
    ("BIOL101", 1, [], []), ("CIS120", 1, [], []), 
    ("CIS121", 1, ["CIS120", "CIS160"], []), ("ESE170", 1, [], []),
    ("ESE215", 1, ["PHYS151"], []), ("CIS240", 1, [], []),
    ("ESE250", 1, ["CIS120"], []), ("ESE350", 1, [], []),
    ("ESE370", 1, ["ESE170", "ESE215"], []),
    ("CIS350", 1, ["CIS240"], []), ("CIS371", 1, ["CIS240"], []),
    ("CIS380", 1, ["CIS240"], []), ("CIS441", 1, ["CIS240"], []),
    ("CIS553", 1, ["CIS121"], []), ("CIS534", 1, ["CIS371"], []),
    ("CIS400", 1, [], []), ("CIS401", 1, ["CIS400"], [])]},

    {"Optional" : [(0, 0, "000")]}]}

