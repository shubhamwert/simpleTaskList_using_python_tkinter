import sqlite3 as sq
import sqlFuncs
  



def saveData(text1,text2):
    conn=sq.connect("task")
    c=conn.cursor()
    
    sqlFuncs.CreateTable(c,[['''title''',text1],['''descrip''',text2]])

    conn.commit()