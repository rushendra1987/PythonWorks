import PyMySQL


def mysqlInsert( name, text, createdTime):
    
    db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    insertQueryStr = "insert into <tablename> (<Column names>) values ('" + name +"','"+ text+"','"+ createdTime +"'  )" 
    cursor.execute(insertQueryStr)
    # Fetch a single row using fetchone() method.
    #data = cursor.fetchone()
    print ("Database query : "+ insertQueryStr)
    # disconnect from server
    db.close()