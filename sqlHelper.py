import sqlite3 as sq
import sqlFuncs
  



def saveData(text1,text2):
    conn=sq.connect("task")
    c=conn.cursor()
    
    sqlFuncs.CreateTable(c,"Tasks",[['''title''','''varchar(10)'''],['''descrip''','''varchar(50)''']])
    sqlFuncs.InsertData(c,"Tasks",[[''' " '''+text1+''' " '''],[''' " '''+text2+''' " ''']])
    conn.commit()
    print("COMMITED ")
def getData():
    conn=sq.connect("task")
    c=conn.cursor()
    
    p=sqlFuncs.getWholeList(c,"Tasks")
    
    return p



