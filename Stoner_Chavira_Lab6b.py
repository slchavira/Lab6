# This program will create a record of 12 students' average grades
# and record them to file grades.txt. It will then open the file and
# display all records.

def main():

    # Counter for students
    students = 12
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

    filename = 'grades.txt'

    while not file_found:

        try:
            # Open the file and read its contents.
            infile = open(filename, 'r')

            file_found = True

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


            # Close the file.
            infile.close()

        except FileNotFoundError:
            print('File not found')
            correct_filename = input('What is the correct file name? ')
            filename = correct_filename


# Call the main function.
main()
