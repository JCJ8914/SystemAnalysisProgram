import sqlite3

def clientData():
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS client_data (CusNo INTEGER PRIMARY KEY, CusFirstName text, CusLastName text, CusContact text, CusAddress text, CusRoom text, CusInDate text, CusOutDate text)")
    # cur.execute("DROP TABLE client_data")
    communication.commit()
    communication.close()

def addData(CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    # cur.execute("INSERT INTO Client_data (NULL, ?,?, ?,?, ?,?, ?,?", \
    #     (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))
    cur.execute("INSERT INTO client_data (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))

    communication.commit()
    communication.close()

def viewData():
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("SELECT * FROM client_data")

    rows = cur.fetchall()
    communication.close()
    return rows

def deleteData(CusNo):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("DELETE FROM client_data WHERE CusNo = ?", (CusNo,))
    communication.commit()
    communication.close()


def searchData(CusNo="", CusFirstName="", CusLastName="", CusContact="", CusAddress="", CusRoom="", CusInDate="", CusOutDate=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("SELECT * FROM client_data WHERE CusNo=? OR CusFirstName=? OR CusLastName=? OR CusContact=? OR CusAddress=? OR CusRoom=? OR CusInDate=? OR CusOutDate=?", (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))

    rows = cur.fetchall()
    communication.close()
    return rows

def updateData(CusNo="", CusFirstName="", CusLastName="", CusContact="", CusAddress="", CusRoom="", CusInDate="", CusOutDate=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    # cur.execute("UPDATE client_data SET CusID="" CusFirstName=?, CusLastName=?, CusContact=?, CusAddress=?, CusRoom=?, CusInDate=?, CusOutDate=?", (CusID, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))
    cur.execute("UPDATE client_data SET CusNo=? CusFirstName=?, CusLastName=?, CusContact=?, CusAddress=?, CusRoom=?, CusInDate=?, CusOutDate=?", (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))

    communication.commit()
    communication.close()

#puebla was here
#checks the User's Input and the Database
def getDataFromDatabase(CusFirstName="", CusLastName="",CusRoom=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()

    cur.execute("SELECT CusFirstName,CusLastName,CusRoom FROM client_data WHERE CusFirstName=? AND CusLastName=?  AND CusRoom=? ", (CusFirstName, CusLastName, CusRoom))

    rows = cur.fetchall()
    communication.close()

    #prints empty row
    if rows==[]:
        print("Empty Row")
        return rows
    #returns row if there is a tuple inside rows
    elif rows!=[]:
        print("Ready to Go")
        return rows

clientData()