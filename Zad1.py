def makeStudent(email, name, surname, points, grade="", status=""):
    student = {"email": email, "name": name, "surname": surname, "points": points, "grade": grade, "status": status}
    return student


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
            line = student["email"]+","+student["name"]+","+student["surname"]+","+student["points"]
            if student["grade"] != "":
                line += student["grade"]
                line += ","
                line += student[""]


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

for studenttmp in studentList:
    gradeStudent(studenttmp)
