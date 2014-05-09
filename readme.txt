PennCourseHelper incorporates many topics that we learned over the course of
the semester, including api's (specifically, PCH uses the penncoursereview
api), flask, regular expressions, modules, json, posting methods, and heroku
(as well as classic favorites such as if/else statements).

The two modules we implemented were helping students plan a schedule
based on their major, preferences, and coruse history, and helping
students choose a course from a department given similar parameters.

The runtime isn't exactly ideal. This is mostly due to the fact that our post
requests, though optimized in number, need a lot of information from PCH. If
this were to be used on a full-scale production scale, we would probably
incorporate threads (or even another language) for better speed.