import smtplib
from email.mime.text import MIMEText


def makeStudent(email, name, surname, points, grade="", status=""):
    student = {"email": email, "name": name, "surname": surname, "points": points, "grade": grade, "status": status}
    return student


def createStudent(list_of_students, emailmake, namemake, surnamemake, pointsmake, grade="", status=""):
    for i in range(0,len(list_of_students)):
        if emailmake in list_of_students[i].values():
            print("Ten email juz znajduje sie w bazie!", emailmake)
            return
    list_of_students.append(makeStudent(emailmake, namemake, surnamemake, pointsmake, grade, status))


def deleteStudent(list_of_students, emaildelete):
    for i in range(0, len(list_of_students)):
        if emaildelete in list_of_students[i].values():
            list_of_students.pop(i)
            return
    print("Nie ma takiego email w bazie!", emaildelete)


def gradeStudent(studentArg):
    if studentArg.get("status", "") == "GRADED" or studentArg.get("status", "") == "MAILED":
        print("Student ma juz ocene! ", studentArg)
        return studentArg

    if studentArg.get("points", "") == "":
        print("Student nie ma wpisanych punktów! ", studentArg)
        return studentArg

    points = studentArg.get("points")
    try:
        a = int(points)
    except ValueError:
        print("Punkty sa w nieprawidlowym formacie! ", studentArg)
        return studentArg

    if int(points) < 50:
        studentArg.update({"grade": "2"})
    else:
        if 60 >= int(points) >= 51:
            studentArg.update({"grade": "3"})
        else:
            if 70 >= int(points) >= 61:
                studentArg.update({"grade": "3.5"})
            else:
                if 80 >= int(points) >= 71:
                    studentArg.update({"grade": "4"})
                else:
                    if 90 >= int(points) >= 81:
                        studentArg.update({"grade": "4.5"})
                    else:
                        studentArg.update({"grade": "5"})
    studentArg.update({"status": "GRADED"})
    return studentArg


def writeListtoFile(list_of_students, pathOut):
    with open(pathOut, "w") as file_object:
        for student in list_of_students:
            lineToWrite = student["email"] + "," + student["name"] + "," + student["surname"] + "," + student["points"]
            if student["grade"] != "":
                lineToWrite += ","
                lineToWrite += student["grade"]
            if student["status"] != "":
                lineToWrite += ","
                lineToWrite += student["status"]
            file_object.write(lineToWrite+"\n")


def emailStudents(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


# Zad1 the program
studentList = []
filepath = "students0.txt"

with open(filepath) as file_object:
    for line in file_object:
        x = line.rstrip().split(",")

        if len(x) == 4:
            studentList.append(makeStudent(x[0], x[1], x[2], x[3]))
        else:
            if len(x) == 5:
                studentList.append(makeStudent(x[0], x[1], x[2], x[3], x[4]))
            else:
                if len(x) == 6:
                    studentList.append(makeStudent(x[0], x[1], x[2], x[3], x[4], x[5]))
                else:
                    print("Niepoprawny obiekt! ", x)

for studenttmp in studentList:
    print(studenttmp)

print("Co chcesz zrobic z danymi studentow?")
while True:
    print("Wybierz |grade| aby wpisac oceny, |email| aby wyslac mail do studentow z statusem Graded, "
          "|make| aby dodac studenta, |delete| aby usunac, lub |end| zeby wyjsc")
    command = input("Wpisz komende")

    if command == "grade":

        print("Ok, ocenianie studentow w toku")
        for studenttmp in studentList:
            gradeStudent(studenttmp)

        writeListtoFile(studentList, filepath)
    else:
        if command == "email":
            print("Ok, mailowanie studentow w toku")

            for studenttmp in studentList:
                if studenttmp["status"] == "GRADED":
                    emailtemp = studenttmp["email"]
                    gradetemp = studenttmp["grade"]
                    emailStudents("Ocena", f"Twoja ocena z przedmiotu PPY to {gradetemp}",
                                  "dummy@gmail.com", emailtemp, "temppass")
                    studenttmp["status"] = "MAILED"

            writeListtoFile(studentList, filepath)
        else:
            if command == "make":
                email = input("Wpisz email")
                name = input("Wpisz imie")
                surname = input("Wpisz nazwisko")
                points = input("Wpisz punkty")

                createStudent(studentList, email, name, surname, points)
                writeListtoFile(studentList, filepath)
            else:
                if command == "delete":
                    email = input("Wpisz mail studenta do usunieca")
                    deleteStudent(studentList, email)
                    writeListtoFile(studentList, filepath)

                else:
                    if command == "end":
                        print("Ok, koncze program")
                        break

                    else:
                        print("Niepoprawna komenda!")

    for studenttmp in studentList:
        print(studenttmp)
