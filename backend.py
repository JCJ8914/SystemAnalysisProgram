import sqlite3

def clientData():
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS client_data (CusNo INTEGER PRIMARY KEY, CusFirstName text, CusLastName text, CusContact text, CusAddress text, CusRoom text, CusInDate text, CusOutDate text, CusStatus text)")
    # cur.execute("DROP TABLE client_data")
    communication.commit()
    communication.close()

def addData(CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate, CusStatus):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    # cur.execute("INSERT INTO Client_data (NULL, ?,?, ?,?, ?,?, ?,?", \
    #     (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))
    cur.execute("INSERT INTO client_data (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate, CusStatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate, CusStatus))
 
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

def updateData(CusNo="", CusFirstName="", CusLastName="", CusContact="", CusAddress="", CusRoom="", CusInDate="", CusOutDate="", CusStatus=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()
    # cur.execute("UPDATE client_data SET CusID="" CusFirstName=?, CusLastName=?, CusContact=?, CusAddress=?, CusRoom=?, CusInDate=?, CusOutDate=?", (CusID, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate))
    cur.execute("UPDATE client_data SET CusNo=? CusFirstName=?, CusLastName=?, CusContact=?, CusAddress=?, CusRoom=?, CusInDate=?, CusOutDate=?, CusStatus=?", (CusNo, CusFirstName, CusLastName, CusContact, CusAddress, CusRoom, CusInDate, CusOutDate, CusStatus))

    communication.commit()
    communication.close()

#------------------------------------------------Under Construction------------------------------------
# #checks the User's Input and the Database
# def getDataFromDatabase(CusNo="",CusFirstName="", CusLastName="",CusContact="",CusRoom=""):
#     communication = sqlite3.connect("resort_client.db")
#     cur = communication.cursor()

#     cur.execute("SELECT CusNo,CusFirstName,CusLastName,CusContact,CusRoom FROM client_data WHERE CusNo=? AND CusFirstName=? AND CusLastName=? AND CusContact=?  AND CusRoom=? ", (CusNo,CusFirstName, CusLastName,CusContact, CusRoom))

#     rows = cur.fetchall()
#     communication.close()

#     #prints empty row
#     if rows==[]:
#         print("Empty Row")
#         return rows
#     #returns row if there is a tuple inside rows
#     elif rows!=[]:
#         print("Ready to Go")
#         return rows
#bawal same checkin date and checkout date in the same room

#-------------------------------------------------------------------------------------------------------------
#checks the user's Input and their customer No. and Customer Contact
def getDataFromDatabase(CusNo="", CusFirstName="", CusLastName="", CusContact="", CusAddress="", CusRoom="", CusInDate="", CusOutDate="", CusStatus=""):
    communication = sqlite3.connect("resort_client.db")
    cur = communication.cursor()



    # cur.execute("SELECT CusNo, CusContact FROM client_data WHERE CusNo=?  AND CusContact=?  ", (CusNo,CusContact))
    #checks if redudant customer ID
    cur.execute("SELECT CusNo  FROM client_data WHERE CusNo=?   ", [CusNo])
    rows = cur.fetchall()


    #proceeds the next batch
    if rows==[]:
        print("Checks the next one")
        rows=''

    #returns row if there is a tuple inside rows
    elif rows!=[]:
        print("RedudantCustomerNo")
        rows='RedudantCustomerNo'
        communication.close()
        return rows
        
    
    cur.execute("SELECT CusRoom,CusInDate, CusStatus  FROM client_data WHERE CusRoom=? AND CusInDate=? AND CusStatus=?  ", (CusRoom,CusInDate,CusStatus))
    rows = cur.fetchall()


        #prints empty row
    if rows==[]:
        print('All Safe')
        return rows
    #returns row if there is a tuple inside rows
    elif rows!=[]:
        print("RoomTaken is taken")
        rows='RoomTaken'
        communication.close()
        return rows


    # cur.execute("SELECT CusFirstName,CusLastName,  FROM client_data WHERE  CusFirstName=? AND CusLastName=?  ", (CusFirstName,CusLastName))
    # rows = cur.fetchall()

    # if rows==[]:
    #     print('check customer if mahal ka niya')
    #     rows=''
    # #returns row if there is a tuple inside rows
    # elif rows!=[]:
    #     print("I love my customer fam")
    #     rows='CustomerNameAlreadyExists'
    #     communication.close()
    #     return rows




#-- customer ID is the core for this constraints
# -no same room in the the same date 

# customerId
# - different customer ID in the same room in the same date--- BIG NO
# - BUT different customer ID in the same room in the same date IF checkout ang 
# first customer while second customer will checkin in the same date--- BIG YES
#SUGGESTION: ADD A STATE - checkin or checkout

# - same name and last name and the same room but okay kung different date


clientData()