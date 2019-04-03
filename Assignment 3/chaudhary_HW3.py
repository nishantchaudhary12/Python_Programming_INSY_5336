#Assignment 3 INSY 5336
#Nishant Chaudhary
#1001568781


import sqlite3
import sys


def view_players():
    conn = sqlite3.connect('players_Data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM players")
    print('Name\t\t\tWins\t\tLosses\t\tTies\t\tGames')
    print('----------------------------------------------------------')
    data = c.fetchall()
    for each in range(len(data)):
        for elem in range(5):
            print(data[each][elem], end='\t\t\t')
        print('\n')
    conn.close()


def add_players():
    conn = sqlite3.connect('players_Data.db')
    c = conn.cursor()
    name = input('Name: ')
    wins = int(input('Wins: '))
    losses = int(input('Losses: '))
    ties = int(input('Ties: '))
    games = wins + losses + ties
    c.execute("INSERT INTO players VALUES (:Name, :Wins, :Losses, :Ties, :Games)", {'Name': name, 'Wins': wins, 'Losses': losses, 'Ties': ties, 'Games': games})
    print(name, 'was added to the database.')
    conn.commit()
    conn.close()


def delete_player():
    conn = sqlite3.connect('players_Data.db')
    c = conn.cursor()
    name = input('Name: ')
    c.execute("DELETE from players WHERE name = :Name", {'Name': name})
    print(name, 'was deleted from the database.')
    conn.commit()
    conn.close()


def update_info():
    conn = sqlite3.connect('players_Data.db')
    c = conn.cursor()
    name = input('Name: ')
    wins = int(input('Wins: '))
    losses = int(input('Losses: '))
    ties = int(input('Ties: '))
    games = wins + losses + ties
    c.execute("""UPDATE players SET wins = :Wins, losses = :Losses, ties = :Ties, games = :Games
                WHERE name = :Name""",
                
             {'Name': name, 'Wins': wins, 'Losses': losses, 'Ties': ties, 'Games': games}
              )
    print(name, 'info was updates in the database.')
    conn.commit()
    conn.close()


def exit_prog():
    #print('Bye!')
    sys.exit(0)


def menu():
    print('COMMAND MENU')
    print('view - View Players')
    print('add - Add a Player')
    print('del - Delete a Player')
    print('update - Update the details')
    print('exit - Exit the program')


def command():
    menu()
    user_command = input('Command: ')
    while user_command != 'exit':
        if user_command == 'view':
            view_players()
        if user_command == 'add':
            add_players()
        if user_command == 'del':
            delete_player()
        if user_command == 'update':
            update_info()
        menu()
        user_command = input('Command: ')
    if user_command == 'exit':
        print('Bye!')
        exit_prog()


def main():
    # conn = sqlite3.connect('players_Data.db')
    # c = conn.cursor()
    # c.execute("""CREATE TABLE players(
    # Name text NOT NULL,
    # Wins integer NOT NULL,
    # Losses integer NOT NULL,
    # Ties integer NOT NULL,
    # Games integer NOT NULL
    # )""")
    print('Player Manager')
    command()


if __name__ == '__main__':
    main()

