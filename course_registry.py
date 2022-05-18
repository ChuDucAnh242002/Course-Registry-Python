"""
COMP.CS.100 The first Python program.
Creator: Chu Duc Anh < anh.chu@tuni.fi>
Student id number: 050358922
"""
def read_file():
    """
    Try to read the file and put it into dictionary
    :return: dictionary, dictionary in dictionary of information in file name
    """
    file_name = input("Enter file name: ")
    file_name = file_name.strip()
    # read the file name
    try:
        file_name = open(file_name, mode ="r")
        data = {}
        fact_key = []
        #split the line one by one and put it in dictionary
        for line in file_name:
            line = line.rstrip()
            parts = line.split(";")
            #Call key and value and create a small dictionary
            fact = {}
            fact_key = parts[1]
            fact_value = parts[2]
            #Apply key and value into the big dictionary (dictionary in dictionary)
            fact[fact_key] = fact_value
            if parts[0] not in data:
                data[parts[0]] = {}
            data[parts[0]].update(fact)
        file_name.close()
    #Checking if there are error, if then print the message
    except OSError:
        print("Error opening file!")
        data =None
    except IndexError:
        print("Error in file!")
        data = None
    return data
def add_data(file_name,department,course,credit):
    """
    add data to the file
    :param file_name: dictionary, dictionary in dictionary loaded before
    :param department: str, the department that needed to add data
    :param course: str, the courses that added to the department
    :param credit: str, the credit point of the course that also be added to the department
    :return: dictionary, the added new dictionary
    """
    #Check if the department in file then add credit
    if department in file_name:
        print(f"Added course {course} to department {department}")
        file_name[department][course] = credit
    #If not create new dictionary and add more credit
    else:
        print(f"Added department {department} with course {course}")
        file_name[department] = {}
        file_name[department][course] = credit
    print()
    return
def credits(file_name,department):
    """
    calculate the sum of credits in given department
    :param file_name: dictionary, dictionary in dictionary loaded before
    :param department:str, the department that need to calculate the sum of credits
    :return:
    """
    sum = 0
    #Checking if department in the file, if yes calculate the sum
    if department in file_name:
        for key in sorted(file_name[department]):
            sum += int(file_name[department][key])
        print(f"Department {department} has to offer {sum} cr.")
    else:
        print("Department not found!")
    print()
    return
def print_de (file_name,department):
    """
    Try to print out the name and credit points of the given department
    :param file_name: dictionary, dictionary in dictionary loaded before
    :param department:str, the name of the department that is needed to print out
    :return:
    """
    #Checking if department in the file, if yes print department
    if department in file_name:
        print(f"*{department}*")
        for key in sorted(file_name[department]):
            print(f"{key} : {file_name[department][key]} cr")
    #If not, print the error sentence
    else:
        print("Department not found!")
    print()
    return
def print_all(file_name):
    """
    print everything in order of department in the file
    :param file_name: dictionary, dictionary in dictionary loaded before
    :return:
    """
    #Firstly, print the department
    for key in sorted(file_name.keys()):
        print(f"*{key}*")
        #create small key and print the course and credits
        for skey in sorted(file_name[key]):
            print(f"{skey} : {file_name[key][skey]} cr")
    print()
    return
def delete(file_name,department,course):
    """
    Try to delete the department or the course in the department of the file
    :param file_name: dictionary, dictionary in dictionary loaded before
    :param department: str, the name of department that needed to delete or the course in the given department
    :param course: str, the course in given department that is needed to be deleted
    :return:
    """
    #Checking if department in the file
    if department in file_name:
        #checking what the course is, if nothing then remove department
        if course == "":
            del(file_name[department])
            print(f"Department {department} removed.")
        #If we have the course, then remove the course in department
        elif course in file_name[department]:
            del(file_name[department][course])
            print(f"Department {department} course {course} removed.")
        #If not then print the sentence
        else:
            print(f"Course {course} from {department} not found!")
    #If cannot find the department in the file, print the error message
    else:
        print(f"Department {department} not found!")
    print()
    return
def main():
    FILE = read_file()
    #if the file could not load, it won't continue
    if FILE == None:
        return
    do_the_loop = True
    while do_the_loop:
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
        choice = input("Enter command: ")
        print()
        choice = choice.strip()
        list_choice = choice.split(" ")
        if list_choice[0] in ["a","A"]:
            list = choice.split(" ")
            small_list = []
            if len(list) > 3:
                for num in range(2,len(list)-1):
                    list1 = list[num]
                    small_list.append(list1)
                    course = " ".join(small_list)
                add_data(FILE,list[1],course,list[-1])
            else:
                print("Invalid command!")
        elif list_choice[0] in ["c","C"]:
            department = choice.split(" ")
            credits(FILE,department[1])
        elif list_choice[0] in ["d","D"]:
            list = choice.split(" ")
            if len(list) == 2:
                course = ""
                delete(FILE,list[1],course)
            else:
                small_list = []
                for num in range(2, len(list)):
                    list1 = list[num]
                    small_list.append(list1)
                    course = " ".join(small_list)
                delete(FILE,list[1],course)
        elif list_choice[0] in ["p","P"]:
            print_all(FILE)
        elif list_choice[0] in ["r","R"]:
            department = choice.split(" ")
            print_de(FILE,department[1])
        elif list_choice[0] in ["q","Q"]:
            do_the_loop = False
            print("Ending program.")
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
