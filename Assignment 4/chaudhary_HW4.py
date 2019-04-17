import employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employees.dat'

def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice


def load_info():
    try:
        input_file = open(FILENAME, 'rb')
        employee_dict = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dict = {}

    return employee_dict


def look_up(employee_dict):

    emp_id = input('Enter the employee ID: ')

    if emp_id in employee_dict:
        print(employee_dict[emp_id])

    else:
        print('Wrong ID number. Please check the ID number you entered.')



def add(employee_dict):

    name = input('Name: ')
    id_number = input('ID number: ')
    department = input('Department: ')
    job_title = input('Job Title: ')

    entry = employee.Employee(name, id_number, department, job_title)

    if id_number not in employee_dict:
        employee_dict[id_number] = entry
        print('The entry has been added.')
    else:
        print('That ID already exists.')


def change(employee_dict):

    emp_id = input('Enter the employee id: ')

    if emp_id in employee_dict:
        name = input('Enter the name: ')

        department = input('Enter the new department: ')

        job_title = input('Enter the new job_title: ')

        entry = employee.Employee(name, emp_id, department, job_title)

        employee_dict[emp_id] = entry
        print('Information updated.')
    else:
        print('That ID is not found.')


def delete(employee_dict):
    emp_id = input('Enter the employee id: ')

    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print('Entry deleted.')
    else:
        print('That name is not found.')


def save_info(employee_dict):
    output_file = open(FILENAME, 'wb')

    pickle.dump(employee_dict, output_file)

    output_file.close()


def main():
    employee_dict = load_info()

    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employee_dict)
        elif choice == ADD:
            add(employee_dict)
        elif choice == CHANGE:
            change(employee_dict)
        elif choice == DELETE:
            delete(employee_dict)

    save_info(employee_dict)

if __name__ == '__main__':
    main()



