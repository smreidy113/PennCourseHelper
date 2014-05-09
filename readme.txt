Sean Reidy and Steven Jaffe

PennCourseHelper incorporates many topics that we learned over the course of
the semester, including api's (specifically, PCH uses the penncoursereview
api), flask, regular expressions, modules, json, posting methods, and heroku
(as well as classic favorites such as if/else statements).

The two modules we implemented were helping students plan a schedule
based on their major, preferences, and coruse history, and helping
students choose a course from a department given similar parameters.

To use schedule, you should input a year, major (choose from the drop-
down list) and enter any classes you've taken (each course should
be of the format DEPTNUM e.g. HIST027 or CIS110, no dash, all uppcase,
no space..., and each course should be separated by a comma e.g. 
HIST027, CIS110), as well as preferences (at least one, each from drop-
downs) for courses. To use decide on a course, you should do the same thing
except you'll choose department from a scrollable list (you can choose more
than one by holding down command for macs or control for windows) instead
of a major.

The runtime isn't exactly ideal. This is mostly due to the fact that our post
requests, though optimized in number, need a lot of information from PCH. If
this were to be used on a full-scale production scale, we would probably
incorporate threads (or even another language) for better speed.

The version we're submitting can be run locally, but can also be used
online (using heroku) by going to secret-wave-9704.herokuapp.com

Most of the methods we actually use are in Methods.py. The information we
need for courses (e.g. co/prerequeisites) we had to create our own
datastructures to store, and can be found in Data.py. The code for
laying out the pages for create schedule and decide on a course, as
well as the main code for those methods are in main.py (they call
methods in Methods.py).

