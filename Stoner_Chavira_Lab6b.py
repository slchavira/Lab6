"""
Write a program for Professor Polanco at Austin Community College that allows him
to keep a record of the students’ average grade in his class. The program must be
written in accordance with the following specs:

1. The input must be interactive from the keyboard. You will take input for 12 students.
2. You will input the students’ name and an average grade. The student cannot enter
an average below zero or above 100. Your program must raise and handle an
exception should this occur. (LO 5)
a. The exception should cause the program to return and get a new grade
3. Write all output to a file named grades.txt (LO 1, 3, 4)
4. Close the output file. (LO 3, 4)
5. Open the file grades.txt for input. (LO 2)
6. Your program will raise and handle an exception if the file is not found. (LO 5)
a. I will test this aspect by changing the file name and looking for your exception
code (your exception should cause program to ask for correct file name).
7. Read all the records from the file and display them. (LO 2)
"""


# This program will create a record of 12 students' average grades
# and record them to file grades.txt. It will then open the file and
# display all records.

def main():

    # Counter for students
    students = 3
    counter = 0

    # Open file to write to.
    grades_file = open('grades.txt', 'w')

    while counter < students:
        try:
            # Get student's info.
            print('Enter info for student #', counter + 1)
            name = input('Name: ')
            avg_grade = int(input('Grade: '))


            # Write data to grades.txt if 100 <= avg_grade >= 0
            if avg_grade <= 100 and avg_grade >= 0:
                grades_file.write(name + '\n')
                grades_file.write(str(avg_grade) + '\n')

                counter += 1  # Increasing counter by 1

                # Display a blank line.
                print()
            else:
                print('The average grade entered cannot be below ' +
                      '0 or above 100.\n')
        except ValueError:
            print('You must enter a number.\n')


    # Close the file.
    grades_file.close()
    print('Data has been written to grades.txt.\n')

    file_found = False

    while not file_found:

        try:
            # Open the file and read its contents.
            print('before input file')
            infile = open('gradees.txt', 'r')
            print('test')

            """
            # Read in first line from file.
            name = infile.readline()
        
            # If a field was read continue processing file.
            while name != '':
                # Read the next line which would be the student's grade.
                grade = infile.readline()
        
                # Strip the \n from name and grade
                name = name.rstrip('\n')
                grade = grade.rstrip('\n')
        
                # Display the contents.
                print('Name: ' + name)
                print('Grade: ' + grade)
                print()
        
                # Read the next name field for the next record.
                name = infile.readline()
            """


            # Close the file.
            infile.close()

        except FileNotFoundError:
            print('File not found')
            correct_filename = input('What is the correct file name? ')
            #infile = open(correct_filename, 'r')







# Call the main function.
main()
