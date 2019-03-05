# contact list


def add():
    file = open("contact.txt", "a")
    print('Enter the following contact info: ')
    c_name = input('Name: ')
    c_email = input('Email: ')
    c_phone = input('Phone: ')
    insert_string = ",".join([c_name, c_email, c_phone])
    file.write(insert_string + '\n')
    file.write('\n')
    file.close()


def show():
    print('List of contacts: \n')
    file = open("contact.txt", "r")

    for line in file:
        if line != '\n':
            a = line.split(',')
            print('Name:', a[0])
            print('Email:', a[1])
            print('Phone:', a[2])
            print('------------------')
    file.close()


def search(c_name):
    name = list()
    file = open("contact.txt", "r")

    for line in file:
        if line != '\n':
            cl = line.split(',')
            name.append(cl)

    for i in range(len(name)):
        if c_name in name[i][0]:
            # c_index = name.index(c_name)
            print('Name:', name[i][0])
            print('Email:', name[i][1])
            print('Phone:', name[i][2])
    file.close()


def modify(c_name):
    name = list()
    file = open("contact.txt", "r")

    for line in file:
        if line != '\n':
            cl = line.split(',')
            name.append(cl)
    file.close()
    for i in range(len(name)):
        if c_name in name[i][0]:
            name[i][1] = input('Enter the new email to update: ')
            name[i][2] = input('Enter the new phone to update: ') + "\n"
            print('The file has been updated.')
    with open('contact.txt', 'w') as f:
        for item in name:
            insert_string = ",".join(item)
            f.write(insert_string)

    f.close()


def delete(c_name):
    name = list()
    file = open("contact.txt", "r")
    for line in file:
        if line != '\n':
            cl = line.split(',')
            name.append(cl)
    for i in range(len(name)):
        if c_name in name[i][0]:
            del name[i]
            print('The contact has been deleted.')
    file.close()
    with open('contact.txt', 'w') as f:
        for item in name:
            insert_string = ",".join(item)
            f.write(insert_string)
    f.close()


def main():
    choice = 0
    while choice != 6:
        print('''CHOICE MENU
                    1. ADD a Contact
                    2. Show the list of contacts
                    3. Search for a name in the list
                    4. Modify a contact
                    5. Delete a contact from the list
                    6. Quit''')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            add()
            add_element = input('Do you want to add another record: ')
            while add_element == 'Y' or add_element == 'y':
                add()
                add_element = input('Do you want to add another record: ')

        if choice == 2:
            show()

        if choice == 3:
            c_name = input('Enter the name you want to search for: ')
            search(c_name)

        if choice == 4:
            c_name = input('Enter the name you want to search for: ')
            modify(c_name)

        if choice == 5:
            c_name = input('Enter the name you want to search for: ')
            delete(c_name)

        if choice == 6:
            break


if __name__ == "__main__":
    main()
