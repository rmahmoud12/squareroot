#-------------------------------------------------------------------------------
# Student Name: Rami Mahmoud
# Assignment: HA4
# Python version:
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation
#-------------------------------------------------------------------------------
# Notes:
#-------------------------------------------------------------------------------


import firstname_lastname_HA4_utility as u          #Import Utility file

def read_file():                                    #Function to read text file

    file = open("studentProfile.txt", "r")          #File Opening
    data=file.read()                                #Read Data
    file.close()                                    #Closing File
    return  data                                    #Return File Information



def create_dict(students):                                   #Function to create Dictionary

    student_dict = {}                                # defining an empty students_dict dictionary
    filedata = (students.split("\n"))             #calling read file function to read from file the split data on the bases of \n
    for x in range(len(filedata)):                   #Looping through file
        data = filedata[x].split("|")                #split file information on the basis of |
        key = data[0]                                #Getting Key
        value = data[1:]                             #Getting list of values
        student_dict[key] = value                    #Assigning key value pair to dictionary
    return student_dict                              #Return Student Dictionary



def write_file(students_dict):                             #Function to write data to new text file

    fp = open('studentProfileupdated.txt', 'w')            #Open file in write mode
    for x, y in students_dict.items():                     #Loop through the student Dictionary
        fp.write(x+"|"+y[0]+"|"+y[1]+"|"+y[2]+"\n")        #Write data to file in specific format as given
    fp.close()                                             #Clos file

def main():
    students = read_file()                                                           # read in information and returns students list
    students_dict = create_dict(students)                                           # create students_dict from students list
    menu = '\n\n1. Add\n2. Search\n3. Update\n4. Delete\n5. Display\n6. Exit'
    choice = '0'
    while choice != '6':                                                 #While loop terminates ony when choice is 6
        print(menu)
        choice = input('\nEnter your choice (1-6): ')

        if choice == '1':                                               #Check if choice is 1 or not
            ID = input('Enter student ID to add: ')                     #Taking ID from user
            name = input('Enter full name: ')                            #Taking name from user
            email = input('Enter email address: ')                       #Taking email from user
            major = input('Enter  major: ')                              #Taking major from user
            print(u.add(ID, [name, email, major], students_dict))        #Sending data to function add in utility file


        if choice == '2':                                   #Check if choice is 2 or not
            ID=input('Enter student ID: ')                  #Taking ID from user
            print(u.search(ID,students_dict))               #Sending data to function search in utility file


        if choice == '3':                                                           #Check if choice is 3 or not
            ID=input('Enter student ID to update: ')                                #Taking ID from user
            update_item = input('Which one to update (name/email/major)? ')         #Taking Update-item from user
            updated_info = input('Enter updated info: ')                            #Taking Updated value from user
            print(u.update(ID,update_item,updated_info,students_dict))              #Sending data to function update in utility file


        if choice == '4':                                       #Check if choice is 4 or not
            ID = input('Enter student ID to delete: ')          #Taking ID from user
            print(u.delete(ID,students_dict))                   #Sending data to function delete in utility file


        if choice == '5':                        #Check if choice is 5 or not
            u.display(students_dict)             #Sending data to function display in utility file


        if choice == '6':                           #Check if choice is 6 or not
            write_file(students_dict)               #Sending data to function write file



if __name__ == '__main__':
    main()
