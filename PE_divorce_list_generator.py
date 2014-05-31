"""
List data this way in txt file to be converted into a divorce decree list:
• ex_hubby; ex_hubby_town; ex_wife; ex_wife_town; marriage_date
• Homer Simpson; Springfield, N.T.; Marge Simpson; Springfield, N.T.; Oct. 31, 1969

Output looks like this:
• Homer Simpson, Springfield, N.T., from Marge Simpson, Springfield, N.T.; married Oct. 31, 1969
"""

import re

f = ""
new_list = ""

# Opens source txt file and creates a new txt file.
def file_opener(file_name):
    global f, new_list
    f = open(file_name + ".txt", "r")
    new_list = open(file_name + "_list.txt", "w")

#  Makes list of divorce decrees inside new txt file.	
def list_maker(county_choice):
    global f, new_list
    data = f.readlines()
    cc = county_choice.upper()
    if cc == "C":
        new_list.write("COLUMBIA COUNTY DIVORCE DECREES" + "\n")
    elif cc == "M":
        new_list.write("MONTOUR COUNTY DIVORCE DECREES"  + "\n")
    for line in data:
        parts = line.split(";")
        new_list.write("• " + parts[0] + "," + parts[1] + ", from" + parts[2] + "," + parts[3] + "; married" + parts[4])
    new_list.write("\n")

# Closes source txt file and new txt file.
def file_close():
    f.close()
    new_list.close()

# Asks user for name of source txt file and for the county issuing the divorce decrees.
# Passes user's input into def list_maker.
def ask_user():
    print("Welcome to the Press Enterprise divorce-decree list generator.")
    original_list = input("Please enter name of txt file to convert into a list. Omit '.txt' extension.")
    county_choice = input("Which county issued these divorce decrees? Columbia or Montour? Please enter C or M.")
    file_opener(original_list)
    list_maker(county_choice)
    file_close()

ask_user()
