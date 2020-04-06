import mysql.connector
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
    answer = int(input('What have you drunk? '))
    if answer == 1:
        howMuch = int(input('How much ml? '))
        sql1 = "INSERT INTO " + name + " (liquid, howMuch) VALUES ('Water', %s)"
        mycursor.execute(sql1, (howMuch,))
        WaterConnect.commit()
    elif answer == 2:
        howMuch = int(input('How much ml? '))
        sql2 = "INSERT INTO " + name + " (liquid, howMuch) VALUES ('Tea', %s)"
        mycursor.execute(sql2, (howMuch,))
        WaterConnect.commit()
    elif answer == 3:
        howMuch = int(input('How much ml? '))
        sql3 = "INSERT INTO " + name + " (liquid, howMuch) VALUES ('Coffee', %s)"
        mycursor.execute(sql3, (howMuch,))
        WaterConnect.commit()
    else:
        print('Bye!')
        exit(0)


def showHistory(): #function that shows a history
    sql = "SELECT * FROM " + name + " order by date desc"
    mycursor.execute(sql)
    for x in mycursor:
        print(str(x[0]), str(x[1]), str(x[2]) + ' ml')



def menu(): #main function which is looped
    print('What can I do?: ')
    print('1 - Add liquid')
    print('2 - Show history')
    print('3 - Exit program')
    choose = int(input('Please choose: '))
    if choose == 1:
        addLiquid()
    elif choose == 2:
        showHistory()
    elif choose == 3:
        print('Bye!')
        exit(0)



while True:
    menu()
    print('\n')




WaterConnect.close()