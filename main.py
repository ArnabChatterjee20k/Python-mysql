import mysql.connector as con

def connection_method_1():
    """Simply connecting to the database"""
    db= con.connect(
        host="localhost",
        user="root",
        password="arnab",
        database="arnab"
    )

    if db.is_connected():
        print("Connection established......")
        cur = db.cursor()

        table = cur.execute("show tables")
        print("tables",cur.fetchall()) # seeing tables
        
        student = cur.execute("select * from student")
        print("student",cur.fetchall()) # seeing data

    else:
        print("Connection not established......")
    
    # closing the cursor
    cur.close()
    
    # closing the connection
    db.close()

def connection_method_2():
    """connection using context manager and using a config variable"""

    con_config = {
        "host" : "localhost",
        "user" : "root",
        "password" : "arnab",
        "database" : "arnab"
    }

    with con.connect(**con_config) as db:
        print(db.is_connected())

connection_method_1()

connection_method_2()