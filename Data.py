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

# Each major ordered according to: Major : {Required : [required courses], 
# Optional: [(total optional credits need, total needed beyond a certain level, level), 
# optional courses]}
# Class written as: (ID, credits, [prereqs], [coreqs])
major_courses = {"Bioengineering" : { "Required" : [("MATH104", 1, [], []), 
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
    ("BE496", 1, [], [])], 

    "Optional" : [(5, 2, "400"), ("BE099", 1, [], []), 
    ("BE225", 1, ["PHYS140"], []), ("BE303", 1, [], []), ("BE330", 1, ["CHEM102"], []), 
    ("BE400", 1, [], []), ("BE540", 1, [], []), ("BE441", 1, ["BIOL121"], []), 
    ("BE555", 1, [], []), ("BE445", 1, [], []), ("BE455", 1, ["MATH241"], []), 
    ("BE470", 1, [], []), ("BE480", 1, ["BE301"], []), ("BE583", 1, ["BE305"], []), 
    ("BE486", 1, ["BE301"], []), ("BE490", 1, [], [])]},


    "Chemical and Biomolecular Engineering" : { "Required" : 
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
    ("CBE459", 1, ["CBE400"], []), ("CBE460", 1, ["CBE353"], [])],

    "Optional" : [(2, 0, "000"), ("CBE099", 1, [], []),
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
    ("CBE582", 1, [], [])]},


    "Computer Engineering" : {"Required" :
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
    ("CIS400", 1, [], []), ("CIS401", 1, ["CIS400"], [])],

    "Optional" : [(0, 0, "000")]},

    "Computer Science" : {"Required" :
    [("MATH104", 1, [], []), ("MATH114", 1, ["MATH104"], []),
    ("CIS160", 1, [], []), ("CIS261", 1, ["CIS160"], []),
    ("PHYS140", 1, [], ["MATH104"]), 
    ("PHYS141", 1, ["PHYS140"], ["MATH114"]),
    ("CIS110", 1, [], []), ("CIS120", 1, [], []), 
    ("CIS121", 1, ["CIS120", "CIS160"], []),
    ("CIS240", 1, [], []), ("CIS262", 1, ["CIS160"], []),
    ("CIS320", 1, ["CIS120", "CIS121", "CIS160", "CIS262"], []),
    ("ESE350", 1, [], []), ("CIS371", 1, ["CIS240"], []),
    ("CIS380", 1, ["CIS240"], []),
    ("CIS400", 1, [], []), ("CIS401", 1, ["CIS400"], [])],

    "Optional" : [(0, 0, "000")]},
    
    "Digital Media Design" : {"Required" :
    [("MATH104", 1, [], []), ("MATH114", 1, ["MATH104"], []),
    ("CIS160", 1, [], []), ("CIS262", 1, ["CIS160"], []),
    ("EAS205", 1, ["MATH114"], []), ("PHYS140", 1, [], ["MATH104"]), 
    ("PHYS141", 1, ["PHYS140"], ["MATH114"]), ("CHEM101", 1, [], ["CHEM053"]), 
    ("CHEM053", .5, [], ["CHEM101"]), ("BIOL101", 1.5, [], []),
    ("CIS110", 1, [], []), ("CIS120", 1, [], []), 
    ("CIS121", 1, ["CIS120", "CIS160"], []),
    ("CIS240", 1, [], []), ("CIS277", 1, ["CIS120"], []),
    ("CIS320", 1, ["CIS120", "CIS121", "CIS160", "CIS262"], []),
    ("CIS460", 1, [], []), ("CIS455", 1, [], []),
    ("CIS497", 1, [], []), ("FNAR123", 1, [], []),
    ("FNAR235", 1, [], [])],

    "Optional" : [(3, 2, "300"),
    ("CIS099", 1, [], []), ("CIS101", 1, [], []),
    ("CIS106",1, [], []), ("CIS112", 1, [], []),
    ("CIS125", 1, [], []), ("CIS140", 1, [], []),
    ("CIS190", .5, ["CIS240"], []), ("CIS191", .5, ["CIS110"], []),
    ("CIS192", .5, ["CIS120"], []), ("CIS193", .5, ["CIS110"], []),
    ("CIS194", .5, [], []), ("CIS195", .5, [], []), ("CIS196", .5, [], []),
    ("CIS261", 1, ["CIS160"], []), ("CIS330", 1, ["CIS121", "CIS160"], []),
    ("CIS334", 1, ["CIS320"], []), ("CIS341", 1, ["CIS121", "CIS240"], []),
    ("CIS350", 1, ["CIS240"], []), 
    ("CIS368", 1, ["CIS121", "CIS277"], []),
    ("CIS371", 1, ["CIS240"], []),
    ("CIS380", 1, ["CIS240"], []),
    ("CIS390", 1, ["MATH240", "PHYS150"]),
    ("CIS391", 1, ["CIS121", "CIS262"], []),
    ("CIS398", 1, ["CIS260", "CIS262", "MATH240"], []),
    ("CIS400", 1, [], []), ("CIS401", 1, ["CIS400"], []),
    ("CIS430", 1, ["CIS121"], []), ("CIS441", 1, ["CIS240"], []),
    ("CIS462", 1, [], []), ("CIS477", 1, ["PHIL006"], []),
    ("CIS553", 1, ["CIS121"], []), ("CIS534", 1, ["CIS371"], []),
    ("CIS563", 1, [])]},

    "ELectrical Engineering" : {"Required" :
    [("MATH104", 1, [], []), ("MATH114", 1, ["MATH104"], []),
    ("MATH240", 1, ["MATH114", "MATH104"], []),
    ("ESE301", 1, ["MATH114"], []),
    ("PHYS150", 1.5, [], ["MATH104"]), 
    ("PHYS151", 1.5, ["PHYS150"], ["MATH114"]),
    ("BIOL101", 1.5, [], []), ("CHEM053", 1, [], []),
    ("CIS110", 1, [], []), ("ESE111", 1, [], []),
    ("ESE215", 1, ["PHYS151"], ["MATH240"]),
    ("ESE218", 1, ["ESE215"], []), ("ESE224", 1, [], []),
    ("CIS120", 1, ["CIS110"], []), ("ESE450", 1, [], []),
    ("ESE451", 1, ["ESE450"], [])],

    "Optional" : [(4, 0, "000"),
    ("ESE319", 1, ["ESE216"], []), ("ESE350", 1, [], []),
    ("ESE370", 1, ["ESE170", "ESE215"], []),
    ("ESE419", 1, ["ESE319"], []), ("ESE570", 1, ["ESE319"], []),
    ("ESE578", 1, ["ESE572"], ["ESE570"]), 
    ("ESE310", 1, ["PHYS151", "MATH240"], []),
    ("ESE460", 1, ["ESE218"], []),
    ("ESE521", 1, ["ESE218"], []), ("ESE525", 1, ["ESE218"], []),
    ("ESE529", 1, [], []), ("ESE303", 1, ["ESE301"], []),
    ("ESE313", 1, ["ESE116", "MATH240"], []), ("ESE325", 1, ["MATH240"], []),
    ("ESE406", 1, [], []),
    ("ESE500", 1, [], []), ("ESE504", 1, ["MATH312"], []),
    ("ESE531", 1, [], []),
    ("ESE539", 1, [], []), ("ESE590", 1, [], [])]},

    "Materials Science and Engineering" : {"Required" :
    [("MATH104", 1, [], []), ("MATH114", 1, ["MATH104"], []),
    ("CHEM101", 1, [], ["CHEM053"]), 
    ("CHEM053", .5, [], ["CHEM101"]), 
    ("CHEM102", 1, ["CHEM101"], ["CHEM054"]), 
    ("CHEM054", .5, [], ["CHEM102"]),
    ("PHYS140", 1, [], ["MATH104"]), 
    ("PHYS141", 1, ["PHYS140"], ["MATH114"]),
    ("MATH240", 1, ["MATH114", "MATH104"], []),
    ("MATH241", 1, ["MATH240", "MATH114", "MATH104"], []),
    ("EAS101", 1, [], []), ("EAS203", 1, [], []),
    ("ENGR105", 1, [], []), ("MSE220", 1, [], []),
    ("MSE221", 1, ["PHYS140", "PHYS141"], ["MATH240"]), 
    ("MSE215", 1, ["MSE221"], []),
    ("MSE250", 1, ["MSE220"], []), ("MSE260", 1, ["CHEM101"], []),
    ("MSE330", 1, ["CHEM102", "MSE220"], []), ("MSE360", 1, [], []),
    ("MSE393", 1, ["MSE220"], []), ("ESE301", 1, ["MATH114"], []),
    ("CHEM241", 1, ["CHEM102"], []), ("EAS303", 1, [], []),
    ("MSE405", 1, [], []), ("MSE495", 1, [], []),
    ("MSE440", 1, [], []), ("MSE496", 1, [], []),
    ("MSE561", 1, [], [])],

    "Optional" : [(1, 0, "000"),
    ("MSE465", 1, [], []), ("MSE545", 1, [], [])]},


    "MEAM" : {"Required" :
    [("MEAM110", 1.5, [], []), ("MATH104", 1, [], []),
    ("CHEM101", 1, [], ["CHEM053"]), 
    ("CHEM053", .5, [], ["CHEM101"]),
    ("PHYS151", 1.5, ["MEAM110"], ["MATH114"]),
    ("ENGR105", 1, [], []), ("MEAM210", 1, ["MEAM110"], ["MEAM247"]),
    ("MEAM247", 1, [], ["MEAM210"]), 
    ("MATH240", 1, ["MATH104", "MATH114"], []),
    ("MEAM203", 1, ["MATH104", "MATH114"], []), 
    ("MEAM211", 1, ["MEAM210"], []), 
    ("MEAM248", 1, [], ["MEAM203", "MEAM211"]),
    ("MATH241", 1, ["MATH240"], []),
    ("MEAM302", 1, ["MATH241", "MEAM211"], []), 
    ("MEAM321", 1, ["MATH241", "MEAM211"], []), 
    ("MEAM347", 1, [], []), ("MEAM333", 1, ["MEAM203", "MEAN302"], []), 
    ("MEAM354", 1, ["MEAM210"], []), ("MEAM348", 1, [], []), 
    ("MEAM445", 1, [], []), ("MEAM446", 1, [], [])],

    "Optional" : [(3, 3, "400"),
    ("MEAM410", 1, [], []), ("MEAM415", 1, [], []), 
    ("MEAM454", 1, ["MEAM210", "MATH240", "MATH241"], []), 
    ("MEAM455", 1, [], []), 
    ("MEAM502", 1, ["MEAM203", "MEAM333"], []), ("MEAM504", 1, [], []), 
    ("MEAM505", 1, [], []), ("MEAM510", 1, [], []), 
    ("MEAM513", 1, ["MEAM321"], []), 
    ("MEAM514", 1, ["MEAM101", "MEAM210"], []), 
    ("MEAM516", 1, [], []), ("MEAM519", 1, [], []), 
    ("MEAM520", 1, ["MEAM211", "MATH240"], []), ("MEAM521", 1, [], []), 
    ("MEAM522", 1, [], []), ("MEAM527", 1, ["MATH241", "PHYS151"], []), 
    ("MEAM528", 1, ["MATH114"], []), ("MEAM529", 1, [], []), 
    ("MEAM530", 1, [], []), ("MEAM535", 1, [], []), 
    ("MEAM536", 1, [], []), ("MEAM537", 1, ["PHYS151"], []), 
    ("MEAM540", 1, ["MATH240"], []), ("MEAM544", 1, ["MATH312"], []), 
    ("MEAM545", 1, ["MEAM302"], []), ("MEAM550", 1, ["MEAM354"], []), 
    ("MEAM553", 1, [], []), 
    ("MEAM554", 1, ["MEAM210", "MEAM354", "MATH240", "MATH241"], []), 
    ("MEAM555", 1, ["MEAM203"], []), ("MEAM561", 1, ["MEAM203"], []), 
    ("MEAM564", 1, ["MEAM333"], []), ("MEAM570", 1, [], []), 
    ("MEAM571", 1, ["MEAM570"], []), ("MEAM572", 1, ["MEAM203"], []),
    ("MEAM575", 1, [], [])]},

    "Networked and Social Systems Engineering" : {"Required" :
    [("MATH104", 1, [], []), ("MATH114", 1, ["MATH104"], []),
    ("MATH240", 1, ["MATH104", "MATH114"], []),
    ("EAS205", 1, ["MATH114"], []), ("CIS160", 1, [], []),
    ("ESE301", 1, ["MATH114"], []), ("PHYS150", 1.5, [], ["MATH104"]), 
    ("PHYS151", 1.5, ["PHYS150"], ["MATH114"]),
    ("CIS110", 1, [], []), ("CIS120", 1, [], []), 
    ("CIS121", 1, ["CIS120", "CIS160"], []),
    ("CIS320", 1, ["CIS120", "CIS121", "CIS160", "CIS262"], []),
    ("ESE210", 1, ["MATH240"], []),
    ("ESE303", 1, ["ESE301"], []), ("ESE304", 1, ["MATH240"], []),
    ("NETS112", 1, [], []), ("NETS150", 1, [], []),
    ("NETS212", 1, ["NETS112"], []), ("NETS312", 1, ["NETS212"], []),
    ("NETS412", 1, ["NETS312"], []),
    ("CIS400", 1, [], []), ("CIS401", 1, ["CIS400"], []),
    ("ECON101", 1, [], []), 
    ("ECON212", 1, ["ECON101", "MATH104", "MATH114"], [])],

    "Optional" : [(3, 0, "000"),
    ("CIS330", 1, ["CIS121", "CIS160"], []), 
    ("CIS334", 1, ["CIS320"], []), 
    ("CIS368", 1, ["CIS121", "CIS277"], []), ("CIS430", 1, ["CIS121"], []), 
    ("CIS455", 1, [], []), ("CIS520", 1, ["MATH312"], []), 
    ("CIS551", 1, ["TCOM512"], []), ("CIS553", 1, ["CIS121"], [])]}

    }


