#Diego Aguilera
#The app will allow you to enter a students information to figure out to see if their gpa is enough to be in Honor Roll or the deans list
while():
       
        lastname = input("Enter last name of student: ")

        if lastname == "zzz":

            print("Student processing records quit.")
            break

        firstname = input("Enter first name of student: ")

        while True:
            gpa = input("Enter GPA of Student: ")

            gpa_value = float(gpa)

            if gpa_value >= 3.5:
                print(firstname + " " + lastname + " made the Dean's List")

            elif gpa_value < 3.5 and gpa_value >= 3.25:
                print(firstname + " " + lastname + " made the Honor Roll")

            else:
                print("Keep studying, " + firstname + " " + lastname + "!")
            break