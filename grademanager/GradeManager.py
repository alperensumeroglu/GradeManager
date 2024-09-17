'''
Grade Manager
Project Description:
This application prompts users to enter their name and surname, saving this information to a file. Users can then enter their grades, and the application calculates the average grade, assigning letter grades based on the average. For example, an average of 100 results in an 'AA', and an average of 90 results in a 'BA'. All calculated values are stored in another file.
The application features a menu that runs in an infinite loop until the user decides to quit by entering 'Q' or 'EXIT'. In this menu, users can choose between entering new grades, calculating averages, or saving results.
'''
def save_user_info(name,surname,graders):
    with open('user_info.txt','a',encoding='utf-8') as file:
         file.write(f'{name} {surname}\n')
         for grade in graders:
             file.write(f'{grade}\n') 
#'write` Method: The `write` method does not erase the existing content of the file; it performs the write operation according to the file mode specified by the `open` function. If the file is opened in `'w'` mode, the file content is cleared and new data is written. If the file is opened in `'a'` mode, it appends new data without removing the existing content.
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
def assign_letter_grade(average):
    if average >= 90 and average <= 100:
        return 'AA'
    elif average >= 80 and average <= 89:
        return 'BA'
    elif average >= 70 and average <=79:
        return 'BB'
    elif average >= 60 and average <=69:
        return 'CB'
    elif average >= 50 and average <=59:
        return 'CC'
    else:
        return 'FF'
def save_results(name, surname, average, letter_grade):
    with open('results.txt','a', encoding='utf-8') as file:
        file.write(f'{name} {surname} - average: {average:.2f}, grade: {letter_grade}\n')
    print(f'Results for {name} {surname} have been saved.')
def display_menu():
    print('\nMenu:')
    print('1. Enter new grades.')
    print('2. Calculate averages')
    print('3. Save results')
    print('Q: Quit')
exit_program = False
while not exit_program:
    display_menu()
    choice = input('Choose an option: ').strip().upper()
    if choice == 'Q':
        print('Exiting the program.')
        exit_program = True
    elif choice == '1':
       name = input('Enter your name: ').strip()
       surname = input('Enter your surname: ').strip()
       grades = []
       # Ask how many grades the user wants to enter and ensure a valid number is provided
       try:
           num_of_grades = int(input('How many grades would you like to enter? ').strip())
       except ValueError:
           print('Please enter a valid number.')
           continue
    # Collect the number of grades specified by the user
       for i in range(num_of_grades):
            while True:  # Loop until a valid grade is entered
              try:
                 grade = float(input(f'Enter grade {i+1}: ').strip())
                 grades.append(grade)
                 break  # Exit the loop when a valid grade is entered
              except ValueError:
                 print('Invalid grade. Please enter a valid number.')
       save_user_info(name, surname, grades)
    elif choice == '2':
        try:
            grades = []
            with open('user_info.txt','r',encoding='utf-8') as file:
                for line in file:
                    cleaned_line = line.strip()
                    if cleaned_line.replace(' ','').replace('\n','').isdigit():
                        grades.append(float(cleaned_line))
            if grades:
                average = calculate_average(grades)
                print(f'The average grade is: {average:.2f}')
            else:
                print('No grades found.')
        except FileNotFoundError:
            print('No user information found. Please enter grades first.')
    elif choice == '3':
        try:
            name = input('Enter your name: ').strip()
            surname = input('Enter your surname: ').strip()
            grades = []
            with open('user_info.txt','r',encoding='utf-8') as file:
                for line in file:
                    if line.strip().replace(' ','').replace('\n','').isdigit():
                        grades.append(float(line.strip()))
            if grades:
                average = calculate_average(grades)
                letter_grade = assign_letter_grade(average)
                save_results(name,surname,average,letter_grade)
            else:
                print('No grades found.')
        except FileNotFoundError:
            print('No user information found. Please enter grades first.')
    else:
        print('Invalid option. Please choose again.')
