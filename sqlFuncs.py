import sqlite3 as sq

def CreateTable(c,tableName,attr):
    try:
        st=""
        for p in attr:
            if p!=attr[-1]:
                st=st+" ".join(p)+","
            else:
                st=st+" ".join(p)
        print(st)
        c.execute("CREATE TABLE IF EXISTS"+tableName+" ( "+st+" );")
    except :
        print("table already exist, tables cant have same name\nto drop table try command\n\n\'DropTable(cursor,tableName)\'")
    
def DropTable(c,tableName):
    p='''Drop Table '''+tableName+''';'''
    c.execute(p)
    
    
def InsertData(c,tableName,values):
    st=""
    for p in values:
            if p!=values[-1]:
                st=st+''' '''.join(p)+''','''
            else:
                st=st+''' '''.join(p)
    print(st)
    c.execute('''INSERT INTO '''+tableName+''' VALUES ( '''+st+''' );''')
    print("INSERTION COMPLETED")

def getWholeList(c,tableName):
    k=c.execute('''Select * FROM '''+tableName)
    
    return k
def printcol(c,tableName,colName):
   
    k=c.execute("SELECT "+colName+" FROM "+tableName)
    for i in k:
        print(i)
    return k
def PrintRowsWithCond(c,tableName,conditions,colname='*'):
    st=""
    for p in conditions:
            if p!=conditions[-1]:
                st=st+" ".join(p)+","
            else:
                st=st+" ".join(p)
    print(st)
    p=c.execute("SELECT "+colname+" FROM "+tableName+" WHERE "+st+" ;")
    for i in p:
        print(i)
    return p
def InsertMultiData(c,tableName,DataList):
    for values in DataList:
        InsertData(c,tableName,values)

def UpdateRow(c,tableName,values,conditions=""):
    st=''
    for p in values:
            if p!=values[-1]:
                st=st+" = ".join(p)+","
            else:
                st=st+" = ".join(p)
    if(len(conditions) != 0):
        st=st+''' WHERE '''
        for p in conditions:
            if p!=conditions[-1]:
                st=st+" ".join(p)+","
            else:
                st=st+" ".join(p)

    print(st)
    c.execute('''Update '''+tableName+''' SET ''' +st+''' ;''')

def DeleteRow(c,tableName,conditions):
    st=""
    for p in conditions:
            if p!=conditions[-1]:
                st=st+" ".join(p)+","
            else:
                st=st+" ".join(p)
    print(st)
    p=c.execute("DELETE FROM "+tableName+" WHERE "+st+" ;")
    
def DropDb(c,dbName):
    c.execute(''' DROP DATABASE  '''+dbName+''' ; ''')



def TestFuncs():
  try:
    conn=sq.connect("test")
    c=conn.cursor()
    CreateTable(c,"hello",[['''name''','''varchar(10)'''],['''value''','''INTEGER''']])
    InsertData(c,"hello",[['''"shubham"'''],['''3''']])
    InsertData(c,"hello",[['''"subham"'''],['''32''']])
    InsertData(c,"hello",[['''"shuham"'''],['''13''']])
    printWholeList(c,"hello")
    PrintRowsWithCond(c,"hello",[['''name = "shubham"''']],colname='''"name"''')
    UpdateRow(c,"hello",[['''name''','''"shubham"''']],[['''name = "subham"''']])
    DeleteRow(c,"hello",[['''name = "shubham"''']])
    conn.close()
  except:
      print("ERROR in functions")