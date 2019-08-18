import tkinter 
import sqlite3 as sq
import sqlHelper as helper

def getData(e1,e2):
    title=e1.get()
    description=e2.get()
    if len(title)!=0 & len(description):
        helper.saveData(text1=""+title,text2=""+description)




def addTask():
    master=tkinter.Tk()
    
    tkinter.Label(master, text='Title').grid(row=0)    
    tkinter.Label(master, text='TitleDescription').grid(row=1) 
    e1 = tkinter.Entry(master)  
    e2 = tkinter.Entry(master) 
   
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1) 
    print("e1=="+e1.get())
    submit=tkinter.Button(master,height=1,width=10,text="commit",command=lambda:getData(e1,e2))
    submit.grid(row=2,column=1)
    tkinter.mainloop()


def getTask():
    mastera=tkinter.Tk()
    mastera.geometry("500x500")
    taskNumber=0
    
   

    p=helper.getData()
    print(p)
    for i in p:
         tkinter.Text(mastera).grid(row=taskNumber,column=0)   
         tkinter.Text(mastera).grid(row=taskNumber,column=1)
         tasknumber=taskNumber+1


    mastera.mainloop()

getTask()
addTask()

