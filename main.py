#Project "Water"
#v.0.1
#made by Mykhailo Solop, Bartosz Skibiński, Wiktor Rychta

import mysql.connector
import datetime
from User import *
from Liquid import *


def pretty_print(liquids):
    for key, liquid_name in liquids.items():
        print(key + " - " + liquid_name)


def welcome_user():  # function that say hi to user and asks for a name, if it doesnt exists - creates a table in database

    name = input('Enter Your name: ')
    print('Welcome ' + name + '!')
    user = User(name)

    sql = "CREATE TABLE IF NOT EXISTS " + user.name + " (date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, " \
                                                      "liquid_name VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL," \
                                                      "capacity_in_ml INT(50) UNSIGNED NOT NULL ) ENGINE = InnoDB;"
    my_cursor.execute(sql)
    WaterConnect.commit()

    return user.name


def choose_liquid():
    liquids = {
        '1': 'Water',
        '2': 'Tea',
        '3': 'Coffee'
    }
    pretty_print(liquids)
    choose_number = input('What have you drunk? ')
    if choose_number not in liquids:
        print('There is no that liquid')
        choose_liquid()
    liquid_name = liquids.get(choose_number)
    capacity_in_ml = int(input('How much ml? '))
    if capacity_in_ml <= 500:
        liquid = Liquid(liquid_name, capacity_in_ml)
        return liquid
    else:
        print('Please try again')


def add_liquid():  # function that adds liquid and saves it into table in database
    liquid = choose_liquid()

    query = "INSERT INTO " + user_name + " (liquid_name, capacity_in_ml) VALUES (%s, %s)"
    val = (liquid.name, liquid.capacity_in_ml)

    my_cursor.execute(query, val)
    WaterConnect.commit()


def show_history():  # function that shows a history from date which is chosen by user
    sql = "SELECT SUM(capacity_in_ml) FROM " + user_name + " WHERE date >= '" + date + " 00:00:00' AND date <= '" + date + " 23:59:59'"
    my_cursor.execute(sql)
    for x in my_cursor:
        print('\nIn total, you drank:', x[0], 'ml of liquid today.')

    while True:
        print('\nDo you want to see a history from another day? Enter Y (Yes) or N (No).')

        a = input()
        if a == 'Y' or a == 'y':
            userdate = input('Choose the date of the day you want to see how much you drank.\n'
                             'In format YYYY-MM-DD: ')

            sql = "SELECT SUM(capacity_in_ml) FROM " + user_name + " WHERE date >= '" + userdate + " 00:00:00' AND date <= '" + userdate + " 23:59:59'"
            my_cursor.execute(sql)
            for x in my_cursor:
                print("\nThat day you drank:", x[0], "ml")
                break

        elif a == "N" or a == 'n':
            print('Turning back to the menu.')
            menu()
            break

        else:
            print('Wrong symbol. Please, try again.')
            break


def menu():  # main function which is looped
    print('What can I do?: ')
    print('1 - Add liquid')
    print('2 - Show history')
    print('3 - Exit program')
    choose = int(input('Please choose: '))
    if choose == 1:
        add_liquid()
    elif choose == 2:
        show_history()
    elif choose == 3:
        WaterConnect.close()
        print('Bye!')
        exit(0)
    else:
        print('Wrong choice!')


# connection to our remotemysql
WaterConnect = mysql.connector.connect(user='UhpGjwrwo6',
                                       password='KeeBeGzEFX',
                                       host='remotemysql.com',
                                       database='UhpGjwrwo6')

my_cursor = WaterConnect.cursor()

user_name = welcome_user()

helpdate = datetime.datetime.now()  # just a temporary variable
date = helpdate.strftime(
    "%Y-%m-%d")  # variable saves current date to show it by default when user calls addLiquid function

while True:
    menu()
    print('\n')
