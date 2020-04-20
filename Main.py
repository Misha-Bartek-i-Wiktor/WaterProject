import mysql.connector
import datetime
#connection to our remotemysql

WaterConnect = mysql.connector.connect(user='UhpGjwrwo6', password='KeeBeGzEFX',
                                       host='remotemysql.com',
                                       database='UhpGjwrwo6')

mycursor = WaterConnect.cursor()

def welcome(name): #function that say hi to user and asks for a name, if it doesnt exists - creates a table in database

    sql = "CREATE TABLE IF NOT EXISTS " + name + " (date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , " \
                                                 "liquid VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ," \
                                                 " howMuch INT(50) UNSIGNED NOT NULL ) ENGINE = InnoDB;"
    mycursor.execute(sql)
    WaterConnect.commit()


name = input('Enter Your name: ')
welcome(name)

def addLiquid(): #function that adds liquid and saves it into table in database
    print('1 - Water')
    print('2 - Tea')
    print('3 - Coffee')
    print('4 - exit to menu')
    answer = '1', '2', '3', '4'
    add = True
    while add:
        try:
            answer = input('What have you drunk? ')
            if answer == '1':
                    howMuch = int(input('How much ml? '))
                    if howMuch <= 500:
                        sql1 = "INSERT INTO " + name + " (liquid, howMuch) VALUES ('Water', %s)"
                        mycursor.execute(sql1, (howMuch,))
                        WaterConnect.commit()
                        addLiquid()
                    else:
                        print('You can add only 500ml')
                        addLiquid()

            elif answer == '2':
                    howMuch = int(input('How much ml? '))
                    if howMuch <= 500:
                        sql2 = "INSERT INTO " + name + " (liquid, howMuch) VALUES ('Tea', %s)"
                        mycursor.execute(sql2, (howMuch,))
                        WaterConnect.commit()
                        addLiquid()
                    else:
                        print('You can add only 500ml')
                        addLiquid()
            elif answer == '3':
                    howMuch = int(input('How much ml? '))
                    if howMuch <= 500:
                        sql3 = "INSERT INTO " + name + " (liquid, howMuch) VALUES ('Coffee', %s)"
                        mycursor.execute(sql3, (howMuch,))
                        WaterConnect.commit()
                        addLiquid()
                    else:
                        print('You can add only 500ml')
                        addLiquid()

            elif answer == '4':
                    menu()

            else:
                print('Please, try again.')
                addLiquid()
        except: menu()
    else :
        print('Please, try again.')
        addLiquid()

helpdate = datetime.datetime.now() #just a temporary variable
date = helpdate.strftime("%Y-%m-%d") #variable saves current date to show it by default when user calls addLiquid function

def showHistory(): #function that shows a history from date which is chosen by user


    sql = "SELECT SUM(howMuch) FROM " + name + " WHERE date >= '" + date + " 00:00:00' AND date <= '" + date + " 23:59:59'"
    mycursor.execute(sql)
    for x in mycursor:
        print('\nIn total, you drank:', x[0], 'ml of liquid today.')


    while True:
        print('\nDo you want to see a history from another day? Enter Y (Yes) or N (No).')

        a = input()
        if a == 'Y' or a== 'y':
            userdate = input('Choose the date of the day you want to see how much you drank.\n'
                             'In format YYYY-MM-DD: ')

            sql = "SELECT SUM(howMuch) FROM " + name + " WHERE date >= '" + userdate + " 00:00:00' AND date <= '" + userdate + " 23:59:59'"
            mycursor.execute(sql)
            for x in mycursor:
                print("\nThat day you drank:", x[0], "ml")


        elif a == "N" or a == 'n':
            print('Turning back to the menu.')
            menu()

        else:
            print('Wrong symbol. Please, try again.')


def menu(): #main function which is looped
    print('What can I do?: ')
    print('1 - Add liquid')
    print('2 - Show history')
    print('3 - Exit program')
    choose = '1', '2', '3'
    function_menu = True
    while function_menu:
        try:
            choose = input('Please choose: ')
            if choose == '1':
                addLiquid()
            elif choose == '2':
                showHistory()
            elif choose == '3':
                print('Bye!')
                exit(0)
                break
            else:
                print('Wrong number. Please, try again.')
                menu()
        except:
            exit(0)
    else:
        print('Please, try again.')
        menu()



while True:
    menu()
    #print('\n')




WaterConnect.close()