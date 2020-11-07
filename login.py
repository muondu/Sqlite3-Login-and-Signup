def login():
    global asking
    asking = input("Are you regestered. Yes(y) or No(n):  ")
    if asking == "y" or asking == "Y":
        for i in range(3):
            name = input("PLS enter your name: ")
            if len(name) > 2:
                try:
                    age = int(input("PLS enter your age: "))
                    if age >= 7 or age <=14:
                        try:
                            grade = int(input("PLS enter your grade: "))
                            if grade >=1 or grade <= 8:
                                with sqlite3.connect('main.db') as db:
                                    cursour = db.cursor()
                                find_user = ('SELECT * FROM login WHERE name = ? AND age = ? AND grade = ?')
                                cursour.execute(find_user,[(name), (age),(grade)])
                                results = cursour.fetchall()

                                if results:
                                    for i in results:
                                        buda = str(i)
                                        print("Welcome " +buda)
                                        

                            else:
                                print("Your grade is to high/low to enter.")
                        except ValueError:
                            print("Pls input numbers")
                    else:
                        print("You are too old.")
                except ValueError:
                    print("Pls input numbers")
            else:
                print("I did not undertand ")
                login()
    elif asking == "n" or asking == "N" or asking == "no" or asking == "No":
        def newUser():
            name = input("Please enter a name:  ")
            if len(name) > 2:
                try:
                    age = int(input("Enter your age : "))
                    if age >= 7 or age <=14:
                        try:
                            grade = int(input("Enter your grade:  ")) 
                            if grade >=1 or grade <= 8:
                                insertData = '''INSERT INTO login('name', 'age','grade') 
                                VALUES(?,?,?)'''
                                c.execute(insertData,[(name),(age),(grade)])
                                print("Loading...")
                                time.sleep(3)
                                print("Succesfully done")
                                conn.commit()
                                login() 
                            else:
                                print("Your grade is to high/low to enter")
                        except ValueError:
                            print("Pls input numbers.")
                            newUser()
                    else:
                        print("You are too old.")
                        newUser()
                except ValueError:
                    print("Pls input numbers")
                    newUser()
            elif name.isdigit() == True:
                print("Only put words on your name")
                newUser()
            else:
                print("I did not understand you. Please try again")
                newUser()
        newUser()

    else:
        print("Please input Yes(y) or No(n)")
        login()
login()