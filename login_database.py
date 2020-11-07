import sqlite3
conn = sqlite3.connect('main.db') 
cursour = conn.cursor()
    
cursour.execute("CREATE TABLE IF NOT EXISTS login(name TEXT, age INTEGER, grade INTEGER)")

cursour.execute("INSERT INTO login VALUES('Nesh', 11,7)")
                
                

conn.commit()
                

