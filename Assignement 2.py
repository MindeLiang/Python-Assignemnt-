dict = {}


def add_student_information():
    student_name = input("please enter student name: ")
    student_grade = input("please add student grades: ")
    dict[student_name] = student_grade
    return dict


def search_student_information():
    search_name = input("please enter the name you want to search: ")
    for student_name, student_grade in dict.items():
        if search_name == student_name:
            print("The grade of " + student_name + " is " + student_grade)
        else:
            print("we do not have this student")


def delete_student_information():
    remove_name = input("please enter the name you want to remove: ")
    dict.pop(remove_name, None)


def update_student_information():
    update_student_name = input("please enter student name you want to update: ")
    update_student_grade = input("please add student grades you want to update: ")
    dict[update_student_name] = update_student_grade
    print("")


while True:
    command = input("Which operation do you want to do?\n"
                    "Add student information Enter 1 \n Search "
                    "student information Enter 2\n Delete"
                    "student information Enter 3 \n"
                    "Update student information Enter 4 \n "
                    "Quit Command Enter 5: ")
    if command == "1":
        add_student_information()
    elif command == "2":
        search_student_information()
    elif command == "3":
        delete_student_information()
    elif command == "4":
        update_student_information()
    elif command == "5":
        break
print(dict)

