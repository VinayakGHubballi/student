import sys

def display_student_details(name, college, usn, city):
    print("----- Student Details -----")
    print("Name   :", name)
    print("College:", college)
    print("USN    :", usn)
    print("City   :", city)
    print("---------------------------")


name = sys.argv[1]
college = sys.argv[2]
usn = sys.argv[3]
city = sys.argv[4]

display_student_details(name, college, usn, city)
