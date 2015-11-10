# Divorce Decree Generator
_By Gary Pang, "CodeWritingCow"_


## What It Does
This Python program produces a txt file of new divorce decrees for newspaper publication. I'm a reporter, and I wrote this program back in 2014 to make my job easier.


## How It Works
It opens a txt file (ex. divorces_2014-05-01.txt) with information like this:

* Homer Simpson; Springfield, N.T.; Marge Simpson; Springfield, N.T.; Dec. 26, 1991

And makes a new txt file (divorces_2014-05-01_list.txt) like this:
* Homer Simpson, Springfield, N.T., from Marge Simpson, Springfield, N.T.; married Dec. 26, 1991

(When the program starts, it asks user to type a txt file's name. In this example, type divorces_2014-05-01".)


## Requirements
Someone must visit the local courthouse, read each new divorce decree, and write a txt with the following info:

ex_hubby; ex_hubby_town; ex_wife; ex_wife_town; marriage_date
ex_hubby; ex_hubby_town; ex_wife; ex_wife_town; marriage_date

Each field must be separated by a semicolon. Each new decree must be in one paragraph (see example above.) Avoid extra breaks before and after each decree (watch that "enter" key!) Otherwise, you'll get an error message.